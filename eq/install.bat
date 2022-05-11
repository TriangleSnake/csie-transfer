chcp 65001
@echo off
SET /P haspy=是否有安裝Python(Y/N)
IF %haspy% == N (echo 正在載入Python安裝元件)
IF %haspy% == N (start python-3.10.4-amd64.exe /wait)
SET /P hasgc=是否有安裝地牛WakeUp(Y/N)
IF %hasgc% == N (echo 正在載入地牛WakeUp安裝元件)
IF %hasgc% == N (start OXWU-Setup-win64.exe /wait)
pip install -r requirement.txt
echo 安裝完成，請手動至地牛WakeUp連動
echo "地牛WakeUp->設定->其他->連動設定"
pause