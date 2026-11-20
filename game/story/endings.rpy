# ============================================================
#  VN2 • 八个结局演出（契约 §4）
#  ------------------------------------------------------------
#  label 命名：vn2_end_<key>；每个只演「这一刻」的场景与对白，
#  最后一行必须是 return（不 jump、不 leave_chapter）。
#  ch26 用 call expression ("vn2_end_" + vn2_ending_key) 派发。
#  素材只用现有 bg / 立绘 / amb / bgm，不新增图片文件。
# ============================================================


# ---------- 蓝羽 · 同行 ----------
label vn2_end_lan_together:
    $ vn2_unlock_cg("cg_end_lan_together_v1")

    scene bg forest with slow_fade
    $ vn2_amb("forest")
    $ vn2_bgm("ending")

    $ vn2_show("lan", pos="center", trans=dissolve_soft)
    $ vn2_cg_show("images/cg/cg_end_lan_together_v1.png", trans=dissolve_soft)

    nar "雾从树冠缝里漏下来，一层薄，贴着湿泥面慢慢走。蓝羽蹲在栈道边，把地图摊在膝上。那截断线他重画过一遍：断口处两道铅笔线叠在一起，新的一道压着旧的一道，接上了。"
    $ vn2_current_voice = "voice/lan/lan_0153.ogg"
    voice "voice/lan/lan_0153.ogg"
    lan "出去以后，我把整张图重画一遍。"
    zhou "断线那一笔呢？"
    $ vn2_current_voice = "voice/lan/lan_0154.ogg"
    voice "voice/lan/lan_0154.ogg"
    lan "补上。不描旧的，重新走一遍，记下来。"
    nar "他把图折好，折痕压在原来那道旧痕上，一丝没偏。队徽收在他身上，隔着布，不露边。他起身，拍掉膝上的湿泥，走在前面。你跟在后面，一前一后，隔着半步。走出两步，他又停下，从内侧口袋摸出那枚队徽。断口的别针只剩半截，他把它别在两个人背包带挨着的那一段上，按了按，确认扣住了布。"
    $ vn2_current_voice = "voice/lan/lan_0155.ogg"
    voice "voice/lan/lan_0155.ogg"
    lan "跟紧。栈道滑，别踩我踩过的那块松板。"
    zhou "嗯。"
    nar "他没回头，尾巴往你这边偏了半寸。林子两边的雾往中间收。天光从枝桠间漏下来，一道一道，落在湿泥上。两道影子压在泥上，一前一后，谁也没并到谁旁边。"
    $ vn2_current_voice = "voice/lan/lan_0156.ogg"
    voice "voice/lan/lan_0156.ogg"
    lan "上一次走这段，是我一个人。"
    nar "他声音很平，像说给路听。"
    $ vn2_current_voice = "voice/lan/lan_0157.ogg"
    voice "voice/lan/lan_0157.ogg"
    lan "这一次不是。"
    nar "栈道尽头能看见林线。风把潮气吹过来，又带走。走到栈道口，他偏头叫了你一声。这回后半句没被风盖住。"
    $ vn2_current_voice = "voice/lan/lan_0158.ogg"
    voice "voice/lan/lan_0158.ogg"
    lan "[player_name]。"
    nar "他念完，等你应了，才把视线挪回前面的路。"
    zhou "在。"
    nar "出林之前，他在前面停了一下，抬手把路标刻进树干：圈加一横。刻完没回头，接着走。背包带上拴了一路的那道双结，他抬手解开。结眼松开，旧绳褪下来一截，仍松松搭在两个人中间，没有绷紧。"
    think "线接上了。人也在前面。"
    nar "你跟着他，走完最后三里。"

    $ vn2_hide_all(trans=dissolve_soft)
    $ vn2_cg_hide(trans=dissolve_soft)
    return


