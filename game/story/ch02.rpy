# 第 2 章 • 三里旧栈道（第 2 天 / 共同线）
# 节点：1 栈道露头 · 2 板下的东西（menu）· 3 试板过栈 · 4 先看你的手（menu）
#       · 5 三里走完 · 6 路上记号（menu）· 7 板缝泥水 · 8 接上土路
#       · 9 栈道尽头扎营（menu · C 批营地容器）
#
# 表情规则：每句角色台词前用 $ vn2_face("角色", "表情") 显式指定。

label ch02:

    scene bg forest with slow_fade
    $ vn2_enter_chapter("ch02")
    call vn2_title_card(2, "三里旧栈道", "第 2 天 • 共同线")
    $ vn2_amb("forest")

    # --- 节点 1/8 · 栈道露头 ---
    $ vn2_show("bai", expr="sad", pos="left", trans=dissolve_soft)

    nar "栈道从泥里露出来。木板一块接一块，板面长着薄苔，一头扎进雾里。"
    nar "白砚拦在板前，指着你手背上昨天那道裂口。"
    $ vn2_current_voice = "voice/bai/bai_0004.ogg"
    voice "voice/bai/bai_0004.ogg"
    $ vn2_face("bai", "sad")
    bai "先缠好。踩上去手要抓边绳，裂口别再扯开。"

    nar "你把手背翻过来。药布边缘起毛，裂口发红，握拳时牵扯着紧。"
    nar "蓝羽说，过了这段栈道，能少绕一天路。"
    nar "你敲了敲木板。回声很短，短得不像空。"
    zhou "下面不是空的。是实的。"

    nar "木板贴着坡边铺过去，两边是斜下去的湿藤和倒木。板与板之间留着一指宽的缝，缝里塞着落叶和泥。你吸了一口气，烂木的酸味里混着铁锈。栈道口的腐叶被人踩成一摊黑泥，你站在板前，把鞋底在石头上蹭了蹭。"

    $ vn2_hide("bai", trans=dissolve_soft)
    $ vn2_show("lan", expr="surprised", pos="right", trans=dissolve_soft)

    $ vn2_current_voice = "voice/lan/lan_0006.ogg"
    voice "voice/lan/lan_0006.ogg"
    $ vn2_face("lan", "surprised")
    lan "地图上写这儿是桥。可这不像桥。"
    zhou "下面不是空的。是实的。"
    $ vn2_current_voice = "voice/lan/lan_0007.ogg"
    voice "voice/lan/lan_0007.ogg"
    $ vn2_face("lan", "surprised")
    lan "……那不叫桥。那叫盖在上面的东西。"

    nar "盖在铁上的木板是后来铺的。旧站的人不想让谁看见底下的东西。"
    think "是不想让人看见，还是不想让人进去？"

    nar "蓝羽蹲下去，把脸贴近板缝。缝里黑，只有潮气往上冒，带着锈和烂木混在一起的味。"
    nar "他按了按最近一块板，板面晃了晃，没塌。"
    think "木板底下有东西。掀不掀？"

    # --- 节点 2/8 · 板下的东西（menu） ---
    menu:
        "自己先过，一块一块试稳":
            $ vn2_aff_add("bai", 3)
            nar "你先上。木板在你脚下响了一声，没塌。"
            zhou "一个一个来。别跑。"
            nar "你数着人过去。最后一个，是你自己。"
            nar "后面三个人踩着你试过的板往前。你站在中段，把走过的板角按了按。"

        "停下来，跟蓝羽一起看那块板":
            $ vn2_aff_add("lan", 4)
            $ vn2_hide("lan")
            $ vn2_show("lan", expr="surprised", pos="center")
            nar "蓝羽把板角撬起一寸。底下是铁，锈得发红。"
            $ vn2_current_voice = "voice/lan/lan_0008.ogg"
            voice "voice/lan/lan_0008.ogg"
            $ vn2_face("lan", "surprised")
            lan "有人在这上面又盖了一层。"
            nar "他把板放回去，动作很轻，像怕惊动底下的东西。"
            nar "铁面和木板之间垫着朽木楔，一捏就碎。他用刀尖刮下一点锈，锈里混着旧泥。"
            $ vn2_current_voice = "voice/lan/lan_0009.ogg"
            voice "voice/lan/lan_0009.ogg"
            $ vn2_face("lan", "neutral")
            lan "钉子是铁的。这一带早先有人走过，走过不止一回。"

        "让白砚先摸木头的裂口":
            $ vn2_aff_add("bai", 4)
            $ vn2_hide("lan", trans=dissolve_soft)
            $ vn2_show("bai", expr="sad", pos="center")
            nar "白砚蹲下去，指腹压着裂纹。"
            $ vn2_current_voice = "voice/bai/bai_0005.ogg"
            voice "voice/bai/bai_0005.ogg"
            $ vn2_face("bai", "sad")
            bai "泡了太久。再下一场雨，就撑不住。"
            nar "他把手套摘了，用指甲刮下一层木屑，收进兜里。裂纹里渗着黑水，木头在指底下发软。他把手套重新戴上，指尖在裤缝上蹭了蹭。"
            $ vn2_current_voice = "voice/bai/bai_0006.ogg"
            voice "voice/bai/bai_0006.ogg"
            $ vn2_face("bai", "neutral")
            bai "这条板先记着。过的时候别在上面停。"

    $ vn2_hide_all(trans=dissolve_soft)

    # --- 节点 3/8 · 试板过栈 ---
    nar "四个人在栈板上站定。风从坡底卷上来，板缝里的泥水滴到下面的藤上，很久才听见落地的声。蓝羽把地图折小，压进胸口的口袋。白砚把药箱抱到身前，青岩把样本箱扣检查了两遍。你握住边绳试了试，绳股潮软，吃劲的地方还牢。"
    think "上了板，就没有回头挑路的余地。一块一块走过去。"

    # --- 节点 4/8 · 先看你的手（menu） ---
    nar "过了头一段板，队伍在一处稍宽的板面上停下歇脚。手背的药布被汗浸透，得趁这会儿重新缠一缠。"

    menu:
        "先让白砚把手伤重新缠好":
            # 节点 4 分支 · 白砚被照顾甜点（先缠你的手，再顾自己；余波为抓绳试握）
            $ vn2_aff_add("bai", 2)
            nar "你在干板上坐下，把手背朝自己翻过来。药布被汗浸得发软，裂口周围发红，握拳的时候牵扯着紧。"
            $ vn2_current_voice = "voice/bai/bai_0007.ogg"
            voice "voice/bai/bai_0007.ogg"
            $ vn2_face("bai", "neutral")
            bai "手伸过来。"
            nar "他在你面前蹲下来，先把旧药布解开。布粘在裂口边上，他一点一点揭，没扯。指腹落在昨天那道口子边上，没再重新找位置。新药布绕上去，一圈压一圈，绕到腕口，他的手按着不让你动，缠完才松开。"
            nar "他自己袖口蹭破了一道，小臂沾着木屑，一直没顾上。先把你的手缠好，扣好药箱，他才低头去看自己那道蹭破的边。"
            $ vn2_current_voice = "voice/bai/bai_0008.ogg"
            voice "voice/bai/bai_0008.ogg"
            $ vn2_face("bai", "neutral")
            bai "手稳着。抓边绳别攥太死。"
            nar "旁边蓝羽蹲在板边撬松板看桩根，青岩在板那头擦箱底，都看得见这边。他把用过的旧药布条收进兜里，没丢在板上。"
            nar "你站起来，攥了攥那只手，药布贴得住。前面板缝渗水，你抓住边绳试了一下，五指收紧，布边没滑。"
            think "他先处理我的手，再处理自己。布缠得齐整，一圈是一圈。"

        "把撬松的木板压回去":
            nar "你转身回到刚才那块翘起的板边，把板角踩实，又从坡边捡碎石垫进板缝。板面不再晃，踩上去只有一声闷响。"
            $ vn2_current_voice = "voice/lan/lan_0010.ogg"
            voice "voice/lan/lan_0010.ogg"
            $ vn2_face("lan", "happy")
            lan "垫稳了。后面的人过这儿，脚不会滑。"
            nar "他跟过来，伸手在板角上压了两下，确认石头吃进缝里，才把手收回去。"

        "看青岩擦样本箱":
            nar "你走到板那头，青岩正拿干布擦箱底的泥。你伸手扶着箱角，让他擦得匀一些。"
            $ vn2_current_voice = "voice/qing/qing_0006.ogg"
            voice "voice/qing/qing_0006.ogg"
            $ vn2_face("qing", "neutral")
            qing "板上有水。箱子搁在干处，别贴着板缝。"
            nar "他把擦下来的泥捻成一小团，弹到坡下去。箱扣掀开看了一眼，分格没湿，他才把扣压回去。"

    # --- 节点 5/8 · 三里走完 ---
    nar "三里的路，走了一个上午。"
    zhou "过了。谁也没掉队。"
    nar "板越往后越窄，最窄的地方只能侧着身过。有几段塌了半边，你扶着边绳探过去。"
    nar "蓝羽在前面报板况，后面的人听见一句，踩一步。白砚的药箱一路磕着板边，青岩在队尾，脚步慢半拍。"
    nar "谁的呼吸都压得很低。板声一声接一声。"
    think "三里不长。可这段路走得像比一上午还久。"

    # --- 节点 6/8 · 路上记号（menu） ---
    menu:
        "把旧钉的位置记进地图边角":
            $ vn2_aff_add("lan", 3)
            $ vn2_show("lan", expr="neutral", pos="left")
            nar "蓝羽凑过来看，在地图边角补了一个很小的点。"
            $ vn2_current_voice = "voice/lan/lan_0011.ogg"
            voice "voice/lan/lan_0011.ogg"
            $ vn2_face("lan", "neutral")
            lan "铁钉，不是木楔。这一带早先有人来过。"
            nar "他拿铅笔在点旁边画了一道极短的线，标明钉在板的哪一侧。写完把图角抹平。"
            $ vn2_current_voice = "voice/lan/lan_0012.ogg"
            voice "voice/lan/lan_0012.ogg"
            $ vn2_face("lan", "neutral")
            lan "旧钉的位置别圈出来。点着就行。"
            nar "蓝羽把铅笔头在指间转了半圈，又在图边补了个极小的记号，标明这处旧钉离栈道口几步。"

        "把水壶递给白砚":
            $ vn2_aff_add("bai", 3)
            $ vn2_show("bai", expr="sad", pos="center")
            nar "白砚喝了一口，水壶放回你手边。他扫了一眼你渗汗的药布。"
            $ vn2_current_voice = "voice/bai/bai_0009.ogg"
            voice "voice/bai/bai_0009.ogg"
            $ vn2_face("bai", "sad")
            bai "药布渗了汗。晚上我再换。"
            nar "他把水壶在掌心里转了半圈，才搁回你伸手够得到的位置。他自己那只壶挂在箱侧，一路没摘下来喝过。"
            nar "你递过去的时候，壶身还是温的。"

        "替青岩把样本箱拎离湿板":
            $ vn2_aff_add("qing", 3)
            $ vn2_show("qing", expr="neutral", pos="right")
            nar "青岩正把箱底擦了又擦。你接过来，搁到干处。"
            $ vn2_current_voice = "voice/qing/qing_0007.ogg"
            voice "voice/qing/qing_0007.ogg"
            $ vn2_face("qing", "neutral")
            qing "淋过雨的样本，读数就废了。"
            nar "他跟着你把箱子挪到背风的板角，又拿布把箱面沾的水迹抹掉。分格掀开一道缝，对着光看了看，合上扣好。"

    # --- 节点 7/8 · 板缝泥水 ---
    nar "歇脚的工夫，潮气又重了一层。板缝里往外渗泥水，一滴一滴落在下一块板上。"
    nar "蓝羽把地图上那条断线和栈道旧钉的位置对照了一遍。断线不是断在河上，是断在铁上。"
    think "铁。旧站的人造物，已经埋到脚底下了。"

    # --- 节点 8/8 · 接上土路 ---
    nar "栈道尽头接上土路。最后一块板压在土坡上，板边被踩得发圆。"
    nar "身后的栈道退回雾里。路往坡上抬，树影一层比一层疏。"

    # --- 节点 9/9 · 栈道尽头扎营（menu · C 批营地容器） ---
    nar "栈道到这里断了。最后一块板压在土坡根上，再往前没有桩，也没有边绳。"
    nar "日头压到树冠底下，再往前摸黑走，找不着第二块能落脚的平地。"
    nar "蓝羽沿坡根绕了半圈，在三处地面各踩了一下，回头看你。"

    $ vn2_show("lan", expr="neutral", pos="right", trans=dissolve_soft)

    $ vn2_current_voice = "voice/lan/lan_0013.ogg"
    voice "voice/lan/lan_0013.ogg"
    $ vn2_face("lan", "neutral")
    lan "今晚就在这儿落。三处，各有各的毛病。"
    nar "白砚把药箱搁在脚边，从箱侧抽出一块干布，蹲下去，按在最近一块地面上，掌心隔着布压了压，又翻过布角看了一眼。"

    $ vn2_hide("lan", trans=dissolve_soft)
    $ vn2_show("bai", expr="sad", pos="left", trans=dissolve_soft)

    $ vn2_current_voice = "voice/bai/bai_0010.ogg"
    voice "voice/bai/bai_0010.ogg"
    $ vn2_face("bai", "sad")
    bai "布返潮了。地底下的水，今晚还没全退。"
    nar "青岩把样本箱从背上摘下来，抱在怀里，视线把坡根、老树、溪边各扫了一遍，像在给三处地方编号。"
    nar "风从坡底翻上来，带着湿土味。林子里的雾压在低处，再不走远，天黑之前就得把睡袋铺开。"
    think "营地选在哪一块地，今晚谁的觉能睡干，谁的靴能烤透，这会儿定。"

    menu:
        "今晚扎在哪一处？"

        "崖根凹处，背风":
            $ vn2_aff_add("lan", 2)
            $ vn2_hide("bai")
            $ vn2_show("lan", expr="neutral", pos="left")
            nar "蓝羽沿崖根走出两步，脚尖在三块地上各压了压，踩出一个浅窝才收手。"
            $ vn2_current_voice = "voice/lan/lan_0014.ogg"
            voice "voice/lan/lan_0014.ogg"
            $ vn2_face("lan", "neutral")
            lan "这块。脚踩下去不下陷。边上那块一踩一个软坑，不能睡人。"
            nar "他把绳解下一段，一头系在崖根石角上，另一头压到营地边的石头底下。夜里谁起身，先攥绳再迈步。"
            nar "石壁挡风，可地上一层潮气。白砚隔布按上去，布心很快洇深一块。"
            $ vn2_hide("lan")
            $ vn2_show("bai", expr="neutral", pos="center")
            $ vn2_current_voice = "voice/bai/bai_0011.ogg"
            voice "voice/bai/bai_0011.ogg"
            $ vn2_face("bai", "neutral")
            bai "地是湿的。睡袋底下得垫两层干枝，别直接贴泥。"
            nar "四个人把干枝折来铺底。青岩把样本箱抬到石棱上，药箱搁在靠壁的干角。"
            nar "火生得慢，柴芯潮，火苗只够暖到鞋尖。后半夜崖壁那边有人压着嗓子咳了两声，靴底到天亮没干透。"

        "老树底下，地面干":
            $ vn2_aff_add("bai", 2)
            $ vn2_hide("lan", trans=dissolve_soft)
            $ vn2_show("bai", expr="happy", pos="center")
            nar "白砚蹲在树根间，干布按进落叶层底下，掌心隔着布来回揉了两下，再把布翻起来看。"
            $ vn2_current_voice = "voice/bai/bai_0012.ogg"
            voice "voice/bai/bai_0012.ogg"
            $ vn2_face("bai", "happy")
            bai "这块干。潮气在半尺以下，布心没返。"
            nar "他抬起头，看了一眼头顶交叠的枝桠，指尖点了点其中一根发黑的枯枝。"
            $ vn2_current_voice = "voice/bai/bai_0013.ogg"
            voice "voice/bai/bai_0013.ogg"
            $ vn2_face("bai", "sad")
            bai "就是头上这些枝，不牢靠。夜里风一拽，说不准落哪根。"
            nar "四个人把睡袋挪到树干外侧，避开正上方那几根枯枝。青岩把样本箱搁在盘根拱起的干棱上。火在树根边生，火苗比别处立得高。"
            nar "风从树缝里漏下来。后半夜一根细枝落下来，砸在睡袋外侧的泥上，没人起身，都醒了半分。靴底沾的是干土，天亮时鞋帮是暖的。"

        "溪边近水处":
            $ vn2_hide("bai")
            $ vn2_show("qing", expr="neutral", pos="right")
            nar "溪在坡脚下，水很浅，听见流声看不见亮。营地挨水扎，取水不用绕远，可溪边的泥被踩出一层软底。"
            nar "青岩先把样本箱抱到溪岸高处的干土上，掀开分格看了一眼，才把扣压回去。"
            nar "头一趟蓝羽过去拎水，回来时两只靴帮全湿了。睡袋铺在岸坡稍高的一道土棱上，离水远一步。"

    $ vn2_hide_all(trans=dissolve_soft)

    nar "营地支好，天已经全黑。四个人的睡袋在地上排开，火照着鞋尖这一圈。"
    nar "蓝羽把地图摊在火边，指尖压在断线尽头。那条线断在崖后，明天要过的就是断崖。"
    think "明天过断崖。地图上被擦掉的那段路，就在崖后。"

    $ vn2_hide_all(trans=dissolve_soft)
    $ vn2_leave_chapter()
