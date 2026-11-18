# ============================================================
#  VN2 • 音频系统
#  ------------------------------------------------------------
#  三个通道：
#    music   主线 BGM（跨章淡入淡出）
#    ambient 环境音（雨、风、虫），随场景切换
#    sound   音效 / 一次性
#  voice 通道 Ren'Py 自带，保留给配音
#  文件缺失时静默跳过，不报错——方便边写剧本边补素材
# ============================================================

init python:

    renpy.music.register_channel("ambient", mixer="sfx", loop=True, tight=True)

    VN2_BGM = {
        # 通用线不再用偏沉、偏紧的 common.mp3，改用已验证更平缓的旧站环境曲。
        # 原曲保留为 common_tense，需要时可以单独换回。
        "common": "audio/bgm/station.mp3",
        "common_tense": "audio/bgm/common.mp3",
        "lan":    "audio/bgm/route_lan.mp3",
        "bai":    "audio/bgm/route_bai.mp3",
        "qing":   "audio/bgm/route_qing.mp3",
        "station": "audio/bgm/station.mp3",
        "ending": "audio/bgm/ending.mp3",
        "end":    "audio/bgm/ending.mp3",
    }

    # 全局限定已设为音乐/音效 50%，不再额外按曲目压电平；
    # 保留这个空表，方便以后需要单独调某首曲子时直接加项。
    VN2_BGM_LEVEL = {}

    VN2_AMB = {
        "rain":   "audio/amb/rain_looped.wav",
        "fire":   "audio/amb/fire_looped.wav",
        "forest": "audio/amb/forest_looped.wav",
        "tunnel": "audio/amb/tunnel_looped.wav",
    }

    # 界面音效（程序化合成，_tools/make_ui_sfx.py，44.1k 立体声 WAV）。
    # 样式层直接引用，这里留一份给脚本调用。本机无 ogg 编码器，故落 WAV。
    VN2_SFX = {
        "click":   "audio/ui/click.wav",
        "hover":   "audio/ui/hover.wav",
        "back":    "audio/ui/back.wav",
        "confirm": "audio/ui/confirm.wav",
        "page":    "audio/ui/page.wav",
        "save":    "audio/ui/save.wav",
    }


    def vn2_playable(path):
        try:
            return bool(path) and renpy.loadable(path)
        except Exception:
            return False


    def vn2_bgm(path_or_key, fade=1.8):
        path = VN2_BGM.get(path_or_key, path_or_key)
        if not vn2_playable(path):
            return False
        try:
            renpy.music.get_channel("music").set_volume(VN2_BGM_LEVEL.get(path, 1.0))
        except Exception:
            pass
        renpy.music.play(path, channel="music", loop=True, fadein=fade, fadeout=fade)
        return True


    def vn2_bgm_for_route(route):
        """按章节所属的线切 BGM，找不到就沿用上一首。"""
        return vn2_bgm(route if route in VN2_BGM else "common")


    def vn2_menu_music():
        """主菜单音乐：换成更平缓的旧站环境曲，避免开局像进战斗。"""
        try:
            cur = renpy.music.get_playing(channel="music")
            if cur and cur.endswith("station.mp3"):
                return True
        except Exception:
            pass
        return vn2_bgm("station", fade=2.4)


    def vn2_amb(path_or_key=None, fade=1.2):
        """换环境音；传 None 表示淡出停掉。"""
        if path_or_key is None:
            renpy.music.stop(channel="ambient", fadeout=fade)
            return True

        path = VN2_AMB.get(path_or_key, path_or_key)
        if not vn2_playable(path):
            return False

        renpy.music.play(path, channel="ambient", loop=True, fadein=fade, fadeout=fade)
        return True


    def vn2_sfx(path, fade=0.2):
        if not vn2_playable(path):
            return False
        renpy.sound.play(path, channel="sound", fadein=fade)
        return True


    def vn2_audio_stop(fade=1.5):
        renpy.music.stop(channel="music", fadeout=fade)
        renpy.music.stop(channel="ambient", fadeout=fade)


# 语音重播位用：写剧本时 $ vn2_current_voice = "voice/xxx.ogg"
default vn2_current_voice = None

init 999 python:

    def _vn2_apply_mix_once():
        """老 persistent 只迁移一次：语音 90，音乐/音效 50。
        玩家之后仍可在设置里自由调整，不会被每次启动重置。"""
        if getattr(persistent, "vn2_mix_v4", False):
            return
        persistent.vn2_mix_v4 = True
        try:
            preferences.set_mixer("music", 0.50)
            preferences.set_mixer("sfx", 0.50)
            preferences.set_mixer("voice", 0.90)
            preferences.emphasize_audio = True
        except Exception:
            pass

    _vn2_apply_mix_once()

init python:

    VN2_VOICED_NAMES = {info.get("name") for key, info in VN2_CAST.items() if key != "zhou"}

    def vn2_history_voice(d):
        """把当前语音文件塞进 history 条目，回想里就能重播。
        旁白、玩家/老周不挂语音，避免把上一句角色台词误挂到旁白上。"""
        try:
            if getattr(d, "who", None) in VN2_VOICED_NAMES:
                d.voice = store.vn2_current_voice
            else:
                d.voice = None
        except Exception:
            pass

    if vn2_history_voice not in config.history_callbacks:
        config.history_callbacks.append(vn2_history_voice)
