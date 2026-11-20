# ============================================================
#  VN2 • 核心状态层（schema 2）
#  ------------------------------------------------------------
#  规则：
#   1) 所有跨章状态一律用 default 声明（存档兼容）
#   2) 默认值集中写在 VN2_DEFAULT_VALUES，default 行只引用它，
#      从此改默认值只改一处
#   3) 存档 schema 版本写在 VN2_SAVE_SCHEMA，加载时由
#      vn2_repair_state() 补齐缺失项（见 30_save.rpy）
# ============================================================

init -6 python:

    VN2_SAVE_SCHEMA = 2
    VN2_TITLE = "雾线"
    VN2_SUBTITLE = "二十七日 / 雨林"

    VN2_AFF_KEYS = ("lan", "bai", "qing", "ari")
    VN2_ROMANCE_KEYS = ("lan", "bai", "qing")

    VN2_ROUTE_NAMES = {
        "common": "共同线",
        "lock":   "锁线",
        "lan":    "蓝羽线",
        "bai":    "白砚线",
        "qing":   "青岩线",
        "end":    "结局",
        "solo":   "独自进入",
    }

    VN2_CHAR_NAMES = {
        "zhou":  "玩家",
        "lan":   "蓝羽",
        "bai":   "白砚",
        "qing":  "青岩",
        "ari":   "阿瑞",
        "shiqi": "十七",
    }

    # 锁线门槛：ch14 菜单上对应好感 >= 22 才可进入该线
    VN2_LOCK_THRESHOLD = 22

    # 好感度初始值：10 点起（0–100）
    VN2_DEFAULT_VALUES = {
        "aff_lan":  10,
        "aff_bai":  10,
        "aff_qing": 10,
        "aff_ari":  10,

        # 契约 §2 旗标表（全部 bool）
        "trust_team":       False,  # 队伍把后背交给你
        "close_lan":        False,  # 蓝羽向你交了底
        "lan_map_fixed":    False,  # 帮蓝羽把地图补回去
        "saved_bai":        False,  # 你救过白砚的手
        "bai_treated":      False,  # 陪白砚做完了那台手术
        "bai_rationed":     False,  # ch21 药份选择：余量是否全压在白砚身上
        "know_qing_secret": False,  # 知道青岩守站人的身份
        "qing_trusted":     False,  # 青岩信了你
        "station_key":      False,  # 拿到了站门钥匙
        "evidence_kept":    False,  # 真把证据带出去了（真结局判定只认这个）
        "evidence_copied":  False,  # 先抄了一份名单（ch23 分支，ch24 按编号取格）
        "trust_shiqi":      False,  # 守门人十七信了你
        "route_commit":     False,  # ch25 明确选择“和身边的人一起离开”，不靠隐藏好感补
        "ari_helped":       False,  # 你帮过阿瑞

        "player_name": "队长",

        # 锁线结果：lan / bai / qing / solo（旧档缺失时兜底 solo）
        "vn2_lock_route": "solo",

        # 章节上下文（供存档元数据使用）
        "vn2_chapter_id":    "ch01",
        "vn2_chapter_no":    1,
        "vn2_chapter_title": "",
        "vn2_disp":          None,
        "vn2_disp_label":    "",
        "vn2_route_name":    "共同线",
        "vn2_route_key":     "common",
        "vn2_day":           1,
        "vn2_ending_key":    "",
        # 剧情节奏：cut = 1.28.22 起用的导演剪辑版中段；classic = 旧脚本
        # 老存档只在章节开头读取该值，章节中途仍按旧脚本继续，避免坏档
        "vn2_story_mode":    "cut",
        "vn2_story_rev":     1,
    }


# ---------- 好感度 4 条（0–100；ari 为 NPC，不进结局判定） ----------
default aff_lan  = VN2_DEFAULT_VALUES["aff_lan"]
default aff_bai  = VN2_DEFAULT_VALUES["aff_bai"]
default aff_qing = VN2_DEFAULT_VALUES["aff_qing"]
default aff_ari  = VN2_DEFAULT_VALUES["aff_ari"]


