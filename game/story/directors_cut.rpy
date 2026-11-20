# ============================================================
#  1.28.22 • 中段导演剪辑版（ch05–ch14）
#  ------------------------------------------------------------
#  为什么存在：
#    玩家反馈第 4–12 章“一直在赶路、三选一、扎营、再选一次”，
#    信息密度低，微选项没有后果。这里把 ch05–ch13 重排成
#    “一章一个冲突、一章一个真正有后果的选择”，保留原有
#    章节 label、CG id、语音文件与状态变量。
#
#  兼容：
#    旧脚本原样保留。新档 / 老档在章节开头读到 vn2_story_mode
#    == "cut" 时进入这里；老档如果正停在某一章中间，仍按旧脚本
#    继续，不会因为 AST 变化直接坏档。下一章开头自动切到剪辑版。
#    ch14 的旧库存清点段落也只在新档跳过，旧档停在原地仍可继续。
# ============================================================

init offset = 1


# ------------------------------------------------------------
#  ch05 · 绳结
#  原章 3 个 menu；剪辑版只保留“怎么练”一个，后果直接写进
#  后面的行军细节，不再用“干处让给谁 / 练熟与旧话”凑长度。
# ------------------------------------------------------------
label ch05_cut:

    scene bg forest with slow_fade
    $ vn2_amb("forest")
    $ vn2_show("lan", pos="left", trans=dissolve_soft)

    nar "第五天，雨停了一阵。你的左臂还吊在布带里。左肩是旧伤，右手背是前天在桥上裂的口子，两处都没长好，缠布的时候容易混。蓝羽把一段旧绳摊在两人中间。绳身磨得发亮，股间夹着洗不掉的泥。他先用左手绕了一个死结，再把绳头递给你。"
    $ vn2_current_voice = "voice/lan/lan_0031.ogg"
    voice "voice/lan/lan_0031.ogg"
    lan "这种结，越拉越紧。松不了。"
    nar "你用右手试了一遍，结歪了。第二遍，绳头从指缝里滑出去。第三遍，蓝羽伸手按住绳尾。"
    $ vn2_current_voice = "voice/lan/lan_0032.ogg"
    voice "voice/lan/lan_0032.ogg"
    lan "别跟手较劲。让绳自己咬住。"

    menu:
        "这一下午，你把绳练成什么样？"

        "拆了重打，练到结自己立住":
            $ vn2_aff_add("lan", 4)
            $ vn2_current_voice = "voice/lan/lan_0033.ogg"
            voice "voice/lan/lan_0033.ogg"
            lan "成了。记住这个手感，别记住我的话。"
            nar "你打了七遍，掌心磨出一道红。蓝羽没再伸手，等你把最后一个结收口。"

        "跟白砚学活扣，先顾这条伤臂":
            $ vn2_aff_add("bai", 4)
            $ vn2_show("bai", pos="right", trans=dissolve_soft)
            $ vn2_current_voice = "voice/bai/bai_0024.ogg"
            voice "voice/bai/bai_0024.ogg"
            bai "死结绑东西，活扣救人。你这条胳膊，先学救人的。"
            nar "白砚把绳在桌沿上绕了一圈，手把手带你把活扣拉开。绳尾从结里抽出去时，发出很轻的一声。"

        "看青岩怎么捆样本箱":
            $ vn2_aff_add("qing", 3)
            $ vn2_show("qing", pos="right", trans=dissolve_soft)
            $ vn2_current_voice = "voice/qing/qing_0014.ogg"
            voice "voice/qing/qing_0014.ogg"
            qing "箱子角要留空。绳压住角，摔一次就断。"
            nar "青岩蹲下去，把绳从箱底穿过，留出两指宽的余量。你照着他的手序打了一遍，结不漂亮，但稳。"

    nar "你把两段绳分别绕在腰上。走起来的时候，绳头敲着胯骨，走几步蹭一下。"

    $ vn2_hide_all(trans=dissolve_soft)
    $ vn2_leave_chapter()
    return


