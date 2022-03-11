# byte_140003000 데이터
byte_140003000 = [0x52, 0xDF, 0xB3, 0x60, 0xF1, 0x8B, 0x1C, 0xB5, 0x57, 0xD1, 0x9F, 0x38, 0x4B, 0x29, 0xD9, 0x26, 0x7F, 0xC9, 0xA3, 0xE9, 0x53, 0x18, 0x4F, 0xB8, 0x6A, 0xCB, 0x87, 0x58, 0x5B, 0x39, 0x1E]

# ROL 연산 코드 (https://hacking-ai.tistory.com/68)
def rol(x, n):
    shiftBit = x << n
    shiftBit &= 255
    carryBit = x >> 8 - n
    return shiftBit | carryBit

# Dreamhack FLAG 형식에 맞추기
print("flag is... ", end='')
print("DH{", end='')    

# i는 반복인자, 0x00부터 0x1F - 1까지 0x01씩 증가하며 반복됨
for _i in range(0x1F):
	# readable ASCII를 전부 만든 다음에 if문으로 검증을 실시해서, 조건이 맞으면 flag로 본다.
    for _charTry in range(33, 128):
        if(_i ^ rol(_charTry, _i & 7)) == byte_140003000[_i]:
        	# 조건이 맞았을 때 한 문자씩 이어서 출력
            print(chr(_charTry), end='')
            
print("}")
