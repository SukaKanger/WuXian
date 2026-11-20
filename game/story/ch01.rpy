# 第 1 章 • 雨停之后（第 1 天 / 共同线）
# 节点：1 营火余烬 · 2 出发前清点（menu）· 3 拔营前的分工（menu）· 4 天光入林
#       · 5 队形（menu）· 6 第一里路 · 7 雾起 · 8 上路
#
# 表情规则：每个角色开口前都有一句 $ vn2_face("角色", "表情")，
# 显式钉死这一句的脸；vn2_face 只换脸不动位置/明暗，不会重播动画。

label ch01:
    $ vn2_unlock_cg("cg_camp_fire_v1")

    # 冷开场：无线电
    scene black with slow_fade
    $ vn2_amb("fire")
    nar "无线电在凌晨四点自己响了。杂音，风声，然后半句话：“别进来。”你等了一会儿，后面再没声音。"
    think "旧站早就没声了。"

    scene bg firelight with slow_fade
    $ vn2_enter_chapter("ch01")
    call vn2_title_card(1, "雨停之后", "第 1 天 • 共同线")

    nar "雨停的时候你醒了一次，没看表，先摸外套。外套还在滴水，火也快灭了。白砚半夜把火压得太死，你拿树枝扒了两下，才见到底下的红。地图从内袋掏出来，纸边已经发软，字还在，旧站那块空白也还在。四个人，四个包，你数了一遍，又数了一遍。"

    $ vn2_show("lan", expr="neutral", pos="left", trans=dissolve_soft)
    $ vn2_cg_show("images/cg/cg_camp_fire_v1.png", trans=dissolve_soft)

    $ vn2_current_voice = "voice/lan/lan_0001.ogg"
    voice "voice/lan/lan_0001.ogg"
    $ vn2_face("lan", "neutral")
    lan "前面三里有个旧栈道。地图上标着，但没人走过。"
    zhou "没人走过，不等于过不去。"
    nar "蓝羽没接话，只把地图折成很小一块，露在手心里的部分还没巴掌大。折角被水泡开，线有点发虚；他用指腹抹了一下，没能抹平。"

    $ vn2_hide("lan", trans=dissolve_soft)
    $ vn2_show("bai", expr="sad", pos="center", trans=dissolve_soft)

    $ vn2_current_voice = "voice/bai/bai_0001.ogg"
    voice "voice/bai/bai_0001.ogg"
    $ vn2_face("bai", "sad")
    bai "你的肩膀昨天就裂了。别撑。"
    zhou "……撑得住。"
    nar "白砚把药布扔到你腿上，没抬头。药箱搁在脚边，箱扣上挂着半卷备用的药布。他挨个按了按瓶罐，把没归位的推回格子。"

    $ vn2_hide("bai", trans=dissolve_soft)
    $ vn2_show("qing", expr="neutral", pos="center", trans=dissolve_soft)

    $ vn2_current_voice = "voice/qing/qing_0001.ogg"
    voice "voice/qing/qing_0001.ogg"
    $ vn2_face("qing", "neutral")
    qing "那就走。天一亮，雾散不散，看命。"
    nar "青岩没起身，蹲在火边把样本箱的绳子重绕了一遍。绕到一半他停了手，等你扶住箱角。火苗塌下去，谁都没先动。"

    think "出发前还有一点时间。先做什么？"

    # --- 节点 2/8 · 出发前清点（menu） ---
    menu:
        "跟蓝羽核对地图":
            $ vn2_aff_add("lan", 4)
            $ vn2_hide_all(trans=dissolve_soft)
            $ vn2_show("lan", expr="surprised", pos="center")
            nar "蓝羽把地图摊在膝盖上，指尖压着那个被水泡开的角。"
            $ vn2_current_voice = "voice/lan/lan_0002.ogg"
            voice "voice/lan/lan_0002.ogg"
            $ vn2_face("lan", "surprised")
            lan "这条线，不是我画的。"
            nar "他说得很轻，怕被林子听见。"
            $ vn2_current_voice = "voice/lan/lan_0003.ogg"
            voice "voice/lan/lan_0003.ogg"
            $ vn2_face("lan", "sad")
            lan "先记着。别追着问。"
            nar "地图边角起毛，折痕一道压一道。他顺着折痕抹平，没去碰那道发虚的线。线的尽头是一块空白——旧站原本该在的位置。"
            think "不是他画的。那这条线是谁补上去的？"

        "找白砚换药布":
            $ vn2_aff_add("bai", 4)
            $ vn2_hide_all(trans=dissolve_soft)
            $ vn2_show("bai", expr="neutral", pos="center")
            nar "白砚把药布在火上烤了烤，才缠到你手背上。"
            $ vn2_current_voice = "voice/bai/bai_0002.ogg"
            voice "voice/bai/bai_0002.ogg"
            $ vn2_face("bai", "neutral")
            bai "烫就说。"
            $ vn2_current_voice = "voice/bai/bai_0003.ogg"
            voice "voice/bai/bai_0003.ogg"
            $ vn2_face("bai", "angry")
            bai "你们一个个都当我这儿是修东西的。"
            nar "他手指压着药布绕了两圈，边角掖进布层，顺手把腕上松了的一截缠紧。他没抬头，把空出来的药布条咬在齿间，腾出手去按箱扣。"

        "问青岩，雾什么时候散":
            $ vn2_aff_add("qing", 4)
            $ vn2_hide_all(trans=dissolve_soft)
            $ vn2_show("qing", expr="neutral", pos="center")
            nar "青岩蹲在营地边缘，尾巴扫开一层落叶。"
            $ vn2_current_voice = "voice/qing/qing_0002.ogg"
            voice "voice/qing/qing_0002.ogg"
            $ vn2_face("qing", "neutral")
            qing "雾不看时辰。它想散就散。"
            nar "他停了一下，回头看你。"
            $ vn2_current_voice = "voice/qing/qing_0003.ogg"
            voice "voice/qing/qing_0003.ogg"
            $ vn2_face("qing", "happy")
            qing "不过今天会散。我闻得出来。"
            nar "他抬手往林子低处指了指。雾正顺着沟底往坡上漫，贴地。"
            think "闻得出来。这条路他走过多少回，才敢说这话。"

    $ vn2_hide_all(trans=dissolve_soft)

    # --- 节点 3/8 · 拔营前的分工（menu） ---
    nar "清点完装备，离拔营还有一刻。火又矮下去一截，炭红贴地，谁都没先起身。"

    menu:
        "把四份干粮按人分好，摆到各人手边":
            # 节点 3 分支 · 白砚偏心甜点（软份压你那份底下，硬份自己留）
            $ vn2_aff_add("bai", 2)
            nar "你把干粮袋解开，两份压缩粮各掰成两半，一份一份搁在各人包上。四份里两块发硬，两块在火边烤软。白砚把软的那块压到你那份底下，另一块推给蓝羽；硬的两块，他一块留给自己，一块给青岩。你那份拿起来还带着温气。他没看你，先低头掰自己那块硬的。"
            think "四份。四个人。软的那块压在底下，路上少一份，就知道是谁的。"

        "把守夜的班次先排出来":
            $ vn2_flag("trust_team")
            nar "你拿树枝在灰上划班次：四个时辰，两个人轮。"
            $ vn2_show("lan", expr="neutral", pos="center")
            $ vn2_current_voice = "voice/lan/lan_0004.ogg"
            voice "voice/lan/lan_0004.ogg"
            $ vn2_face("lan", "neutral")
            lan "前半夜雾重。你先睡，我守头一班。"
            nar "白砚把药箱挪到靠火的位置，说后半夜换他。青岩点头，把轮班次序记在本子上。"

        "把各人的背包扣和鞋带再查一遍":
            nar "你绕着营地走了一圈，把松了的背包扣按紧，鞋带散的重新系成死结。青岩把样本箱的捆绳重绕，绕到一半停手，等你伸手帮他扶着箱角。"
            $ vn2_show("qing", expr="happy", pos="center")
            $ vn2_current_voice = "voice/qing/qing_0004.ogg"
            voice "voice/qing/qing_0004.ogg"
            $ vn2_face("qing", "happy")
            qing "箱角磕过一回。这回不歪了。"
            nar "一圈查完，装备都在该在的位置。"

    $ vn2_hide_all(trans=dissolve_soft)
    scene bg forest with slow_fade
    $ vn2_amb("forest")

    # --- 节点 4/8 · 天光入林 ---
    nar "天光从树冠的缝里漏下来，落在湿泥上。四个人在布边站定，包背好，绳盘在腰上。"

    $ vn2_show("lan", expr="neutral", pos="left", trans=dissolve_soft)
    $ vn2_show("bai", expr="neutral", pos="right", trans=dissolve_soft)

    nar "林子还在滴水，鞋底踩进泥里，拔出来时发出很轻的吸声。"
    zhou "三里。谁掉队谁自己喊。"
    nar "走出半里，蓝羽忽然停住。路边一棵倒木上有一道旧刻痕，像箭头，指着栈道方向。刻痕比这季的雨还老。"
    think "这条路上，早有人走过。"

    # --- 节点 5/8 · 队形（menu） ---
    menu:
        "跟蓝羽并排，盯着地图":
            $ vn2_aff_add("lan", 3)
            nar "蓝羽把地图折成很小一块，只露出手心那么大。"
            $ vn2_current_voice = "voice/lan/lan_0005.ogg"
            voice "voice/lan/lan_0005.ogg"
            $ vn2_face("lan", "surprised")
            lan "看见那条断线没有？断在这儿，可栈道不该断。"
            nar "他走在你左后半步，折起的图角从指缝里露出一点白。路窄的地方他收着肩。你顺着他指尖的方向看过去，林子层层，看不出断线从哪儿起。"

        "留在队尾，替白砚托药箱":
            $ vn2_aff_add("bai", 3)
            nar "白砚走得不快，药箱在背上一下一下磕着。你伸手托了一把。他没道谢，只把步子放慢半拍。药箱底贴着他后腰。你手掌垫在箱角和背之间，把颠劲卸掉一点。"

        "把青岩的样本箱揽到自己这边":
            $ vn2_aff_add("qing", 3)
            $ vn2_hide("bai")
            $ vn2_show("qing", expr="neutral", pos="right")
            nar "青岩把样本箱换了个肩，你接过去，压在自己这侧。"
            $ vn2_current_voice = "voice/qing/qing_0005.ogg"
            voice "voice/qing/qing_0005.ogg"
            $ vn2_face("qing", "happy")
            qing "箱角别磕石头。里面的东西比我娇气。"
            nar "箱子比看着沉，分格在里面顶着，走路时不能晃。他跟在你斜后方，手一直扶着箱底。"

    # --- 节点 6/8 · 第一里路 ---
    nar "第一里路，鞋底陷进泥里。拔出来时带出一股腐叶的甜味。蓝羽走在第二位，眼睛不断在地图和路之间来回；白砚压着药箱；青岩在最后，每隔一段停下来看土层。谁都没多说话。喘气声、脚步声、水滴声叠在一起，把林子填得很满。"

    # --- 节点 7/8 · 雾起 ---
    nar "走到半里多，低处的雾又漫上来，先没过鞋帮，再漫到膝盖。前面人的背影隔十步只剩轮廓。蓝羽抬手比了个收拢的手势。白砚把药箱抱在怀里，青岩把样本箱扣按了一遍。蓝羽把绳头分在两个人腰上。绳子连着，谁走远了都能觉出来。"
    think "雾一重，人就容易散。今晚之前，不能再拉开距离。"

    # --- 节点 8/8 · 上路 ---
    nar "天光掀开树冠时，第一里路走完了。前面的地势抬起来，泥里混进碎石，鞋底有了硬实的声响。三里旧栈道就在前面。地图上那块被水泡开的角，终于要对上了。可栈道入口的木板底下，传来一声空响——不像木头，像铁。"
    think "盖在桥上的东西。"

    $ vn2_hide_all(trans=dissolve_soft)
    $ vn2_leave_chapter()