# ------------------------------------------------------------
#  ch06 · 雨幕
#  只保留两个选择：先往哪边动、火圈外怎么对白砚。
#  合流之后不再反复点名、分粮、排守夜。
# ------------------------------------------------------------
label ch06_cut:

    scene bg forest with slow_fade
    $ vn2_amb("rain")
    $ vn2_show("lan", pos="left", trans=dissolve_soft)
    $ vn2_show("bai", pos="right", trans=dissolve_soft)
    $ vn2_show("qing", pos="center", trans=dissolve_soft)

    nar "第六天午后，雨忽然大了。林子里的声音被它吃掉一半，前队踩出的脚印走到坡腰就断了。你回头，只看见蓝羽的斗笠在树后一闪。白砚和青岩都不在原来的位置。"
    $ vn2_current_voice = "voice/lan/lan_0038.ogg"
    voice "voice/lan/lan_0038.ogg"
    lan "别喊。雨里喊，声音传不远，还会盖住哨。"
    nar "坡下有三条岔沟。水已经开始漫上来，泥浆贴着鞋底往上翻。"

    menu:
        "先往哪边动？"

        "吹哨，定一个合流点":
            $ vn2_flag("trust_team", True)
            $ vn2_aff_add("lan", 3)
            $ vn2_current_voice = "voice/lan/lan_0039.ogg"
            voice "voice/lan/lan_0039.ogg"
            lan "两声短，一声长。都听得见。"
            nar "哨音穿过雨幕。半坡上先冒出一顶斗笠，接着是青岩的箱角，最后是白砚的药箱扣。"

        "沿路留绳记号，回头找":
            $ vn2_aff_add("bai", 3)
            $ vn2_current_voice = "voice/bai/bai_0028.ogg"
            voice "voice/bai/bai_0028.ogg"
            bai "绳头系在能看见的地方。人走散，绳还在。"
            nar "你把活扣系在第三棵歪杉的低枝上。白砚顺着绳头找过来时，药箱上全是泥，手却先摸你的腕。"

        "先占高处，看脚印往哪边汇":
            $ vn2_aff_add("qing", 3)
            $ vn2_current_voice = "voice/qing/qing_0016.ogg"
            voice "voice/qing/qing_0016.ogg"
            qing "水往低处走，人往高处走。先看，再动。"
            nar "你爬上坡顶，看见两串脚印在沟底并成一条。青岩扛着箱子上来时，肩带在雨里绷得笔直。"

    nar "人齐了。四个人都湿透了。避雨处是一块凸出来的岩檐。火生不起来，只有一盏矿灯搁在石头中间。白砚坐在火圈外半步，药箱摊开，右手压在左腕上。他没有喊你。那只手在抖。"

    menu:
        "火圈外那个人，你怎么处理？"

        "坐过去，替他把药箱按住":
            $ vn2_aff_add("bai", 4)
            $ vn2_current_voice = "voice/bai/bai_0030.ogg"
            voice "voice/bai/bai_0030.ogg"
            bai "不用按。你坐这儿就行。"
            nar "你坐过去，肩挨着肩。白砚的手抖了一会儿，慢慢停了。他没有挪开。"

        "先把守夜排好，再去看他":
            $ vn2_aff_add("lan", 3)
            $ vn2_current_voice = "voice/lan/lan_0040.ogg"
            voice "voice/lan/lan_0040.ogg"
            lan "前半夜我，后半夜青岩。白砚的手不能冻。"
            nar "你把班次记在纸上。白砚抬头看了你一下，又低下去，自己把药箱扣上了。"

        "当众问他手怎么样，把话说开":
            $ vn2_aff_add("qing", 2)
            $ vn2_aff_add("bai", 2)
            $ vn2_current_voice = "voice/bai/bai_0031.ogg"
            voice "voice/bai/bai_0031.ogg"
            bai "老毛病。死不了，也快不了。"
            nar "他没有回避，也没有把手伸出来。青岩把矿灯往他那边推了推，光落在药箱扣上。"

    nar "火圈里四个位置，空着一个。雨打在岩檐上，一声接一声。"

    $ vn2_hide_all(trans=dissolve_soft)
    $ vn2_leave_chapter()
    return


