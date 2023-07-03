'Este programa esta destinado a inventariar as máquinas da Sapore
'Em  desenvolvimento e testes pela equipe da TI Sede

'Inicia o CollectIndo.bat em segundo plano
Set objShell = CreateObject("WScript.Shell")
objShell.Run "C:\path_to_collectinfo.bat\CollectInfo.bat", 0, True
