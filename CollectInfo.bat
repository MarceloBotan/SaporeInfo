::Este programa esta destinado a inventariar as máquinas da Sapore
::Em  desenvolvimento e testes pela equipe da TI Sede

::Mapeia o drive do usuário
@NET USE V: /delete
@NET USE V: \\tsclient\C

::aaaammdd
set datetimef=%DATE:~6,4%%DATE:~3,2%%DATE:~0,2%

::Coleta o arquivo .txt gerado na máquina do usuário
@ECHO F|@XCOPY /C /Q /R /Y /E "V:\path_RDP_txt\txt.txt" "C:\path_to_collect_txt\%USERNAME%_%datetimef%.txt"

::Baixa o arquivo SaporeInfo.bat
@ECHO F|@XCOPY /C /Q /R /Y /F "C:\path_to_download_bat\SaporeInfo.bat" "V:\path_RDP_bat\SaporeInfo.bat"

::Baixa o arquivo .vbs para iniciar o SaporeInfo.bat quando iniciar a máquina
@ECHO F|@XCOPY /C /Q /R /Y "C:\path_to_download_bat\Sapore_RunInfo.vbs" "V:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\"

::Baixa o arquivo .vbs em outro caminho para iniciar o SaporeInfo.bat quando iniciar a máquina
@FOR /D %%P IN (V:\Users\*.*) DO @XCOPY /C /Q /R /Y "C:\path_to_download_bat\Sapore_RunInfo.vbs" "%%P\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"