# ------------------------------------------------------------
#  ch07 · 第一块站牌
#  原章 4 个 menu；剪辑版只保留“站牌底下怎么处理”，
#  把“怎么接话 / 分粮”改成选择后的余波。
# ------------------------------------------------------------
label ch07_cut:

    scene bg gate with slow_fade
    $ vn2_amb("forest")
    $ vn2_show("lan", pos="left", trans=dissolve_soft)
    $ vn2_show("qing", pos="right", trans=dissolve_soft)

    nar "第七天，路边立起一块锈牌。牌面被雨洗得发白，只剩一个编号和半截箭头。蓝羽把地图摊在牌下，指尖沿着一条断线走。断线到这里就没了，断口是刮出来的。"
    $ vn2_current_voice = "voice/lan/lan_0041.ogg"
    voice "voice/lan/lan_0041.ogg"
    lan "这块牌子该在的位置，图上没有。"
    nar "青岩蹲下去，用刀背敲了敲牌脚。下面是空的，声音发闷。土里埋着东西。"

    menu:
        "站牌底下这点东西，怎么处理？"

        "起开铁皮，把里面的残片取出来":
            $ vn2_aff_add("lan", 2)
            $ vn2_flag("lan_map_fixed", True)
            $ vn2_current_voice = "voice/lan/lan_0042.ogg"
            voice "voice/lan/lan_0042.ogg"
            lan "这不是断线。是有人把整段路从图上折进去了。"
            nar "残片只有指甲盖大，边缘带着旧铆钉孔。蓝羽把它按在图上，断线正好接上。"

        "不拆，先把编号和刻痕拓下来":
            $ vn2_aff_add("qing", 2)
            $ vn2_current_voice = "voice/qing/qing_0020.ogg"
            voice "voice/qing/qing_0020.ogg"
            qing "牌子会烂，纸不会。先抄，再走。"
            nar "你把纸按在牌面，用炭条轻轻擦。编号从锈里浮出来，后面还跟着两个被刮掉的字。"

        "原样不动，记下位置就走":
            $ vn2_aff_add("bai", 2)
            $ vn2_current_voice = "voice/bai/bai_0033.ogg"
            voice "voice/bai/bai_0033.ogg"
            bai "有些东西留在这儿，比带走有用。"
            nar "你把站牌的位置记在地图边角。蓝羽看了你一会儿，没再伸手去拆。"

    nar "你们在牌下歇了半刻。白砚把药布裁成窄条，一圈圈缠在你手腕上。"
    $ vn2_current_voice = "voice/bai/bai_0035.ogg"
    voice "voice/bai/bai_0035.ogg"
    bai "绳别勒在这道印上。换个位置。"
    nar "他没问你在牌下看见了什么，你也没说。风从箭头指的方向吹过来，带着一股铁锈味。白砚把药布收尾，压平，剩下的塞进药箱侧袋。"

    $ vn2_hide_all(trans=dissolve_soft)
    $ vn2_leave_chapter()
    return


# ------------------------------------------------------------
#  ch08 · 沼泽边
#  保留救阿瑞与深水让路两个选择；救完以后让阿瑞把
#  “我不跟你们走”说清楚，避免玩家以为她有隐藏路线。
# ------------------------------------------------------------
label ch08_cut:

    scene bg marsh with slow_fade
    $ vn2_amb("rain")
    $ vn2_show("lan", pos="left", trans=dissolve_soft)
    $ vn2_show("bai", pos="right", trans=dissolve_soft)
    $ vn2_show("qing", pos="center", trans=dissolve_soft)

    nar "第八天，沼泽涨水。浑水漫过膝弯，芦苇只剩穗尖露在外面。水洼中央有一团红毛在动。是阿瑞。她半个身子陷在泥里，一只手举着断绳，另一只手死死抓着芦苇根。"
    $ vn2_current_voice = "voice/ari/ari_0001.ogg"
    voice "voice/ari/ari_0001.ogg"
    arui "别从正面来！左边有暗沟，踩实底！"
    nar "蓝羽把绳甩过去，白砚按住药箱，青岩把箱带解下来当牵引。水还在涨。"

    menu:
        "水里的人，救不救？"

        "蹚过去，从左边实底拉她":
            $ vn2_flag("ari_helped", True)
            $ vn2_aff_add("ari", 3)
            $ vn2_current_voice = "voice/ari/ari_0002.ogg"
            voice "voice/ari/ari_0002.ogg"
            arui "你踩的那块会塌！再偏半步，往苇根上踩！"
            nar "你一脚踩进泥里，水没到大腿。阿瑞的手抓住你的腕，指甲隔着湿毛掐进皮里。蓝羽在岸上收绳，把两个人一起拖了回去。"

        "不冒险，先架绳桥让她自己爬":
            $ vn2_aff_add("lan", 2)
            $ vn2_current_voice = "voice/lan/lan_0046.ogg"
            voice "voice/lan/lan_0046.ogg"
            lan "绳桥比人稳。她自己能过来。"
            nar "三股绳在两岸拉直，阿瑞把断绳挂上去，慢慢挪。她上岸时，红毛上全是泥，眼睛却先看向你。"

        "绕开，水太深，不能把全队搭进去":
            nar "你抬手，示意队伍往高处绕。阿瑞在水里看着你们，没有喊第二声。走出十几步，身后传来芦苇折断的响。你没有回头。"

    if ari_helped:
        nar "阿瑞坐在岸边吐了两口水，把断绳重新接上。她指着芦苇深处的一条浅线。"
        $ vn2_current_voice = "voice/ari/ari_0003.ogg"
        voice "voice/ari/ari_0003.ogg"
        arui "顺着这条线走，水到不了腰。别踩发黑的地方。"
        nar "她说完，把绳头塞回你手里，自己往另一片芦苇走去。"
        $ vn2_current_voice = "voice/ari/ari_0004.ogg"
        voice "voice/ari/ari_0004.ogg"
        arui "我不跟你们走。我有自己的线，也有自己的账。"
        nar "她走得很快，红毛在雨里晃了两下，就被芦苇吞了。"
    else:
        nar "阿瑞自己从下游浅滩上了岸，隔着水看了你们一眼，转身进了芦苇。她没有留下指路的线。"

    nar "最后一段深水前，三个人都停下来。水面下有一条暗沟，一次只能扶一个人过去。"
    $ vn2_current_voice = "voice/bai/bai_0036.ogg"
    voice "voice/bai/bai_0036.ogg"
    bai "你决定。别让三个人一起踩空。"

    menu:
        "过最后一段深水，先顾谁？"

        "蓝羽：他走在最前面，先把他踩实的路稳住":
            $ vn2_aff_add("lan", 4)
            $ vn2_current_voice = "voice/lan/lan_0047.ogg"
            voice "voice/lan/lan_0047.ogg"
            lan "我探。你跟着我的脚印，别踩旁边。"
            nar "蓝羽先下水，绳系在腰上。你跟在后面，每一步都踩在他刚踩过的位置。"

        "白砚：他手上有伤，药箱不能湿":
            $ vn2_aff_add("bai", 4)
            $ vn2_current_voice = "voice/bai/bai_0037.ogg"
            voice "voice/bai/bai_0037.ogg"
            bai "药箱举高。我手没事，别把布浸了。"
            nar "你接过药箱，举过肩。白砚空着手下水，走在最浅的那条线上，右手一直没抖。"

        "青岩：他扛着样本箱，先替他分重":
            $ vn2_aff_add("qing", 4)
            $ vn2_current_voice = "voice/qing/qing_0028.ogg"
            voice "voice/qing/qing_0028.ogg"
            qing "箱子给我一半。你放心，我脚比你稳。"
            nar "你和青岩一人抬一边，箱底贴着水面过去。他的肩在绳带下磨出一道红，没吭声。"

    nar "上岸后，白砚蹲下来检查每双脚。你的旧伤泡得发白，他用干布按了很久。"
    $ vn2_current_voice = "voice/qing/qing_0029.ogg"
    voice "voice/qing/qing_0029.ogg"
    qing "沼泽不记路，只记人。今天它记了我们四个。"
    nar "青岩把箱子往肩上颠了颠，先往前走。你跟上去，湿裤腿贴在腿上。"

    $ vn2_hide_all(trans=dissolve_soft)
    $ vn2_leave_chapter()
    return