# ---------- 蓝羽 · 独行 ----------
label vn2_end_lan_alone:
    $ vn2_unlock_cg("cg_end_lan_alone_v0")

    scene bg cliff with slow_fade
    $ vn2_amb("forest")
    $ vn2_bgm("ending")

    $ vn2_show("lan", pos="center", trans=dissolve_soft)
    $ vn2_cg_show("images/cg/cg_end_lan_alone_v0.png", trans=dissolve_soft)

    nar "公路在崖下铺开，白花花的一条。蓝羽停在崖边，没有跟你往下走。风从崖底往上灌，把草压弯一片。他站在风里，尾巴收在腿边。"
    $ vn2_current_voice = "voice/lan/lan_0159.ogg"
    voice "voice/lan/lan_0159.ogg"
    lan "我姐没走出来。我得回去找。"
    zhou "一个人回去？"
    $ vn2_current_voice = "voice/lan/lan_0160.ogg"
    voice "voice/lan/lan_0160.ogg"
    lan "习惯了。"
    nar "他把地图从内侧口袋掏出来，折好，压在你手里。折痕很深，断线那一段，他用指甲描过。队徽他摘下来，放在脚边那块平石头上。金属磨得发亮，别针断在半截。"
    zhou "队徽不留着？"
    $ vn2_current_voice = "voice/lan/lan_0161.ogg"
    voice "voice/lan/lan_0161.ogg"
    lan "留给你。哪天你走这条线，替我看一眼。"
    nar "他说完，转身往雾里走。背影走得很慢，没有停，也没有回头。雾从崖腰漫上来，把他一截一截盖住。先盖住脚，再盖住肩，最后只剩尾巴尖在雾里晃了一下，也没了。你站在原地，手里攥着那张图。石头上的队徽被风刮得发凉。腕口那截旧绳头还缠着，双结松在外面，没往里收紧。"
    think "路还在脚下，他选的是另一条。"
    nar "图角被雾打潮卷起来一点，你用掌心压平；绳头那道双结还松着，没解。这条绳当初说归你收。他往后走的那段，绳在不在他手里，没人知道；结留在你这儿，也没人替他打第二个。公路在下面等你。你没有立刻下去，也没有喊他。风又起了一阵，草压弯一片，又直起来。公路往下绕进雾里。下一个走到这条线上的人，会不会替他把绳收起来，雾里看不出来。"

    $ vn2_hide_all(trans=dissolve_soft)
    $ vn2_cg_hide(trans=dissolve_soft)
    return


# ---------- 白砚 · 同行 ----------
label vn2_end_bai_together:
    $ vn2_unlock_cg("cg_end_bai_together_v1")

    scene bg firelight with slow_fade
    $ vn2_amb("fire")
    $ vn2_bgm("ending")

    $ vn2_show("bai", pos="center", trans=dissolve_soft)
    $ vn2_cg_show("images/cg/cg_end_bai_together_v1.png", trans=dissolve_soft)

    nar "火压得很低。白砚坐在火边，把药箱打开，一支一支点剩下的针剂。他抽出一卷药布，递给你。布是干的，边角磨毛了。"
    $ vn2_current_voice = "voice/bai/bai_0122.ogg"
    voice "voice/bai/bai_0122.ogg"
    bai "手腕那道伤，重新缠一遍。旧布湿了，不换会烂。"
    nar "你把手伸过去。他低头缠，绕得很紧，打结的时候指尖在你腕上停了一下。"
    $ vn2_current_voice = "voice/bai/bai_0123.ogg"
    voice "voice/bai/bai_0123.ogg"
    bai "药箱分一半。针剂三支归你，两支归我。"
    zhou "你自己那份够吗？"
    nar "他手上的动作停了一息。火光照着他半边脸，另外半边在暗里。他没接这话。指尖把自己那两支针剂在格位里并排摆正，管身贴着管身，推到格位中间，又把箱盖内侧那卷药布的边角掖平。他把药箱扣上，扣得很慢，一道搭扣一道搭扣。夹层里那张叠成小方的纸包空了，半片药早分着吃完。他把空纸包折回去，收进药箱盖的夹层里，没扔。"
    $ vn2_current_voice = "voice/bai/bai_0124.ogg"
    voice "voice/bai/bai_0124.ogg"
    bai "出去以后，针剂够开个小诊所。手稳，饿不着。"
    zhou "嘴别硬。"
    nar "他没笑，肩膀却松下来一点。火光落在两个人中间，不烫，也不往这边压过来。他低头解自己腕上那圈旧药布。活扣捏在指尖，一拉就开，布松下来，他重新卷好，搁进箱侧袋。"
    $ vn2_current_voice = "voice/bai/bai_0125.ogg"
    voice "voice/bai/bai_0125.ogg"
    bai "以前这个结，都是你替我打的。"
    $ vn2_current_voice = "voice/bai/bai_0126.ogg"
    voice "voice/bai/bai_0126.ogg"
    bai "手稳这回事，我以前只信自己那只手。这回信两只。"
    zhou "下回再抖呢？"
    $ vn2_current_voice = "voice/bai/bai_0127.ogg"
    voice "voice/bai/bai_0127.ogg"
    bai "那就再按一次。"
    nar "夜里路长，你们轮流守着。谁也没先睡，药箱搁在两个人中间，各分一半。"

    $ vn2_hide_all(trans=dissolve_soft)
    $ vn2_cg_hide(trans=dissolve_soft)
    return


