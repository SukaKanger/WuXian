## This file contains options that can be changed to customize your
## game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't
## uncomment them. Lines beginning with a single '#' mark are
## commented-out code, and you may want to uncomment them when
## appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default
## window title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("雾线")


## Determines if the title given above is shown on the main menu
## screen. Set this to False to hide the title.

define gui.show_name = True


## The version of the game.
## 版本号集中定义在 game/core/05_version.rpy（单一真值），本文件不再
## 重复赋值；界面统一用 [config.version] 插值引用，不要在别处硬编码版本串。


## Text that is placed on the game's about screen. Place the text between
## the triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")


## A short name for the game used for executables and directories in the
## built distribution. This must be ASCII-only, and must not contain
## spaces, colons, or semicolons.

define build.name = "WuXian"

## Android/Gradle 使用的发行版本号必须是纯数字点分，不带阶段后缀。
## 游戏内展示仍使用 config.version（V1.28.9 Beta）。
define build.version = "1.28.16"

## 发行目录名必须 ASCII，且不能包含空格、冒号、分号。
## 外部展示版本仍由 config.version 提供（V1.28.9 Beta），这里只固定发行目录/产物前缀。
define build.directory_name = "WuXian-1.28.16-beta"


## Where the game keeps its save files and persistent data. Leave this
## alone once the game ships — changing it "loses" every player's progress.

define config.save_directory = "WuxianVN2-1"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are
## shown to the player by default. Setting one of these to False will
## hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

## VN2 混音默认（2026-11-18 调整为 50%）
## 目标：语音保持 90%，音乐/音效默认 50%；角色开口时音乐自动退到约 18%。
## 新玩家使用这些默认值；已有 persistent 的玩家由 50_audio.rpy 的一次性迁移补齐。
define config.default_music_volume = 0.50
define config.default_sfx_volume = 0.50
define config.default_voice_volume = 0.90
define config.default_emphasize_audio = True
## 设置页写的是「退到约 18%」，这里必须与文案一致。
define config.emphasize_audio_volume = 0.18
define config.emphasize_audio_time = 0.35

## 设置页拖动语音滑杆时的试听样本（第一句蓝羽台词，约 5 秒）
define config.sample_voice = "voice/lan/lan_0001.ogg"


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played
## while the player is at the main menu. This file will continue playing
## into the game, until it is stopped or another file is played.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that
## no transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts
## does not exist. Instead, use a with statement after showing
## the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again
## once dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any
## other number is the number of characters per second to type out.
## VN2: 默认 28 字/秒；瞬时文本会让打字音链路整段失效。

default preferences.text_cps = 28


## The default auto-forward delay. Larger numbers lead to longer waits,
## with 0 to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save
## files for this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.
##
## 本工程已在文件开头（build.name 下方）显式定义为 "WuxianVN2-1"，
## 这里不再重复 define（重复 define 会被 lint 报 already defined）。

# define config.save_directory = "gui-7"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "images/ui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution
## files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/**.ogg"
    ## matches ogg files in the game directory or any of its subdirectories, and
    ## "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## 内部迭代文档与开发存档不进发行包（仓库内保留）：
    ## game/_docs 存游戏口径、契约、审查报告与历史记录，其中含已被否定的旧方案。
    build.classify('game/_docs/**', None)
    build.classify('game/saves/**', None)

    ## 发版时排除项目根目录下的历史备份、图标工作目录和验收截图，
    ## 避免把旧立绘、旧背景与中间图重复压进 APK。
    build.classify('_backup*/**', None)
    build.classify('_icon_work*/**', None)
    build.classify('shots/**', None)

    ## 不把已生成的旧 APK、开发工具、语音源 WAV 和 QA 工程压进新 APK。
    build.classify('*.apk', None)
    build.classify('*.zip', None)
    build.classify('_tools/**', None)
    build.classify('_voice_source_wav/**', None)
    build.classify('_qa_headless*/**', None)
    build.classify('_lint_tmp*/**', None)
    build.classify('build/**', None)
    build.classify('dist/**', None)
    build.classify('_qa_*', None)
    build.classify('*.baiduyun.*', None)
    build.classify('draft_*/**', None)
    build.classify('*.txt', None)
    build.classify('game/_qa_automated.rpy', None)
    build.classify('game/_qa_automated.rpyc', None)
    build.classify('game/_qa_cg_demo.rpy', None)
    build.classify('game/_qa_cg_demo.rpyc', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to perform in-app purchases.
## It can be found in the Google Play developer console,
## under "Monetize" > "Monetization Setup" > "Licensing".

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project,
## separated by a slash.

# define build.itch_project = "renpytom/test-project"