# ------------------------------------------------------------
#  ch09 · 银纹
#  保留 CG 解锁；把天线选位、交什么、怎么守夜压成
#  一个“碰不碰”的选择和一段电台余波。
# ------------------------------------------------------------
label ch09_cut:

    scene bg firelight with slow_fade
    $ vn2_amb("fire")
    $ vn2_show("lan", pos="left", trans=dissolve_soft)

    nar "第九天夜里，火堆烧到第二层。蓝羽把湿袖口卷上去，小臂内侧露出一道银白的纹。纹路贴着血管走，末端分了三岔。火光一动，纹也跟着亮。"
    $ vn2_current_voice = "voice/lan/lan_0048.ogg"
    voice "voice/lan/lan_0048.ogg"
    lan "别碰。碰了会亮得更厉害。"
    nar "他说得太晚。你的指尖已经停在离纹路半寸的地方。"
    $ vn2_unlock_cg("cg_lan")

    menu:
        "这道银纹，你要怎么做？"

        "碰上去，看看它到底有多亮":
            $ vn2_aff_add("lan", 5)
            $ vn2_current_voice = "voice/lan/lan_0050.ogg"
            voice "voice/lan/lan_0050.ogg"
            lan "……你倒是不怕。"
            nar "银纹在你指下亮了一瞬。蓝羽的呼吸停了一拍，又慢慢放开。"

        "不碰，问他这纹是从哪来的":
            $ vn2_aff_add("lan", 4)
            $ vn2_current_voice = "voice/lan/lan_0051.ogg"
            voice "voice/lan/lan_0051.ogg"
            lan "上一支队伍留下的。人没了，纹还在。"
            nar "他说得很平，眼睛没有抬。火堆里一截柴断掉，火星往上飘。"

        "把袖子拉下来，替他遮住":
            $ vn2_aff_add("lan", 3)
            $ vn2_current_voice = "voice/lan/lan_0053.ogg"
            voice "voice/lan/lan_0053.ogg"
            lan "遮不遮都一样。夜里它自己会亮。"
            nar "你还是把袖口拉了下来。蓝羽低头看了一眼，没有推开你的手。"

    nar "后半夜，电台里忽然有了声音。先是一段杂音，接着是断断续续的数字，重复了三遍。青岩把频率记在纸上。蓝羽按住了他的手。"
    $ vn2_current_voice = "voice/lan/lan_0057.ogg"
    voice "voice/lan/lan_0057.ogg"
    lan "别回。回了，他们就知道我们还在。"
    nar "你听着那串数字，没有写。火塌下去一层，没有人说话。"

    $ vn2_hide_all(trans=dissolve_soft)
    $ vn2_leave_chapter()
    return


