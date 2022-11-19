## Powershell_C2

A basic Powershell C2 that I made some time ago and how to build it

## Requierments
You'll need to install powershell on [Linux](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-linux?view=powershell-7.3) or you can simply build it on a Windows machine. 
You'll also need [Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation) in order to obfuscate the code (this will help with the endpoint evasion, but It's not granted to work). Back when I tested it, I used AST type obfuscation, this might not work now.    

__Important__
Before converting it to .exe with [ps1 to exe](https://www.majorgeeks.com/files/details/ps1_to_exe.html) it is important to make copies and make small modifications so that each one has a different hash. You'll have to run this app on Windows or make the code executable yourself (I'll be uploading a C program to turn PowerShell Scripts to executable so stay tuned).

## Installation
Git clone this repository, and read the comments on the code.

__Summary__: Clone -> Change the required parameters of both .ps1 -> Make different copies of base_template.ps1 with different things (ex: Set-Variable -Name john -Value ("aaaa"), so it has a different hash) -> run ps1 to exe and make them windows executables -> host the base_template.ps1 executables (python3 -m http.server 80) -> run your listener with netcat (nc -lvnp port, since you'll have multiple connexions in different ports you can use tmux) -> run the dropper_template.ps1 executable on the target

### notes

6 months ago more or less was not detected by Windows Defender, it might have changed, haven't had the opportunity to test it right now. In a near future I'll make a python program to make the setup easier.
