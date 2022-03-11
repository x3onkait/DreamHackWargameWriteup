from pwn import *
from z3 import *

context.log_level = 'debug'

p = remote('host1.dreamhack.games', port = 15802)

# 문제풀기를 총 30회 반복...
for _gameRound in range(30):

    polynomialSolver = Solver()

    # 변수 준비
    a = Int('a')
    b = Int('b')
    c = Int('c')
    d = Int('d')

    polynomialSolver.add(a >= 100 , a <= 1000)
    polynomialSolver.add(b >= 100 , b <= 1000)
    polynomialSolver.add(c >= 100 , c <= 1000)
    polynomialSolver.add(d >= 100 , d <= 1000)

    print(f"{_gameRound + 1}th GAME. I'll show the power of Sayo's French Fries!") # :)
    p.recvuntil(b"th...")

    rawEquationsDump = p.recvuntil(b"Answer")

    equations = []

    for _splitted_equation in rawEquationsDump.split(b"\n"):
        if b"Answer" in _splitted_equation:
            # "Answer"는 수식이 아님!
            break
        _splitted_equation = _splitted_equation.replace(b"=",b"==")
        equations.append(_splitted_equation)

    del equations[0]            # 그냥 b'' 만 들어있음.

    # additional variables?
    if b"e" in equations[0]:
        e = Int('e')
        polynomialSolver.add(e >= 100 , e <= 1000)
    if b"f" in equations[0]:
        f = Int('f')
        polynomialSolver.add(f >= 100 , f <= 1000)
    if b"g" in equations[0]:
        g = Int('g')
        polynomialSolver.add(g >= 100 , g <= 1000)
    if b"h" in equations[0]:
        h = Int('h')
        polynomialSolver.add(h >= 100 , h <= 1000)

    for equation in equations:
        polynomialSolver.add(eval(equation))        # 문자열 그대로 넣으면 exception 뜸.

    polynomialSolver.check()         # 연립방정식의 해를 구할 수 있는지(sat) 확인한 후,

    solution = polynomialSolver.model()         # 연립방정식의 해를 구한다.
    print(solution)

    # 방정식의 해를 일단 추출해서 dictionary에 넣어준다.
    payloadDictionary = {}
    for d in solution.decls():
        # print(f"{d} {str(solution[d])}")
        payloadDictionary[str(d)] = str(solution[d])

    # 방정식의 해를 변수(variables) 이름 순서(a,b,c,d...) 순서대로 재정렬하여 다시 dictionary를 만든다.
    payloadDictionary = dict(sorted(payloadDictionary.items()))
    print(payloadDictionary)

    payload = ""
    for key, value in payloadDictionary.items():
        payload += str(value)
        payload += ","

    payload = payload.rstrip(',')
    print(payload)

    p.sendline(payload)

    polynomialSolver.reset()

# flag...?
data = p.recvline()
print(data)