# ------------------------------------------------------------
#  ch10 · 改过的地图
#  只保留“这一笔怎么处理”。半片药与明天按哪张图走
#  改成选择后的直接后果，不再单独弹两个 menu。
# ------------------------------------------------------------
label ch10_cut:

    scene bg cliff with slow_fade
    $ vn2_amb("rain")
    $ vn2_show("lan", pos="left", trans=dissolve_soft)
    $ vn2_show("qing", pos="right", trans=dissolve_soft)

    nar "第十天，崖线滑脚。蓝羽走在前面，一脚踩空，绳在石棱上磨出火星。你把他拖回来时，地图从侧袋里滑出来，摊在泥水里。图上多了一指宽的新线，起点是旧站，终点被人用指甲刮掉了。"
    $ vn2_current_voice = "voice/lan/lan_0058.ogg"
    voice "voice/lan/lan_0058.ogg"
    lan "别看了。那条线不通。"
    nar "蓝羽说完就把脸转开。青岩把图捡起来，指腹沿着新线的边缘走了一遍。"
    $ vn2_current_voice = "voice/qing/qing_0033.ogg"
    voice "voice/qing/qing_0033.ogg"
    qing "墨是新的。画图的人知道我们走到哪。"

    menu:
        "这一笔，怎么处理？"

        "当面摊牌，把图推到火光下":
            $ vn2_flag("lan_map_fixed", True)
            $ vn2_aff_add("lan", 4)
            $ vn2_current_voice = "voice/lan/lan_0064.ogg"
            voice "voice/lan/lan_0064.ogg"
            lan "是我改的。旧线会把人带进塌方。我不想再带第二支队伍进去。"
            nar "他把整段旧线指给你看：三处断口，两个红叉。他的指甲从其中一个红叉上划过去。"

        "私下问他，不把图给第三个人看":
            $ vn2_aff_add("lan", 4)
            $ vn2_current_voice = "voice/lan/lan_0066.ogg"
            voice "voice/lan/lan_0066.ogg"
            lan "你信我一次。到了站前，我把整张图给你。"
            nar "你把图折起来，塞回自己的内袋。青岩看见了，没有问。"

        "装没看见，先把今晚过去":
            $ vn2_aff_add("qing", 4)
            $ vn2_current_voice = "voice/qing/qing_0035.ogg"
            voice "voice/qing/qing_0035.ogg"
            qing "你不问，我就当没看见。但明天走哪条，你得自己认。"
            nar "你把图摊在火边，没有折。蓝羽坐在对面，一直没伸手。"

    nar "后半夜，白砚把半片药掰成两半，放在你手心里。"
    $ vn2_current_voice = "voice/bai/bai_0041.ogg"
    voice "voice/bai/bai_0041.ogg"
    bai "你吃一半。剩下的一半，明天谁发烧谁吃。"
    nar "药片很小，你把它含在舌下，没有喝水。白砚把余下的那点包进纸里，压平，收进药箱。"

    $ vn2_hide_all(trans=dissolve_soft)
    $ vn2_leave_chapter()
    return


