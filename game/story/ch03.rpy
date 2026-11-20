# 第 3 章 • 断崖（第 3 天 / 共同线）
# 节点：1 塌方断崖 · 2 活锚（menu）· 3 崖顶歇脚 · 4 谁先处理伤（menu）
#       · 5 绳归谁收（menu）· 6 雨里清点 · 7 左臂 · 8 雾压下来 · 9 下山
#
# 表情规则：每句角色台词前用 $ vn2_face("角色", "表情") 显式指定。

label ch03:
    $ vn2_unlock_cg("cg_key_rope_anchor_v2")

    scene bg cliff with slow_fade
    $ vn2_enter_chapter("ch03")
    call vn2_title_card(3, "断崖", "第 3 天 • 共同线")
    $ vn2_amb("rain")

    # --- 节点 1/9 · 塌方断崖 ---
    $ vn2_show("bai", expr="surprised", pos="right", trans=dissolve_soft)
    $ vn2_cg_show("images/cg/cg_key_rope_anchor_v2.png", trans=dissolve_soft)

    nar "断崖在半路。塌方把整片坡削了下去，露出底下白生生的石头。雨从上午下着，碎石还在往下滑。"
    $ vn2_current_voice = "voice/bai/bai_0014.ogg"
    voice "voice/bai/bai_0014.ogg"
    $ vn2_face("bai", "surprised")
    bai "石头还在动。别靠边。"

    nar "没有路。绕过去要多两天，队伍等不起。要过，只能把绳固定在崖顶，人先下去做锚。崖顶的岩缝里卡着一截旧绳桩，打法和你腕上的结一样。"
    think "十年前那支队伍，也在这里下过崖。"
    nar "断崖两侧的树被掀掉大半，坡底被雨和雾搅成白蒙蒙一片。你把绳头要过来，缠进自己腕口，先下了坡。左胳膊卡进石缝，肩顶住一块斜石。"
    think "胳膊像被石头咬住。绳还牢。"

    # --- 节点 2/9 · 活锚（menu） ---
    menu:
        "你当活锚，把全队换过去":
            $ vn2_flag("trust_team")
            $ vn2_aff_add("lan", 3)
            nar "绳在你掌心勒出一道红。最后一个人离开坡面，你才把胳膊从石缝里抽出来。"
            zhou "记着。这条绳，以后归我收。"
            nar "你没喊疼。只是把绳卷得很紧，紧到手指发白。石缝的边磨着袖子。你换了个肩顶住斜石，绳从腕口绕到掌心，身后的人踩着你让出的位置，一个一个过去。绳勒出的红印过了很久才消。"

        "先固定绳结，再放第二个人下去":
            $ vn2_aff_add("bai", 4)
            nar "白砚把绳结打在树干上，试了三次。"
            $ vn2_current_voice = "voice/bai/bai_0015.ogg"
            voice "voice/bai/bai_0015.ogg"
            $ vn2_face("bai", "angry")
            bai "不稳就是死。稳了再动。"
            nar "等绳稳了，才有第二个人的位置。你自己攀了上来。树干歪在坡边。他把绳绕两圈，压一道活扣，拽了三回确认吃劲，才把绳尾交出来。他拽绳时小臂绷起来，松开时指节上的白才退下去。"

        "先抢回滚下坡的样本箱":
            $ vn2_aff_add("qing", 4)
            $ vn2_hide("bai")
            $ vn2_show("qing", expr="happy", pos="center")
            nar "样本箱卡在石缝底下。你探身把它勾上来，箱扣没开。"
            $ vn2_current_voice = "voice/qing/qing_0008.ogg"
            voice "voice/qing/qing_0008.ogg"
            $ vn2_face("qing", "happy")
            qing "箱子比人慢一步。谢了。"
            nar "箱子从碎石缝里拔出来，带落一片石屑。你把箱底托稳，递回给他。他接过去先掀扣看分格，才把箱子抱回怀里。"

    $ vn2_hide_all(trans=dissolve_soft)

    # --- 节点 3/9 · 崖顶歇脚 ---
    nar "崖顶歇脚时，白砚小腿上划了一道口子，血顺着毛往下淌。他先蹲到你胳膊边，看你那条还没抬起来的左臂，才给自己包。岩台背风，四个人的包搁在四角，药箱搁在石头上。青岩坐在你旁边，样本箱搁在两人中间。他把箱扣掀开一道缝，看了看，又合上。"
    think "先处理谁的伤。伤口都在身上，急的程度不一样。"

    # --- 节点 4/9 · 谁先处理伤（menu） ---
    menu:
        "让白砚先看你的左胳膊":
            $ vn2_aff_add("bai", 3)
            $ vn2_show("bai", expr="sad", pos="center")
            nar "白砚按到你肩头，你没躲。他捏了捏上臂，摇头，没说话。"
            $ vn2_current_voice = "voice/bai/bai_0016.ogg"
            voice "voice/bai/bai_0016.ogg"
            $ vn2_face("bai", "sad")
            bai "今天别再抬重物。"
            nar "他指腹顺着上臂按过去，按到发紧的地方停了一下。你肩背绷着，他松手时拍了拍你上臂。他小腿上的口子还淌着血，先把你的胳膊和手处理完，扣好药箱，才挪到石头另一边给自己包。收拾药箱的时候，他视线落到你左耳上，停了一下。"
            $ vn2_current_voice = "voice/bai/bai_0017.ogg"
            voice "voice/bai/bai_0017.ogg"
            $ vn2_face("bai", "surprised")
            bai "你这只耳朵，缺过一角。旧伤，不长新肉了。"
            nar "你自己没提过。那道旧边在左耳外缘，毛长得长，平时挡得住。他拿指腹在自己耳边比了个位置，没伸手碰。崖边风大，蓝羽在放哨，青岩在开箱验样，都看得见这边。他把药布边角掖好，合上箱扣，没再多问。"
            think "他先处理我，再处理自己。手上的布一圈是一圈，旧处他也看见了。"

        "清点青岩的样本箱有没有碰湿":
            $ vn2_aff_add("qing", 3)
            $ vn2_show("qing", expr="happy", pos="right")
            nar "青岩开箱验样，一格一格翻，你把箱角的泥擦掉，递回去。"
            $ vn2_current_voice = "voice/qing/qing_0009.ogg"
            voice "voice/qing/qing_0009.ogg"
            $ vn2_face("qing", "happy")
            qing "没湿。这一趟，值。"
            nar "他把分格一格对过去，湿的贴箱壁，干的居中。本子摊在箱面上，他把崖况补了两行。"

        "把崖顶干处的碎石清开":
            nar "你蹲到岩台边上，把松动的碎石捡到干处堆好，留出能坐下四个人的地方。青岩把样本箱挪到清出来的干处。"
            $ vn2_show("qing", expr="neutral", pos="right")
            $ vn2_current_voice = "voice/qing/qing_0010.ogg"
            voice "voice/qing/qing_0010.ogg"
            $ vn2_face("qing", "neutral")
            qing "干处留出来，箱子才放得稳。"

    $ vn2_hide_all(trans=dissolve_soft)

    # --- 节点 5/9 · 绳归谁收（menu） ---
    nar "绳从坡面收回来，盘在岩台边上，绳股上的泥还没干。四个人围着绳站定，谁都没先伸手。绳上的泥在岩台上滴出几个湿点。谁先伸手，谁就把后面收绳的活揽过去。"

    menu:
        "把收绳的活揽到自己这边":
            $ vn2_aff_add("lan", 3)
            $ vn2_show("lan", expr="neutral", pos="left")
            nar "蓝羽过来接绳，见你没撒手，就退到崖边放哨。"
            $ vn2_current_voice = "voice/lan/lan_0015.ogg"
            voice "voice/lan/lan_0015.ogg"
            $ vn2_face("lan", "neutral")
            lan "你压过一次锚。这绳你收，我不抢。"
            nar "他退到崖边，砍刀换到外侧，视线沿着坡面扫过去。绳留在你手里，盘心对着自己，绳头压在最上面。"

        "问蓝羽，地图上这段断在哪":
            $ vn2_aff_add("lan", 3)
            $ vn2_show("lan", expr="sad", pos="center")
            nar "蓝羽把地图抖开，指腹在塌方这一段来回抹。"
            $ vn2_current_voice = "voice/lan/lan_0016.ogg"
            voice "voice/lan/lan_0016.ogg"
            $ vn2_face("lan", "sad")
            lan "这里原本有路。图上擦掉了，坡也是后来塌的。"
            nar "图上这一段空白，边沿被水泡得发虚。他拿铅笔在空白边缘点了两个小点，没把中间连上。"
            $ vn2_current_voice = "voice/lan/lan_0017.ogg"
            voice "voice/lan/lan_0017.ogg"
            $ vn2_face("lan", "neutral")
            lan "擦掉的路，图上补不回来。人记住走向就行。"

        "检查矿灯和火绒还够不够":
            $ vn2_show("lan", expr="neutral", pos="left")
            nar "你把矿灯拧亮一格，罩上的水汽擦了擦，灯光稳住。火绒剩半包，潮的那团挑出来，干的压回袋里。"
            $ vn2_current_voice = "voice/lan/lan_0018.ogg"
            voice "voice/lan/lan_0018.ogg"
            $ vn2_face("lan", "neutral")
            lan "黑里走夜路，灯不能先灭。"
            nar "你把矿灯挂回包侧，火绒袋扎紧。蓝羽扫了一眼灯的位置，点了点头。"

    # --- 节点 6/9 · 雨里清点 ---
    nar "歇脚的工夫，四个人把各自的东西摊在干处清点。绳一盘，药箱一摊，样本箱一格，压缩粮按份分开。白砚把用过的药布条收进袋里。青岩把崖况念了一遍，合上本子。蓝羽站在崖边放哨，每隔一会儿回头看一眼岩台上的人。"
    think "绳收了，药点了，样本验过了。下一段路从崖顶绕下去，不能再压这条胳膊。"

    # --- 节点 7/9 · 左臂 ---
    nar "断崖之后，你的左胳膊再没抬过肩。你没跟任何人提过疼。胳膊垂在身侧，走路时跟着步子晃。你把需要抬手的活换到右手，绳也绕在右腕上。白砚看在眼里，没催你说。经过窄处时，他伸手替你把左侧的枝拨开一点。"
    $ vn2_unlock_cg("cg_zhou")

    # --- 节点 8/9 · 雾压下来 ---
    nar "雨小下去，雾从坡底漫上来，先没过崖脚的碎石，再爬到岩台边。四个人靠得更近，包收起来，箱扣按紧。雾里看不见坡底，只听见水顺着石缝往下淌。"
    think "胳膊的事，进站之前不能再加重。剩下的路，稳着走。"

    # --- 节点 9/9 · 下山 ---
    nar "离开岩台，路顺着崖腰往另一侧绕。坡上有前人踩出的浅窝，一个接一个。你走在第二位，右手扶着坡边的湿藤。蓝羽在前探路，白砚压在中，青岩殿后。断崖留在身后。白生生的石头被雾盖住一半，再过一会儿，连那道削平的坡面也看不清楚了。"

    $ vn2_hide_all(trans=dissolve_soft)
    $ vn2_leave_chapter()