# ---------- 白砚 · 独行 ----------
label vn2_end_bai_alone:
    $ vn2_unlock_cg("cg_end_bai_alone_v0")

    scene bg firelight with slow_fade
    $ vn2_amb("fire")
    $ vn2_bgm("ending")

    $ vn2_show("bai", pos="center", trans=dissolve_soft)
    $ vn2_cg_show("images/cg/cg_end_bai_alone_v0.png", trans=dissolve_soft)

    nar "门口的风灌进来，火歪了一下。白砚把药箱搁在脚边，站在火边没动。你小臂上那道口子还渗着血，路上一直没顾上。他看见，把箱盖掀开，重新打开。"
    $ vn2_current_voice = "voice/bai/bai_0128.ogg"
    voice "voice/bai/bai_0128.ogg"
    bai "伸手。最后一道，我处理完。"
    nar "他就着火光清洗、上药、缠布。手很稳，绕到最后一圈，打结，剪断线头。收口打的是活扣。结眼留在外侧，一拉就开。他指腹在结上按了按，没多说。"
    $ vn2_current_voice = "voice/bai/bai_0129.ogg"
    voice "voice/bai/bai_0129.ogg"
    bai "别沾水。三天换一次药布，药在箱侧袋里。"
    zhou "你呢？"
    $ vn2_current_voice = "voice/bai/bai_0130.ogg"
    voice "voice/bai/bai_0130.ogg"
    bai "那个人我得留下照顾。走不开。"
    nar "他把剩下的针剂往你这边推了一支，又收回去两支，留一支在自己箱里。他指尖在箱侧袋里按了一遍，把药布推到顺手能摸到的位置，才把袋口折回去。"
    $ vn2_current_voice = "voice/bai/bai_0131.ogg"
    voice "voice/bai/bai_0131.ogg"
    bai "药在我这儿才有用。我是医生。"
    nar "箱底那格空着，是他自己那份减下来的位置。他合上盖，没有往里补，你背起自己的东西。他在门口替你把最后一道伤口包好，直起身。他没有送你出门。转身往回走，脚步踩在余烬边上，很轻。你走出火光。身后没有脚步声跟上来，只有火里炭塌下去的一声。跟着又是药箱盖扣上的一声。搭扣一道一道，扣得很慢，很齐，扣完就静了。风从门外吹进来，药布上的药味还留在你手腕上，凉的。"
    nar "腕上那道活扣还松着。三天后谁替你换布，他没说，你也没问。风把门里的炭火味送出来一阵，又收回去。"
    think "他把能给的都给了，人留在了里面。"

    $ vn2_hide_all(trans=dissolve_soft)
    $ vn2_cg_hide(trans=dissolve_soft)
    return


# ---------- 青岩 · 同行 ----------
label vn2_end_qing_together:
    $ vn2_unlock_cg("cg_end_qing_together_v0")

    scene bg hall with slow_fade
    $ vn2_amb("tunnel")
    $ vn2_bgm("ending")

    $ vn2_show("qing", pos="center", trans=dissolve_soft)
    $ vn2_cg_show("images/cg/cg_end_qing_together_v0.png", trans=dissolve_soft)

    nar "走廊的灯还亮着。青岩站在档案柜前，样本箱抱在怀里，登记簿夹在胳膊底下。他把最底下那一格拉开，把誊过的副本一页一页理齐，和半页导师的记录并排放在一起。两张纸边不齐，署名的笔迹是同一路。"
    $ vn2_current_voice = "voice/qing/qing_0093.ogg"
    voice "voice/qing/qing_0093.ogg"
    qing "原件我带走。副本你收着。"
    zhou "不怕我弄丢？"
    $ vn2_current_voice = "voice/qing/qing_0094.ogg"
    voice "voice/qing/qing_0094.ogg"
    qing "你不会。"
    nar "他合上箱盖，却没有立刻把箱子抱回去。手在箱扣上停了一会儿。从导师走后，箱子一直压在他怀里：走路抱着，睡觉搁在膝上。他把箱子换到你这边肩上，自己空出一只手，去拿登记簿。"
    $ vn2_current_voice = "voice/qing/qing_0095.ogg"
    voice "voice/qing/qing_0095.ogg"
    qing "箱子沉。两个人抬，比一个人抱稳。"
    nar "你抬箱的这一边，他抬那一边。箱带分作两半，各落一侧肩上。箱角离开柜面，他腾出的手扶住登记簿，没再往箱扣上回。走廊的灯你们没关。走到门口，他回头看了一眼那排空柜子。空柜子留在身后，柜门都合上了，柜面的灰印留在原处。布包里剩的两份干粮，他递一份给你。两个人站在门口把它吃完，没再推来推去，碎屑拢进掌心。登记簿夹在他胳膊底下，纸角压平，走路时不晃。"
    nar "这一次，他跟你一起迈出门。手没有再回去按箱扣。两张纸上的署名并排躺着，墨迹一深一浅，都朝着同一个方向。"
    think "他放下箱子了。不是放下记录，是放下一直自己扛着的那截。"
    nar "门外的光落在石阶上。他走在你旁边，箱角由两个人一起护着，没磕着石头。"

    $ vn2_hide_all(trans=dissolve_soft)
    $ vn2_cg_hide(trans=dissolve_soft)
    return