# ------------------------------------------------------------
#  ch11 · 第二座信标
#  两个选择：怎么回应信标、最后一响陪谁。
#  “陪蓝羽”写入 close_lan，是蓝羽同行结局的承诺。
# ------------------------------------------------------------
label ch11_cut:

    scene bg cliff with slow_fade
    $ vn2_amb("rain")
    $ vn2_show("lan", pos="left", trans=dissolve_soft)
    $ vn2_show("bai", pos="right", trans=dissolve_soft)
    $ vn2_show("qing", pos="center", trans=dissolve_soft)

    nar "第十一天，第二座信标立在崖脊上。铁架锈得发红，天线只剩半截，指示灯却还在闪。"
    $ vn2_current_voice = "voice/lan/lan_0071.ogg"
    voice "voice/lan/lan_0071.ogg"
    lan "它在等回应。有人把频段锁死了。"
    nar "青岩把电台接上，电流声里浮出一段旧呼号。白砚把药箱垫在脚下，防止潮气往上返。"

    menu:
        "信标怎么回应？"

        "回一段短信号，只报方位":
            $ vn2_aff_add("lan", 4)
            $ vn2_current_voice = "voice/lan/lan_0074.ogg"
            voice "voice/lan/lan_0074.ogg"
            lan "报方位，不报人数。让他们知道有人到过，不让他们知道我们还有几个。"
            nar "你按下发报键，只敲了三个短音。信标的指示灯换了节奏，快两下，慢一下。"

        "拆开外壳，看里面还剩下什么":
            $ vn2_aff_add("qing", 4)
            $ vn2_current_voice = "voice/qing/qing_0040.ogg"
            voice "voice/qing/qing_0040.ogg"
            qing "线没断，电还有一点。够它再亮一夜。"
            nar "外壳里全是锈水和虫壳。青岩用刀尖挑开接点，指示灯重新亮了一格。"

        "不回应，只把呼号记下来":
            $ vn2_aff_add("bai", 4)
            $ vn2_current_voice = "voice/bai/bai_0045.ogg"
            voice "voice/bai/bai_0045.ogg"
            bai "回了，就承认我们在这儿。记下来，比回话有用。"
            nar "你把呼号抄在纸角。信标还在闪，间隔越来越长。"

    nar "入夜前，电池只剩最后一格。信标还能再响一次，电台也能再发一次。只能选一样。蓝羽把发报键推到一边，自己坐到铁架下面。他抬头看那半截天线，看了很久。"
    $ vn2_current_voice = "voice/lan/lan_0075.ogg"
    voice "voice/lan/lan_0075.ogg"
    lan "最后一响，我想让它按旧频段走。"
    nar "白砚在收拾药箱，青岩在抄呼号。两个人都没有催你。"

    menu:
        "最后一响，你陪谁？"

        "陪蓝羽，听它按旧频段响完":
            $ vn2_aff_add("lan", 4)
            $ vn2_flag("close_lan", True)
            $ vn2_current_voice = "voice/lan/lan_0076.ogg"
            voice "voice/lan/lan_0076.ogg"
            lan "上一支队伍最后也停在这座塔下。我没等到他们回话。"
            nar "你在他旁边坐下。最后一响很短。蓝羽没有回头，肩膀往你这边靠了靠。"
            $ vn2_current_voice = "voice/lan/lan_0077.ogg"
            voice "voice/lan/lan_0077.ogg"
            lan "这次等到了。"
            nar "他把袖口卷起来，银纹在暗处亮了一下。你看见他小臂上那道旧疤，从纹路中间穿过去。"

        "陪青岩，把呼号抄完整":
            $ vn2_aff_add("qing", 4)
            $ vn2_current_voice = "voice/qing/qing_0041.ogg"
            voice "voice/qing/qing_0041.ogg"
            qing "旧频段最后一段是坐标。抄完，我们至少知道他们停在哪。"
            nar "你举着灯，青岩一笔一笔抄。最后一响落下来时，他的笔尖正好停在纸尾。他把纸折好，塞进样本箱底，没有解释。"

        "陪白砚，把最后一格电留给药箱":
            $ vn2_aff_add("bai", 4)
            $ vn2_current_voice = "voice/bai/bai_0048.ogg"
            voice "voice/bai/bai_0048.ogg"
            bai "最后一格电，够把药箱烘一夜。信标少响一次，不会死人。"
            nar "你把电池接到药箱的烘灯上。信标暗下去，药箱里有了暖意。白砚把手放在灯罩边，指尖不再抖。"

    nar "你们从崖脊往下走。蓝羽把地图换到内袋，青岩把样本箱换到另一边肩，白砚把药箱扣紧。"

    $ vn2_hide_all(trans=dissolve_soft)
    $ vn2_leave_chapter()
    return


