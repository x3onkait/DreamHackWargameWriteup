secret = [0xAD, 0xD8, 0xCB, 0xCB, 0x9D, 0x97, 0xCB, 0xC4, 0x92, 0xA1, 0xD2, 0xD7, 0xD2, 0xD6, 0xA8, 0xA5, 0xDC, 0xC7, 0xAD, 0xA3, 0xA1, 0x98, 0x4C, 0x0]

decryptSecret = [0 for i in range(len(secret))];

# 거꾸로 하나씩 역산하면서 flag를 구한다.
for _seq in range(len(secret) - 1, 0, -1):  
    decryptSecret[_seq - 1] = secret[_seq - 1] - decryptSecret[_seq];
    
# 플래그 출력하기
flag = "DH{" 
for _seq in range(len(decryptSecret) - 1):
    flag += f"{chr(decryptSecret[_seq])}"
    
flag += "}"

print(flag)
