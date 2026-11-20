# ============================================================
#  VN2 • 好感度与旗标
#  ------------------------------------------------------------
#  变量本体在 00_state.rpy 里用 default 声明；这里只放读写函数。
#  所有写入都做 0–100 夹取，避免脚本写错数字把存档写炸。
# ============================================================

init -1 python:

    # schema 2 起已删除的旧键：旧稿章节若残留调用，记日志后跳过，
    # 不抛异常打断流程（写作线并行整改期间的兼容兜底）。
    _VN2_LEGACY_AFF = {"zhou"}
    _VN2_LEGACY_FLAGS = {"trust_zhou", "heard_zhou_past"}


    def vn2_aff_value(key):
        """取某个角色的好感度（key: lan/bai/qing/ari）。"""
        return int(getattr(store, "aff_" + key, 0) or 0)


    def vn2_aff_add(key, amount, notify=True):
        """加/减好感，自动夹在 0–100，并在右上角提示。"""
        if key in _VN2_LEGACY_AFF:
            renpy.log("VN2: legacy aff_%s dropped (schema 2)" % key)
            return vn2_aff_value(key)
        if key not in VN2_AFF_KEYS:
            raise ValueError("unknown affinity key: %r" % (key,))

        old = vn2_aff_value(key)
        new = max(0, min(100, old + int(amount)))
        setattr(store, "aff_" + key, new)

        if notify and amount:
            name = VN2_CHAR_NAMES.get(key, key)
            sign = "+" if amount > 0 else ""
            renpy.notify("%s  %s%d" % (name, sign, int(amount)))

        return new


    def vn2_set_aff(key, value):
        """直接设定好感（章节调试/初始化用）。"""
        if key in _VN2_LEGACY_AFF:
            renpy.log("VN2: legacy aff_%s dropped (schema 2)" % key)
            return
        if key not in VN2_AFF_KEYS:
            raise ValueError("unknown affinity key: %r" % (key,))
        setattr(store, "aff_" + key, max(0, min(100, int(value))))


    def vn2_flag(name, value=True):
        """设置布尔旗标，必须在 00_state.rpy 里先 default 过。"""
        if name in _VN2_LEGACY_FLAGS:
            renpy.log("VN2: legacy flag %s dropped (schema 2)" % name)
            return
        if name not in VN2_DEFAULT_VALUES:
            raise ValueError("unknown flag: %r" % (name,))
        setattr(store, name, bool(value))


    def vn2_aff_summary():
        """存档卡片上的一行好感摘要。"""
        parts = []
        for key in VN2_AFF_KEYS:
            parts.append("%s %d" % (VN2_CHAR_NAMES[key], vn2_aff_value(key)))
        return "  ".join(parts)


    def vn2_route_label(key):
        return VN2_ROUTE_NAMES.get(key, key)


    def vn2_reset_run():
        """新游戏开局：好感与旗标回到初始值。"""
        for key in VN2_AFF_KEYS:
            vn2_set_aff(key, VN2_DEFAULT_VALUES["aff_" + key])

        for key, value in VN2_DEFAULT_VALUES.items():
            if isinstance(value, bool):
                setattr(store, key, value)

        store.vn2_lock_route = VN2_DEFAULT_VALUES["vn2_lock_route"]
        store.vn2_ending_key = VN2_DEFAULT_VALUES["vn2_ending_key"]
        store.vn2_story_mode = VN2_DEFAULT_VALUES["vn2_story_mode"]
        store.vn2_story_rev = VN2_DEFAULT_VALUES["vn2_story_rev"]

        # 笔记本按「每局」清账：新开一局，上一局的情报与已读标记都不再跟着走。
        persistent.vn2_intel_seen = set()
