a = "XIv6wJm1SWE="              # IV (INITIALIZATION VECTOR)
b = "PxwKXGzpuQw="              # data..?!

print(f"a = {a} / b = {b}")

a_decode_base64 = base64.b64decode(a)           # ... IV
b_decode_base64 = base64.b64decode(b)           # ... data..?!

print(f"a > {a} --> {a_decode_base64} | len : {len(a_decode_base64)}")
print(f"a > {b} --> {b_decode_base64} | len : {len(b_decode_base64)}")