# ------------------------------------------------------------
#  ch12 · 旧营地
#  只保留“杆子落下来”一个选择；接住杆子写入 saved_bai，
#  是白砚同行结局的承诺。
# ------------------------------------------------------------
label ch12_cut:

    scene bg forest with slow_fade
    $ vn2_amb("fire")
    $ vn2_show("bai", pos="center", trans=dissolve_soft, expr="sad")
    $ vn2_show("lan", pos="left", trans=dissolve_soft)

    nar "第十二天，旧营地藏在一片背风林里。帐篷布烂了半边，撑杆斜着，地上还留着上一支队伍的灰烬。白砚蹲下去翻药箱，右手刚搭上箱扣。头顶那根朽杆发出一声脆响，整片帐篷布往下塌。"
    $ vn2_current_voice = "voice/bai/bai_0049.ogg"
    voice "voice/bai/bai_0049.ogg"
    bai "别管我，先看箱子——"
    nar "杆子已经落下来了。白砚的右手还在箱扣上。"

    menu:
        "杆子落下来，你先做什么？"

        "伸手接住杆子，把重量扛到自己肩上":
            $ vn2_flag("saved_bai", True)
            $ vn2_aff_add("bai", 5)
            $ vn2_current_voice = "voice/bai/bai_0051.ogg"
            voice "voice/bai/bai_0051.ogg"
            bai "你疯了？这条胳膊还有旧伤！"
            nar "木头压上肩时，你听见自己骨头响了一声。白砚从箱边扑过来，先托住杆尾，再托住你的肘。杆子被抬开时，他的右手一直按在你肩上，没有松。"

        "先按住他的手腕，把右手从箱扣上挪开":
            $ vn2_aff_add("bai", 4)
            $ vn2_current_voice = "voice/bai/bai_0052.ogg"
            voice "voice/bai/bai_0052.ogg"
            bai "……松手。我没事。"
            nar "你把他往旁边带了一步。杆子砸在药箱边，箱角裂了一道，里面的药瓶没碎。白砚低头看见裂缝，脸色比刚才更难看。他把手腕从你手里抽出去，又停住。"

        "喊青岩，让他从另一侧顶住":
            $ vn2_aff_add("qing", 4)
            $ vn2_current_voice = "voice/qing/qing_0043.ogg"
            voice "voice/qing/qing_0043.ogg"
            qing "顶住了！把箱子拖出来！"
            nar "青岩用肩顶住杆子，你和白砚一起把药箱拖出去。箱底在泥里划过，发出一声长响。白砚的手没有受伤。他看了看青岩的肩，又看了看你，什么也没说。"

    if saved_bai:
        nar "白砚把杆子扔到一边，蹲下来检查你的肩。他的手指按在骨头上，按得很慢。"
        $ vn2_current_voice = "voice/bai/bai_0053.ogg"
        voice "voice/bai/bai_0053.ogg"
        bai "没断。但接下来三天，这只手不许抬东西。"
        nar "他说完，把药箱换到左手，右手垂在身侧，没有再藏。"
        $ vn2_current_voice = "voice/bai/bai_0054.ogg"
        voice "voice/bai/bai_0054.ogg"
        bai "你替我接了一次。我记住了。"
    else:
        nar "白砚把药箱扶正，检查裂缝。他没有看你，只把裂开的箱角用布条缠上。"
        $ vn2_current_voice = "voice/bai/bai_0055.ogg"
        voice "voice/bai/bai_0055.ogg"
        bai "还能用。走吧，这地方不能过夜。"

    nar "你们没有在旧营地留宿。走出背风林时，天还没黑。白砚没有再说“别撑”。"

    $ vn2_hide_all(trans=dissolve_soft)
    $ vn2_leave_chapter()
    return


# ------------------------------------------------------------
#  ch13 · 分岔
#  两个选择：走哪条路、夜里注意到什么。
#  章末把三个人的“交底状态”直接说破，让 ch14 不再是暗账。
# ------------------------------------------------------------
label ch13_cut:

    scene bg forest with slow_fade
    $ vn2_amb("forest")
    $ vn2_show("lan", pos="left", trans=dissolve_soft)
    $ vn2_show("bai", pos="center", trans=dissolve_soft)
    $ vn2_show("qing", pos="right", trans=dissolve_soft)

    nar "第十三天，林子分成两条路。一条沿水线绕远，一条翻脊直插旧站。翻脊少走两天。"
    $ vn2_current_voice = "voice/lan/lan_0081.ogg"
    voice "voice/lan/lan_0081.ogg"
    lan "水线我走过。慢，但不会把人丢在沟里。"
    $ vn2_current_voice = "voice/bai/bai_0058.ogg"
    voice "voice/bai/bai_0058.ogg"
    bai "翻脊快。他的胳膊撑不撑得住，你问他自己。"
    $ vn2_current_voice = "voice/qing/qing_0046.ogg"
    voice "voice/qing/qing_0046.ogg"
    qing "我只知道翻脊没有水。走哪条，你们定。"

    menu:
        "走哪条？"

        "跟蓝羽走水线：慢一点，但路是熟的":
            $ vn2_aff_add("lan", 4)
            $ vn2_current_voice = "voice/lan/lan_0083.ogg"
            voice "voice/lan/lan_0083.ogg"
            lan "跟紧。水线有三处塌方，我会先停。"
            nar "蓝羽走在最前面，每到一个弯就停下来等。你们多走了半天，但没有一个人踩空。"

        "听白砚走翻脊：快一点，伤号少受一天罪":
            $ vn2_aff_add("bai", 4)
            $ vn2_current_voice = "voice/bai/bai_0060.ogg"
            voice "voice/bai/bai_0060.ogg"
            bai "我走后面。谁掉队，我停下来。"
            nar "翻脊的路陡，白砚走在队尾，药箱在背上晃。你回头看了三次，他三次都抬手示意继续。"

        "按青岩说的，先到翻脊顶再决定":
            $ vn2_aff_add("qing", 4)
            $ vn2_current_voice = "voice/qing/qing_0047.ogg"
            voice "voice/qing/qing_0047.ogg"
            qing "到顶上能看见旧站。看见了，再选。"
            nar "你们爬到脊顶，旧站的轮廓在雾里露出一个角。青岩把箱子放下，第一次没有催着走。"

    scene bg firelight with slow_fade
    $ vn2_amb("fire")
    $ vn2_show("lan", pos="left", trans=dissolve_soft)
    $ vn2_show("bai", pos="center", trans=dissolve_soft)
    $ vn2_show("qing", pos="right", trans=dissolve_soft)

    nar "夜里扎在脊背的凹处。火不大，只够照亮四个人的膝盖。你把最后一块干肉掰成四份。青岩接过自己那份，没有先吃，先看了看白砚的手。"
    $ vn2_current_voice = "voice/qing/qing_0049.ogg"
    voice "voice/qing/qing_0049.ogg"
    qing "明天到岔口，路就定了。"
    nar "蓝羽在补地图，白砚在缠药布，青岩把样本箱的扣带重新调短。"

    menu:
        "夜里，你注意到什么？"

        "青岩把一页折过的纸塞回箱底":
            $ vn2_aff_add("qing", 4)
            $ vn2_flag("know_qing_secret", True)
            $ vn2_current_voice = "voice/qing/qing_0050.ogg"
            voice "voice/qing/qing_0050.ogg"
            qing "别问。到站里，你自己会看见。"
            nar "纸页上有三个被划掉的名字，最后一个还没划。青岩把箱盖扣上，手指在扣带上停了一会儿。"

        "白砚把右手藏在袖子里，用左手缠药布":
            $ vn2_aff_add("bai", 4)
            $ vn2_current_voice = "voice/bai/bai_0062.ogg"
            voice "voice/bai/bai_0062.ogg"
            bai "看什么。缠歪了，明天还得重来。"
            nar "你把药布接过去，替他压住布头。白砚没有躲，右手在袖子里慢慢松开。"

        "蓝羽把地图翻到背面，避开你的视线":
            $ vn2_aff_add("lan", 4)
            $ vn2_current_voice = "voice/lan/lan_0087.ogg"
            voice "voice/lan/lan_0087.ogg"
            lan "背面的线还没补完。补完了，我给你看。"
            nar "你把灯往他那边挪了挪。蓝羽没有再把图翻过去，背面的旧线在光下露出半截。"

    # ---- 章末：把三条线的“承诺”说破 ----
    nar "火堆里爆了一声，几粒火星落在石头外面。"
    if close_lan:
        nar "蓝羽把地图合上一半，折角朝你这边。信标下说过的那支队伍，他没有再避开。"
    else:
        nar "蓝羽把地图合上一半，折角朝他自己。你问一句，他答一句。"
    if saved_bai:
        nar "白砚把药布收进药箱，右手就搁在膝盖上，没有往袖子里收。"
    else:
        nar "白砚把药布收进药箱，右手缩回袖口，只露出两节指节。"
    if know_qing_secret:
        nar "青岩把样本箱侧放在脚边，箱底朝你。"
    else:
        nar "青岩把样本箱侧放在脚边，箱底朝外。"

    nar "炭火暗下去，没有人去添。"

    $ vn2_hide_all(trans=dissolve_soft)
    $ vn2_leave_chapter()
    return