# ---------- 布尔旗标 ----------
default trust_team       = VN2_DEFAULT_VALUES["trust_team"]
default close_lan        = VN2_DEFAULT_VALUES["close_lan"]
default lan_map_fixed    = VN2_DEFAULT_VALUES["lan_map_fixed"]
default saved_bai        = VN2_DEFAULT_VALUES["saved_bai"]
default bai_treated      = VN2_DEFAULT_VALUES["bai_treated"]
default bai_rationed     = VN2_DEFAULT_VALUES["bai_rationed"]
default know_qing_secret = VN2_DEFAULT_VALUES["know_qing_secret"]
default qing_trusted     = VN2_DEFAULT_VALUES["qing_trusted"]
default station_key      = VN2_DEFAULT_VALUES["station_key"]
default evidence_kept     = VN2_DEFAULT_VALUES["evidence_kept"]
default evidence_copied  = VN2_DEFAULT_VALUES["evidence_copied"]
default trust_shiqi      = VN2_DEFAULT_VALUES["trust_shiqi"]
default route_commit     = VN2_DEFAULT_VALUES["route_commit"]
default ari_helped       = VN2_DEFAULT_VALUES["ari_helped"]


# ---------- 玩家称呼（开局命名页写入；旁白仍用「你」，对白用 [player_name] 插值） ----------
default player_name = VN2_DEFAULT_VALUES["player_name"]

# ---------- 锁线结果 / 章节上下文 ----------
default vn2_lock_route     = VN2_DEFAULT_VALUES["vn2_lock_route"]
default vn2_chapter_id     = VN2_DEFAULT_VALUES["vn2_chapter_id"]
default vn2_chapter_no    = VN2_DEFAULT_VALUES["vn2_chapter_no"]
default vn2_chapter_title = VN2_DEFAULT_VALUES["vn2_chapter_title"]
default vn2_disp          = VN2_DEFAULT_VALUES["vn2_disp"]
default vn2_disp_label    = VN2_DEFAULT_VALUES["vn2_disp_label"]
default vn2_route_name     = VN2_DEFAULT_VALUES["vn2_route_name"]
default vn2_route_key      = VN2_DEFAULT_VALUES["vn2_route_key"]
default vn2_day            = VN2_DEFAULT_VALUES["vn2_day"]
default vn2_ending_key     = VN2_DEFAULT_VALUES["vn2_ending_key"]
default vn2_story_mode     = VN2_DEFAULT_VALUES["vn2_story_mode"]
default vn2_story_rev      = VN2_DEFAULT_VALUES["vn2_story_rev"]


# ---------- 界面偏好（自定义项，落 persistent） ----------
default persistent.vn2_text_scale = 1          # 0 小 / 1 标准 / 2 大
default persistent.vn2_cg = set()               # 已解锁 CG 的 id 集合
default persistent.vn2_endings = set()          # 已达成结局 key 集合
default persistent.vn2_unlocked = []             # 已解锁章节（章节选择用；新档为空，ch01 恒可进）
default persistent.vn2_jump_target = "ch01"     # 章节选择跳转目标
default persistent.vn2_seen_title = False       # 是否看过开场提示
default persistent.vn2_intel_seen = set()      # 笔记本：已读过的情报 id 集合


init python:

    # persistent 兜底（老 persistent 文件里没有这些字段时补上）
    if persistent.vn2_text_scale is None:
        persistent.vn2_text_scale = 1
    if persistent.vn2_cg is None:
        persistent.vn2_cg = set()
    if persistent.vn2_endings is None:
        persistent.vn2_endings = set()
    if persistent.vn2_unlocked is None:
        persistent.vn2_unlocked = []
    elif list(persistent.vn2_unlocked) == ["ch01"]:
        # 旧 schema 默认只塞了 ch01（假进度）；迁移为空表，ch01 由解锁判定恒真放行
        persistent.vn2_unlocked = []
    # 过滤掉不在路由表里的旧 id，避免残留把进度算大
    persistent.vn2_unlocked = [cid for cid in (persistent.vn2_unlocked or [])
                               if cid in CHAPTERS]
    if persistent.vn2_intel_seen is None:
        persistent.vn2_intel_seen = set()
    if persistent.vn2_jump_target is None:
        persistent.vn2_jump_target = "ch01"


# ---------- 字号档位（设置面板用） ----------
define VN2_TEXT_SCALES = [
    ("小", 26),
    ("标准", 30),
    ("大", 34),
]