# ---------- 青岩 · 独行 ----------
label vn2_end_qing_alone:
    $ vn2_unlock_cg("cg_end_qing_alone_v1")

    scene bg hall with slow_fade
    $ vn2_amb("tunnel")
    $ vn2_bgm("ending")

    $ vn2_show("qing", pos="center", trans=dissolve_soft)
    $ vn2_cg_show("images/cg/cg_end_qing_alone_v1.png", trans=dissolve_soft)

    nar "档案柜前，青岩把样本箱抱紧了些。登记簿压在箱盖上，纸角露出来。柜面的灰印他数过一遍，哪一格空着，他心里有数。箱盖上搁着那块没吃完的干粮，纸包敞着口，他没再掰第二回。登记簿压在箱盖上，和干粮搁在一处，纸角都被他压平。"
    $ vn2_current_voice = "voice/qing/qing_0096.ogg"
    voice "voice/qing/qing_0096.ogg"
    qing "我不走。总得有人记得这儿发生过什么。"
    zhou "一个人守着？"
    $ vn2_current_voice = "voice/qing/qing_0097.ogg"
    voice "voice/qing/qing_0097.ogg"
    qing "习惯了。"
    nar "他把钥匙从台上推过来，推到你手边。金属碰着石面，凉的一声。空着的柜子格子一排一排，他临走又扫了一眼，像把这些格子的位置都记进脑子里。他抱起箱子，转身往走廊深处走。石门在尽头，半开着，门内的暗把他的影子一点点吃掉。你站在门外，没有跟进去。脚步声一下一下，踩在石面上，越来越远。他走到门口，停了一下，没回头。"
    nar "箱子在他怀里，抱得很紧，登记簿的纸角从箱盖上翘起来，又被他压平。干粮的纸角被门缝的风掀起一点，压在登记簿底下。石门从里面合上。先是一声闷响，再是石缝挤紧的细声，最后什么都没有了。潮气贴着墙退回去。走廊黑成一条线。你手里攥着那把钥匙，站在门外，听了一会儿。门后再没有第二声。门缝底下还漏着一线灯黄。站里那盏灯没熄，亮在门后头，照着他和那一排空柜子。"
    think "名字留在里面了，他替那些人守着。"

    $ vn2_hide_all(trans=dissolve_soft)
    $ vn2_cg_hide(trans=dissolve_soft)
    return


