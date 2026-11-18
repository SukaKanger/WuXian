# ============================================================
#  VN2 • 剧情 CG 全屏层（一代 CG 批次）
#  ------------------------------------------------------------
#  CG 本身已有角色，显示时不再渲染立绘；对话、语音、HUD 全部照常。
#  用法：
#      $ vn2_cg_show("images/cg/cg01.png")     # 或旧 id "cg_camp_fire_v1"
#  每张图的入画方向 / 缩放 / 黑场 / 换曲参数在 66_cg_fx.rpy。
#  任意 scene 语句都会清掉 CG 层；章节结束进下一章时自动恢复背景。
#  ============================================================

init -1 python:

    def vn2_cg_show(img, trans=None, cid=None):
        """全屏显示一张 24 张正片 CG 之一，走它专属的入画演出。
        立绘 tag 全部隐藏，但 vn2_stage 保留，
        确保 CG 收起后角色能回到原来的位置和表情。"""
        cid2 = cid or vn2_cg_resolve(img)
        spec = vn2_cg_fx(cid2) if cid2 else VN2_CG_FX_DEFAULT
        path = vn2_cg_path(cid2) if cid2 else img

        store.vn2_cg_scene = True
        store.vn2_cg_current = cid2

        for key in VN2_SPRITE_TAGS:
            try:
                renpy.hide(VN2_CAST[key]["tag"])
            except Exception:
                pass

        # 进场换曲：只有登记过 bgm 的 CG 才动，其余沿用当前 BGM
        if spec.get("bgm"):
            vn2_bgm(spec["bgm"], fade=spec.get("bgm_fade", 1.8))

        black = spec.get("black", 0.0)

        # 快进时不要演入画：直接落定，避免动画把快进节奏打断。
        if renpy.get_skipping():
            try:
                renpy.show(
                    "vn2_cg_frame",
                    what=renpy.displayable(path),
                    tag="vn2_cg_frame",
                    at_list=[Transform(xalign=0.5, yalign=0.5, zoom=1.0)],
                    zorder=30,
                )
            except Exception as e:
                renpy.log("VN2 CG show failed: %r" % (e,))
            if black > 0:
                renpy.with_statement(None)
            return

        # 先压黑，再让画面从黑里亮起来；黑场期间画面已经就位，
        # 亮起后只做很轻的漂移和推近，不再横向滑进。
        if black > 0:
            renpy.with_statement(renpy.store.Fade(black, 0.02, 0.0))

        settle_dur = max(2.0, min(3.2, float(spec.get("dur", 2.0))))
        settle_push_t = max(2.6, float(spec.get("push_t", 3.0)))
        z_start = min(1.08, max(0.96, float(spec.get("z0", 1.0))))
        reveal = max(0.55, float(spec.get("reveal", 0.8)))

        try:
            renpy.show(
                "vn2_cg_frame",
                what=renpy.displayable(path),
                tag="vn2_cg_frame",
                at_list=[vn2_cg_settle(spec["sx"], spec["sy"], z_start,
                                       settle_dur, spec["push"],
                                       settle_push_t, reveal)],
                zorder=30,
            )
        except Exception as e:
            renpy.log("VN2 CG show failed: %r" % (e,))

        if black > 0:
            renpy.with_statement(renpy.store.Fade(0.02, 0.0, reveal))
        elif trans is not None:
            renpy.with_statement(trans)


    def vn2_cg_hide(trans=None):
        """收起 CG，并按 vn2_stage 把立绘恢复回来。"""
        try:
            renpy.hide("vn2_cg_frame")
        except Exception:
            pass
        store.vn2_cg_scene = False
        for key, item in (store.vn2_stage or {}).items():
            info = VN2_CAST.get(key)
            if not info:
                continue
            try:
                renpy.show(
                    item["img"],
                    tag=info["tag"],
                    at_list=[vn2_pose(item.get("pos", "center"), item.get("lit", 1.0))],
                    zorder=20,
                )
            except Exception:
                pass
        if trans is not None and not renpy.get_skipping():
            renpy.with_statement(trans)


    def vn2_scene_cb(layer):
        """scene 语句清空 master 层时，同步退出 CG 模式。"""
        if layer == "master":
            store.vn2_cg_scene = False


    if vn2_scene_cb not in config.scene_callbacks:
        config.scene_callbacks.append(vn2_scene_cb)


default vn2_cg_scene = False
