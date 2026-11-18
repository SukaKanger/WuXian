# ============================================================
#  VN2 • CG 画廊数据（一代 CG 24 张｜6 卡 × 4 页）
#  ------------------------------------------------------------
#  每页 3×2 六格，共 4 页；缩略图为 426×272 圆角 cover。
#  这 24 张是当前一代 CG 的剧情 CG 集合，先作为本作正式画廊。
# ============================================================

init -1 python:

    VN2_GALLERY = [
        dict(id="cg_camp_fire_v1", title="营火", sub="共同线｜第 1 章",
             img="images/cg/cg01.png", ratio=(1920, 1080)),
        dict(id="cg_key_rope_anchor_v2", title="断崖的绳锚", sub="共同线｜第 3 章",
             img="images/cg/cg02.png", ratio=(1920, 1080)),
        dict(id="cg_key_four_people_v0", title="四个人的夜", sub="共同线｜第 4 章",
             img="images/cg/cg03.png", ratio=(1920, 1080)),
        dict(id="cg_key_gate_v1", title="门口", sub="共同线｜第 15 章",
             img="images/cg/cg04.png", ratio=(1920, 1080)),
        dict(id="cg_key_badge_v2", title="旧队徽", sub="共同线｜第 16 章",
             img="images/cg/cg05.png", ratio=(1920, 1080)),
        dict(id="cg_key_half_name_v0", title="雾里的名字", sub="共同线｜第 17 章",
             img="images/cg/cg06.png", ratio=(1920, 1080)),

        dict(id="cg_route_lan_ridge_v0", title="山脊", sub="蓝羽线｜第 17 章",
             img="images/cg/cg07.png", ratio=(1920, 1080)),
        dict(id="cg_key_half_map_v2", title="半张地图", sub="共同线｜第 18 章",
             img="images/cg/cg08.png", ratio=(1920, 1080)),
        dict(id="cg_key_half_pill_v2", title="半片药", sub="共同线｜第 19 章",
             img="images/cg/cg09.png", ratio=(1920, 1080)),
        dict(id="cg_key_crush_v0", title="药瓶", sub="共同线｜第 19 章",
             img="images/cg/cg10.png", ratio=(1920, 1080)),
        dict(id="cg_key_surgery_v1", title="灯下手术", sub="共同线｜第 20 章",
             img="images/cg/cg11.png", ratio=(1920, 1080)),
        dict(id="cg_route_bai_ward_v0", title="站门外", sub="白砚线｜第 21 章",
             img="images/cg/cg12.png", ratio=(1920, 1080)),

        dict(id="cg_key_archive_v1", title="档案室", sub="共同线｜第 22 章",
             img="images/cg/cg13.png", ratio=(1920, 1080)),
        dict(id="cg_route_qing_ruins_v0", title="遗迹", sub="青岩线｜第 24 章",
             img="images/cg/cg14.png", ratio=(1920, 1080)),
        dict(id="cg_key_settle_v2", title="结算", sub="共同线｜第 25 章",
             img="images/cg/cg15.png", ratio=(1920, 1080)),
        dict(id="cg_key_dawn_v2", title="出林", sub="共同线｜第 28 章",
             img="images/cg/cg16.png", ratio=(1920, 1080)),
        dict(id="cg_end_lan_together_v1", title="蓝羽｜同行", sub="结局",
             img="images/cg/cg17.png", ratio=(1920, 1080)),
        dict(id="cg_end_lan_alone_v0", title="蓝羽｜独行", sub="结局",
             img="images/cg/cg18.png", ratio=(1920, 1080)),

        dict(id="cg_end_bai_together_v1", title="白砚｜同行", sub="结局",
             img="images/cg/cg19.png", ratio=(1920, 1080)),
        dict(id="cg_end_bai_alone_v0", title="白砚｜独行", sub="结局",
             img="images/cg/cg20.png", ratio=(1920, 1080)),
        dict(id="cg_end_qing_together_v0", title="青岩｜同行", sub="结局",
             img="images/cg/cg21.png", ratio=(1920, 1080)),
        dict(id="cg_end_qing_alone_v1", title="青岩｜独行", sub="结局",
             img="images/cg/cg22.png", ratio=(1920, 1080)),
        dict(id="cg_end_sealed_v1", title="封口", sub="结局",
             img="images/cg/cg23.png", ratio=(1920, 1080)),
        dict(id="cg_end_seventh_v0", title="第七天", sub="结局",
             img="images/cg/cg24.png", ratio=(1920, 1080)),
    ]

    # 画廊固定 6 卡一页、4 页；总数与主菜单进度共用同一个口径。
    VN2_GALLERY_PER_PAGE = 6
    VN2_GALLERY_SLOTS = 24

    # 老章节里仍可能调用一代 CG 的旧 id（如 cg_zhou / cg_lan / cg_bai / cg_qing），
    # 这些图存在，但不占 24 张画廊的格子。未知 id 也只记日志，不让剧情崩掉。
    VN2_STORY_ONLY_CG = {"cg_zhou", "cg_lan", "cg_bai", "cg_qing"}

    def vn2_cg_total():
        return len(VN2_GALLERY)

    def vn2_cg_item(cid):
        for item in VN2_GALLERY:
            if item["id"] == cid:
                return item
        return None

    def vn2_cg_unlocked(cid):
        return cid in (persistent.vn2_cg or set())

    def vn2_unlock_cg(cid, quiet=False):
        item = vn2_cg_item(cid)
        if item is None:
            if cid in VN2_STORY_ONLY_CG:
                renpy.log("VN2: story-only CG %r is outside the 24-slot gallery; skipped." % (cid,))
            else:
                renpy.log("VN2: unknown CG %r; unlock skipped instead of crashing." % (cid,))
            return False

        if vn2_cg_unlocked(cid):
            return False

        pool = set(persistent.vn2_cg or set())
        pool.add(cid)
        persistent.vn2_cg = pool

        if not quiet:
            renpy.notify("CG 已收入画廊：%s" % item["title"])

        return True

    def vn2_cg_count():
        return len([cid for cid in (persistent.vn2_cg or set())
                    if vn2_cg_item(cid) is not None])

    def vn2_endings_count():
        keys = {item.get("key") for item in vn2_endings_matrix()}
        return len([key for key in (persistent.vn2_endings or set())
                    if key in keys])

    # 画廊改为逐张解锁：由各章节 / 结局在剧本里调用 vn2_unlock_cg，
    # 不再在开局把 24 张一次性塞进 persistent。老档若已被旧逻辑写满，
    # 用「一键重置画廊」清掉即可（见 vn2_cg_reset 调试入口）。

    def vn2_cg_reset():
        """清空本机画廊收集（调试 / 老档清库存用）。"""
        persistent.vn2_cg = set()
        persistent.vn2_gallery_seeded_24 = False
        return True

    # 升级兼容：旧版开局会自动把 24 张塞进收藏，这里识别旧标记后清一次。
    # 新版正常游玩解锁的档没有这个标记，不会被误清。
    if getattr(persistent, "vn2_gallery_seeded_24", False):
        persistent.vn2_cg = set()
        persistent.vn2_gallery_seeded_24 = False