# ---------- 封口 ----------
label vn2_end_sealed:
    $ vn2_unlock_cg("cg_end_sealed_v1")

    scene bg hall with slow_fade
    $ vn2_amb("tunnel")
    $ vn2_bgm("ending")

    $ vn2_show("shiqi", pos="center", trans=dissolve_soft)
    $ vn2_cg_show("images/cg/cg_end_sealed_v1.png", trans=dissolve_soft)

    nar "铁皮贴上门框的时候，敲钉的声音一下一下，在走廊里撞出回音。门是双层的，铁皮压着木板。钉完最后一枚，接缝处糊上泥，再看不见里面那道石缝。墙角那台旧无线电还响着。杂音一阵一阵，中间夹着编号，几个数字，念完就断，像从很远的地方拨过来。编号念完一遍，又是杂音。没有人去关它，也没有人去应。十七站在走廊尽头，没有走近。"
    $ vn2_current_voice = "voice/shiqi/shiqi_0011.ogg"
    voice "voice/shiqi/shiqi_0011.ogg"
    shiqi "封了，就再也打不开。想清楚。"
    nar "你点头。"
    $ vn2_current_voice = "voice/shiqi/shiqi_0012.ogg"
    voice "voice/shiqi/shiqi_0012.ogg"
    shiqi "名字我替你们抹掉。出去以后，别提这座站。"
    nar "蓝羽、白砚、青岩站在廊下，先后往外走。三个人都没有回头。走出廊口，三个人一个一个应过名。蓝羽，在；白砚，在；青岩，在。点到最后一个，是你自己，你应了一声，嗓子不高。四个人都还站着。门在身后封上，廊里那些格子留在里面；外面这四个，一个不少。队徽、药箱、登记簿各自压在身上，没有人停下来看封好的门第二眼。"
    nar "石门外的干土上，各留了一件东西：一截盘好的旧绳头，是早年那条烂芯绳褪下的头；一只折成小方的空药纸包，半块没吃完的干粮。没人回头捡。潮气贴着墙退回去。走廊黑成一条线。无线电里的编号又念了一遍，这一遍你们走出了门，没听完。地上留着几枚拔下来的钉子，你没捡。雾从墙根漫过来，把钉子的锈色一点点盖住。身后没有门声再响。铁皮把所有声音都关在了里面。"

    $ vn2_hide_all(trans=dissolve_soft)
    $ vn2_cg_hide(trans=dissolve_soft)
    return


# ---------- 第七天（真结局） ----------
label vn2_end_seventh:
    $ vn2_unlock_cg("cg_end_seventh_v0")

    scene bg gate with slow_fade
    $ vn2_amb("forest")
    $ vn2_bgm("ending")

    $ vn2_show("shiqi", pos="center", trans=dissolve_soft)
    $ vn2_cg_show("images/cg/cg_end_seventh_v0.png", trans=dissolve_soft)

    if vn2_lock_route == "lan":
        $ vn2_show("lan", pos="left", trans=dissolve_soft)
        $ vn2_current_voice = "voice/lan/lan_0162.ogg"
        voice "voice/lan/lan_0162.ogg"
        lan "走吧，出去。"
    elif vn2_lock_route == "bai":
        $ vn2_show("bai", pos="left", trans=dissolve_soft)
        $ vn2_current_voice = "voice/bai/bai_0132.ogg"
        voice "voice/bai/bai_0132.ogg"
        bai "药箱我带着。"
    elif vn2_lock_route == "qing":
        $ vn2_show("qing", pos="left", trans=dissolve_soft)
        $ vn2_current_voice = "voice/qing/qing_0098.ogg"
        voice "voice/qing/qing_0098.ogg"
        qing "记录一页不少。"

    nar "第七天。石门从里面打开。门轴转得很慢，石缝里渗出一股潮味，混着土腥。十七站在门口，骨珠挂在腕上，刻纹被光描出来。他把珠子从腕上褪下来，搁在门槛上，往你这边推了推。珠子碰着石面，一声轻响。"
    $ vn2_current_voice = "voice/shiqi/shiqi_0013.ogg"
    voice "voice/shiqi/shiqi_0013.ogg"
    shiqi "珠子留下。你把证据带出去了，这些，该让外面知道。"
    nar "防水袋在你怀里，一页没湿。纸隔着布，硬的，边角被体温焐得发暖。他侧身让出门道。天光落在石阶上，一道，不亮，是雾散以后第一缕。门外的路一直往前，草叶上水珠往下滴。这条线上没有圈加一横的记号，地图上也查不到名字。你走过他身边，他没有跟出来，只抬了抬手。"
    $ vn2_current_voice = "voice/shiqi/shiqi_0014.ogg"
    voice "voice/shiqi/shiqi_0014.ogg"
    shiqi "替我看看外面的天。"
    nar "雾真的散了。路一直通到林外，草叶上的水珠往下滴。没有人喊，也没有人站在光里等谁欢呼。身边那个人走在你半步之后，点了一遍人。数到四个，他低声把那句话又念了一回：四个人，二十七天。话念完，风把它吹散在林子里。没人追问这句话是谁先讲的。证据压在胸口。名字还没一个个写回去，只是外面终于有人知道这里守过什么。"
    think "不是赢了什么。是活着出来了。"
    nar "鞋尖沾上门外的干土，和门里带出来的潮气，一道一道分开。你迈出门槛。天光落在脚边，雾从脚边退开，没有再跟上来。那条没有名字的路往前伸，通向有人烟的地方；门里的事，留给出林以后再说。"

    $ vn2_hide_all(trans=dissolve_soft)
    $ vn2_cg_hide(trans=dissolve_soft)
    return
