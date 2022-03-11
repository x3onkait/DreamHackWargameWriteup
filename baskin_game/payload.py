from pwn import *

context.log_level = 'debug'

p = remote("host1.dreamhack.games", 22708)

p.recvuntil(b'Good luck~\n\n\n\n')


for _gamePlayTime in range(0, 31):

    # N과 COUNT값 가져오기
    N_COUNT_DUMMY = p.recvline()
    N_COUNT_DUMMY = N_COUNT_DUMMY.split()
    N = int(N_COUNT_DUMMY[2][:-1])
    COUNT = int(N_COUNT_DUMMY[5])
    print(f"N : {N} / COUNT : {COUNT}")

    # 필승(!) 수열을 만들어 게임을 무조건 이기게 만들기(!)
    _num = (N - 1) % (COUNT + 1)

    mustWinNumericProgression = [1]
    while _num < N:
        mustWinNumericProgression.append(_num)
        _num += (COUNT + 1)
    print(mustWinNumericProgression)

    p.recvuntil(b'input your name -> ')
    print("Got new game!")
    p.sendline(b'SYFF')         # 놀랍게도 사용자 이름의 입력값이 "짝수"(글자)이면 내가 먼저 숫자를 말한다
    print(f"SayoFrenchFries now tries game number {_gamePlayTime + 1} of 31! I will show the power of Sayo's french fries!") # :)

    _gameRoundMaximum = len(mustWinNumericProgression) - 1
    for _gameRound in range(_gameRoundMaximum):

        # payloadList = []
        payloadString = b""

        # 나 먼저 값을 먹는다
        p.recvuntil(b'input your number -> ')

		# 이 미묘한 차이를 제대로 신경써주지 않았더니 컴퓨터가 낸 숫자와 내가 낸 숫자가 겹쳐서 에러가 났다.
        if _gameRound == 0:
            for _seq in range(mustWinNumericProgression[_gameRound], mustWinNumericProgression[_gameRound + 1] + 1):
                payloadString += str(_seq).encode()
                payloadString += " ".encode()
        else:
            for _seq in range(computerSaidLastly + 1, mustWinNumericProgression[_gameRound + 1] + 1):
                payloadString += str(_seq).encode()
                payloadString += " ".encode()

        print(f"GAME ROUND : {_gameRound + 1} / {_gameRoundMaximum} | GAME PAYLOAD : {payloadString}")

        p.sendline(payloadString)
        print(int(payloadString.split()[-1]))

        p.recvuntil(b'user say -> ')
        data = p.recvline()

		# 한 판을 이기면 기존과 다르게 "user win!\n" 문자열이 한 줄 더 나와서 중간에 흐름을 중지시켜 이걸 확인한 후 이긴 것이 확실하면 바로 다음 라운드로 넘어가야 한다.
        if _gameRound == _gameRoundMaximum - 1:
            data = p.recvline()
            if b"win" in data:
                print("break.")
                break

        p.recvuntil(b'computer say -> ')
        computerSaid = p.recvuntil('\n')

        print(f"computer said : {computerSaid}")
        computerSaidLastly = int(computerSaid.decode().split()[-1].replace(" ",""))
        print(f"computer said lastly : {computerSaidLastly}")

data = p.recvline()
print(f"result : {data}")
