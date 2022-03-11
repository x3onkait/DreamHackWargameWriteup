from Crypto.PublicKey import RSA


f = open("C:/Users/lksha/Downloads/aaa.pem", "r")

key = RSA.importKey(f.read())

print("key.n = {}".format(key.n))
print()
print("key.e = {}".format(key.e))
