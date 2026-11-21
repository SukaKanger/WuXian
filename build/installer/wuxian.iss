; 雾线 WuXian — Windows 解压式安装向导（Inno Setup 7）
; 默认安装到当前用户目录，无需管理员权限；可选安装路径、可选快捷方式。

#define MyAppName "雾线 WuXian"
#define MyAppVersion "2.28.5"
#define MyAppPublisher "SukaKanger"
#define MyAppURL "https://sukakanger.itch.io/wuxian"
#define MyAppExeName "WuXian.exe"
#define SrcDir "L:\AI\FurryVN\20261117_uidemo\build\windows"
#define OutDir "L:\AI\FurryVN\20261117_uidemo\dist"

[Setup]
AppId={{8D3A2C41-5B7E-4F90-A3D6-2C1B4E7A9F10}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
VersionInfoVersion=2.28.5.0
VersionInfoProductVersion=2.28.5.0
VersionInfoCompany=SukaKanger
DefaultDirName={localappdata}\Programs\WuXian
; 安装目录页始终显示：可以直接输入或浏览到任意盘符（C/D/E…），不再锁死在用户目录。
DisableDirPage=no
DirExistsWarning=auto
UsePreviousAppDir=yes
DefaultGroupName=雾线 WuXian
DisableProgramGroupPage=no
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
OutputDir={#OutDir}
OutputBaseFilename=WuXian-Setup-{#MyAppVersion}
SetupIconFile=L:\AI\FurryVN\20261117_uidemo\build\installer\wuxian.ico
Compression=lzma2/max
SolidCompression=yes
WizardStyle=modern
LicenseFile=L:\AI\FurryVN\20261117_uidemo\build\installer\EULA.txt
UninstallDisplayIcon={app}\wuxian.ico
UninstallDisplayName={#MyAppName}
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
ShowLanguageDialog=no
AllowNoIcons=yes
DisableWelcomePage=no

[Languages]
Name: "chinesesimplified"; MessagesFile: "compiler:Languages\ChineseSimplified.isl"

[Tasks]
Name: "desktopicon"; Description: "创建桌面快捷方式"; GroupDescription: "快捷方式："; Flags: unchecked
Name: "startmenuicon"; Description: "创建开始菜单快捷方式"; GroupDescription: "快捷方式："; Flags: checkedonce

[Files]
Source: "{#SrcDir}\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; 快捷方式专用图标：跟安装程序同一个 ico，装完放在 app 目录里给快捷方式引用。
Source: "L:\AI\FurryVN\20261117_uidemo\build\installer\wuxian.ico"; DestDir: "{app}"; DestName: "wuxian.ico"; Flags: ignoreversion

[Icons]
Name: "{autodesktop}\雾线 WuXian"; Filename: "{app}\{#MyAppExeName}"; WorkingDir: "{app}"; IconFilename: "{app}\wuxian.ico"; Tasks: desktopicon
Name: "{group}\雾线 WuXian"; Filename: "{app}\{#MyAppExeName}"; WorkingDir: "{app}"; IconFilename: "{app}\wuxian.ico"; Tasks: startmenuicon
Name: "{group}\免责声明与开源许可"; Filename: "{app}\DISCLAIMER.txt"; IconFilename: "{app}\wuxian.ico"; Tasks: startmenuicon
Name: "{group}\卸载 雾线 WuXian"; Filename: "{uninstallexe}"; Tasks: startmenuicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "启动 雾线 WuXian"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}\game\saves"

