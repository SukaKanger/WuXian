# ============================================================
#  VN2 • 存档系统（schema 2）
#  ------------------------------------------------------------
#  1) 手动槽位：每槽写入「第 N 章 / 谁的线 / 好感摘要 / 时间」
#     —— 走 config.save_json_callbacks，存档时自动采集当前上下文
#  2) 自动存档：进新章 + 每次弹选项前，只留最近 5 个
#  3) 兼容层：存档写 vn2_schema；读档时 vn2_repair_state() 补缺失变量，
#     丢弃 schema 2 已删除的旧变量
# ============================================================

define config.autosave_slots = 5
define config.has_autosave = True
define config.autosave_on_choice = True
# 退出时自动存档会拍到主菜单/启动页，覆盖章节缩略图；关掉，保留进章与选项自动存档。
define config.autosave_on_quit = False


init python:
    # 存档缩略图 16:9（gui.rpy 里已 define 过，这里只能赋值，不能重复 define）
    config.thumbnail_width = 384
    config.thumbnail_height = 216


init python:

    # schema 2 已删除的旧变量：读档时从 store 上摘掉
    _VN2_DROPPED_VARS = ("aff_zhou", "trust_zhou", "heard_zhou_past")

    # 当前生效的布尔旗标（迁移时强制 bool 化）
    _VN2_BOOL_FLAGS = (
        "trust_team", "close_lan", "lan_map_fixed", "saved_bai",
        "bai_treated", "bai_rationed", "know_qing_secret", "qing_trusted", "station_key",
        "evidence_kept", "evidence_copied", "trust_shiqi", "ari_helped",
    )


    def vn2_save_json(d):
        """每次存档时把当前章节上下文写进存档元数据。"""
        d["vn2_schema"] = VN2_SAVE_SCHEMA
        d["vn2_player"] = getattr(store, "player_name", "队长") or "队长"
        d["vn2_chapter"] = getattr(store, "vn2_chapter_title", "") or ""
        d["vn2_chapter_no"] = int(getattr(store, "vn2_chapter_no", 0) or 0)
        d["vn2_route"] = getattr(store, "vn2_route_name", "") or ""
        d["vn2_day"] = int(getattr(store, "vn2_day", 0) or 0)
        d["vn2_aff"] = vn2_aff_summary()
        d["vn2_top"] = getattr(store, "vn2_lock_route", "solo")
        d["vn2_chapter_id"] = getattr(store, "vn2_chapter_id", "ch01")
        d["vn2_disp_label"] = getattr(store, "vn2_disp_label", "") or ""
        d["vn2_lock_route"] = getattr(store, "vn2_lock_route", "solo")


    # 注册进 Ren'Py 的存档元数据回调
    if vn2_save_json not in config.save_json_callbacks:
        config.save_json_callbacks.append(vn2_save_json)


    def vn2_repair_state():
        """老档兼容：补齐缺失的 default 变量，丢弃已删变量，校正章节上下文。"""
        # 1) 补齐当前 schema 的默认值
        for key, value in VN2_DEFAULT_VALUES.items():
            if key not in vars(store):
                setattr(store, key, value)

        # 2) 摘掉 schema 2 已删除的旧变量
        for dropped in _VN2_DROPPED_VARS:
            if hasattr(store, dropped):
                try:
                    delattr(store, dropped)
                except Exception:
                    pass

        # 3) 锁线结果兜底：旧档没有 vn2_lock_route 时按 solo 处理并记日志
        if not getattr(store, "vn2_lock_route", None):
            renpy.log("VN2: legacy save without vn2_lock_route, fallback solo")
            store.vn2_lock_route = "solo"

        # 4) 旗标必须是 bool，防止旧档里是 0/1
        for key in _VN2_BOOL_FLAGS:
            if hasattr(store, key):
                setattr(store, key, bool(getattr(store, key)))

        # 5) 好感度夹取；旧 aff_zhou 已在上一步摘除
        for key in VN2_AFF_KEYS:
            vn2_set_aff(key, vn2_aff_value(key))

        # 6) 校正章节上下文
        cid = getattr(store, "vn2_chapter_id", "ch01")
        if cid not in CHAPTERS:
            cid = "ch01"
            store.vn2_chapter_id = cid

        ch = CHAPTERS.get(cid)
        if ch:
            store.vn2_chapter_no = ch["no"]
            store.vn2_chapter_title = ch["title"]
            store.vn2_disp = ch["disp"]
            store.vn2_disp_label = vn2_chapter_label(cid)
            store.vn2_route_key = ch["route"]
            store.vn2_route_name = vn2_route_label(ch["route"])
            store.vn2_day = ch["day"]

        return True


    def vn2_continue_slot():
        """主菜单「继续」用：返回最近一次存档的槽位名。"""
        try:
            return renpy.newest_slot()
        except Exception:
            return None


    def vn2_save_schema_of(slot):
        """读某个槽位的 schema 版本（老档没有这个字段时返回 0）。"""
        try:
            return int(FileJson(slot, "vn2_schema", missing=0) or 0)
        except Exception:
            return 0


label after_load:
    $ vn2_repair_state()
    $ renpy.notify("已载入 • 第 %d 章 %s" % (vn2_chapter_no, vn2_chapter_title))
    return
