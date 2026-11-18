# ============================================================
#  VN2 • 打字音（ROUND3 音频 / ROUND4 改为周期回调）
#  ------------------------------------------------------------
#  只在台词逐字慢速显示时播极短 tick，跟随文字速度；打断 / 快进 /
#  瞬时文本 / 静音时立刻停，不残留、不循环、不抢 BGM。
#
#  旧实现用不可见 screen + ATL function 循环，实测在 say 交互里
#  ticker 屏被清掉，10/10 采样都拿不到屏，声音自然没响。
#  现在改走 config.periodic_callbacks：由角色回调维护
#  “正在逐字显示”状态，显示循环每帧检查时间到点就播一声。
#  不依赖 screen，也不会把 time 模块写进 store。
# ============================================================

init offset = 1

default vn2_type_active = False
default vn2_type_next = 0.0
default vn2_type_interval = 0.30


init python:

    # ---- 专用通道（sfx mixer，stop_on_mute 随静音开关收声） ----
    if not renpy.music.channel_defined("vn2_type"):
        renpy.music.register_channel(
            "vn2_type", mixer="sfx", loop=False, stop_on_mute=True)

    VN2_TYPE_TICKS = [
        "audio/ui/type_1.wav",
        "audio/ui/type_2.wav",
        "audio/ui/type_3.wav",
    ]


    def vn2_type_now():
        # 局部导入，避免 time 模块对象进入 store 后被存档 pickle。
        import time
        return time.monotonic()


    def vn2_type_allowed():
        """当前是否允许播打字音：非快进 / 非跳过 / 文字速度 > 0。"""
        try:
            if renpy.is_skipping():
                return False
            if renpy.config.skipping == "fast":
                return False
        except Exception:
            return False
        cps = renpy.game.preferences.text_cps
        if cps is None or cps <= 0:
            return False
        return True


    def vn2_type_play():
        """播一个随机变体；返回是否真的播了。"""
        try:
            path = renpy.random.choice(VN2_TYPE_TICKS)
            if renpy.loadable(path):
                renpy.sound.play(path, channel="vn2_type")
                return True
        except Exception:
            pass
        return False


    def vn2_type_off():
        """立刻停声并清状态（幂等，可重复调用）。"""
        store.vn2_type_active = False
        try:
            renpy.sound.stop(channel="vn2_type")
        except Exception:
            pass


    def vn2_type_periodic():
        """显示循环每帧调用：到点播 tick，不满足条件就收声。"""
        if not getattr(store, "vn2_type_active", False):
            return
        if not vn2_type_allowed():
            vn2_type_off()
            return

        now = vn2_type_now()
        if now < getattr(store, "vn2_type_next", 0.0):
            return

        vn2_type_play()
        interval = getattr(store, "vn2_type_interval", 0.30)
        store.vn2_type_next = now + max(0.06, interval)


    def vn2_type_start():
        cps = float(renpy.game.preferences.text_cps)
        # 每 3 个字一个 tick；间隔随 cps 走，上下夹逼避免极端速度下机关枪 / 拖拍
        interval = 3.0 / cps
        interval = min(max(interval, 0.06), 0.60)
        store.vn2_type_interval = interval
        store.vn2_type_active = True
        store.vn2_type_next = vn2_type_now()
        vn2_type_periodic()


    def vn2_type_cb(event, interact=True, **kwargs):
        try:
            if event == "begin":
                # 新一句先清掉上一句可能残留的声音 / 状态
                vn2_type_off()
            elif event == "show":
                if interact and vn2_type_allowed():
                    vn2_type_start()
            elif event in ("slow_done", "interact_done", "end"):
                vn2_type_off()
        except Exception:
            vn2_type_off()


    if vn2_type_cb not in config.all_character_callbacks:
        config.all_character_callbacks.append(vn2_type_cb)

    # Ctrl 快进起步即停（fast skip 路径不会走 say 回调，这里兜底）
    if vn2_type_off not in config.fast_skipping_callbacks:
        config.fast_skipping_callbacks.append(vn2_type_off)

    # 显示循环周期回调（不依赖 screen，避免 transient 屏被清掉）
    if vn2_type_periodic not in config.periodic_callbacks:
        config.periodic_callbacks.append(vn2_type_periodic)