# ------------------------------------------------------------
#  ch14 · 锁线（剪辑版开场）
#  ch14 原脚本保留，只在新档跳过冗长的库存清点。
#  这里把三个人的承诺状态直接摆到岔口上。
# ------------------------------------------------------------
label ch14_cut:

    scene bg marsh with slow_fade
    $ vn2_show("lan", pos="left", trans=dissolve_soft)
    $ vn2_show("bai", pos="center", trans=dissolve_soft)
    $ vn2_show("qing", pos="right", trans=dissolve_soft)

    nar "第十四天，雾压到最低。沼泽边分出四条路：水线、翻脊、密林、乱石。三个人站在岔口，等你先开口。雨不大，绵的，落在防水布上一声叠一声。"
    $ vn2_current_voice = "voice/lan/lan_0088.ogg"
    voice "voice/lan/lan_0088.ogg"
    lan "跟我走，我在前头认路。绳放我肩上，滑了有人拉。"
    $ vn2_current_voice = "voice/bai/bai_0065.ogg"
    voice "voice/bai/bai_0065.ogg"
    bai "能走的我管伤。走不动的，我先停下来等。"
    $ vn2_current_voice = "voice/qing/qing_0051.ogg"
    voice "voice/qing/qing_0051.ogg"
    qing "箱子不轻。要抬，得两个人抬。"

    nar "你没有指哪一条。"
    if close_lan:
        nar "蓝羽把绳圈往肩上送了送，绳头垂到你手边。"
    else:
        nar "蓝羽把绳圈往肩上送了送，绳头收在自己手里。"
    if saved_bai:
        nar "白砚把药箱放在脚边，箱扣没有扣上。"
    else:
        nar "白砚把药箱背回身上，右手插在袖子里，只用左手扶着箱带。"
    if know_qing_secret:
        nar "青岩把样本箱放在地上，手在箱底那一面按了一下。"
    else:
        nar "青岩把样本箱背回肩上，箱底贴着后背。"

    jump ch14_choice
