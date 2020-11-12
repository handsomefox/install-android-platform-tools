ECHO %PATH% > PATH.TMP
SETX PATH "%PATH%;%SYSTEMDRIVE%\platform-tools" /m
pause
