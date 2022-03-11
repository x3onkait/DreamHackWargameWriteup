import base64

a = "XIv6wJm1SWE="              # IV (INITIALIZATION VECTOR)
b = "PxwKXGzpuQw="              # data..?!

print(f"a = {a} / b = {b}")

a_decode_base64 = base64.b64decode(a)           # ... IV
b_decode_base64 = base64.b64decode(b)           # ... data..?!

print(f"a > {a} --> {a_decode_base64} | len : {len(a_decode_base64)}")
print(f"a > {b} --> {b_decode_base64} | len : {len(b_decode_base64)}")

# REFER TO THE PKCS#7 padding
originalData = b"guest\x03\x03\x03"
modifiedData = b"admin\x03\x03\x03"

intermediary_value = []
modified_IV = []                # <--- change IV to fit as target, admin!

for _seq in range(0x08):
    intermediary_value.append(a_decode_base64[_seq] ^ originalData[_seq])

for _seq in range(0x08):
    modified_IV.append(intermediary_value[_seq] ^ modifiedData[_seq])

print(modified_IV)

print(f"{base64.b64encode(bytes(modified_IV))}")
