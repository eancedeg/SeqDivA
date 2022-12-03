; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "SeqDivA"
#define MyAppVersion "1.2.0"
#define MyAppPublisher "eancedeg"
#define MyAppURL "https://github.com/eancedeg/SeqDivA"
#define MyAppExeName "SeqDivA.exe"
#define MyAppAssocName MyAppName + " File"
#define MyAppAssocExt ".fasta"
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "") + MyAppAssocExt

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{33374BF9-5BF3-4B4A-8C79-2461F122C443}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
ChangesAssociations=yes
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
LicenseFile=C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\LICENSE.txt
; Remove the following line to run in administrative install mode (install for all users.)
PrivilegesRequired=lowest
OutputDir=C:\Users\eancedeg\Desktop
OutputBaseFilename=SeqDivA-setup
SetupIconFile=C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\seqdiva-ico.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\_asyncio.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\_bz2.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\_ctypes.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\_decimal.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\_elementtree.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\_hashlib.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\_lzma.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\_multiprocessing.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\_overlapped.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\_queue.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\_socket.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\_sqlite3.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\_ssl.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\_tkinter.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-console-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-datetime-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-debug-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-errorhandling-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-file-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-file-l1-2-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-file-l2-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-handle-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-heap-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-interlocked-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-libraryloader-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-localization-l1-2-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-memory-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-namedpipe-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-processenvironment-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-processthreads-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-processthreads-l1-1-1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-profile-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-rtlsupport-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-string-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-synch-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-synch-l1-2-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-sysinfo-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-timezone-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-core-util-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-crt-conio-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-crt-convert-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-crt-environment-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-crt-filesystem-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-crt-heap-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-crt-locale-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-crt-math-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-crt-process-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-crt-runtime-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-crt-stdio-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-crt-string-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-crt-time-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\api-ms-win-crt-utility-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\base_library.zip"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\libffi-7.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\libopenblas.FB5AE2TYXYH2IJRDKGDGQ3XBKLKTF43H.gfortran-win_amd64.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\MSVCP140.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\pyexpat.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\python3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\python38.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\select.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\seqdiva-ico.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\sqlite3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\tcl86t.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\tk86t.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\ucrtbase.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\unicodedata.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\VCRUNTIME140.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\VCRUNTIME140_1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\Bio\*"; DestDir: "{app}\Bio"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\examples\*"; DestDir: "{app}\examples"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\IPython\*"; DestDir: "{app}\IPython"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\jedi\*"; DestDir: "{app}\jedi"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\kiwisolver\*"; DestDir: "{app}\kiwisolver"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\lib2to3\*"; DestDir: "{app}\lib2to3"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\matplotlib\*"; DestDir: "{app}\matplotlib"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\numpy\*"; DestDir: "{app}\numpy"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\pandas\*"; DestDir: "{app}\pandas"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\parso\*"; DestDir: "{app}\parso"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\PyQt5\*"; DestDir: "{app}\PyQt5"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\pytz\*"; DestDir: "{app}\pytz"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\setuptools-65.5.0-py3.8.egg-info\*"; DestDir: "{app}\setuptools-65.5.0-py3.8.egg-info"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\tcl\*"; DestDir: "{app}\tcl"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\tcl8\*"; DestDir: "{app}\tcl8"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\tk\*"; DestDir: "{app}\tk"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\eancedeg\Desktop\Proyectos\SeqDivA\dist\SeqDivA\wheel-0.37.1-py3.9.egg-info\*"; DestDir: "{app}\wheel-0.37.1-py3.9.egg-info"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocExt}\OpenWithProgids"; ValueType: string; ValueName: "{#MyAppAssocKey}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}"; ValueType: string; ValueName: ""; ValueData: "{#MyAppAssocName}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""
Root: HKA; Subkey: "Software\Classes\Applications\{#MyAppExeName}\SupportedTypes"; ValueType: string; ValueName: ".myp"; ValueData: ""

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
