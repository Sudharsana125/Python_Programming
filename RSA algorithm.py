import math
p = 17
q = 11

n = p * q
phi = (p - 1) * (q - 1)

e = 7

d = pow(e, -1, phi)

message = 65

cipher = pow(message, e, n)

decrypted = pow(cipher, d, n)

print("Public Key:", (e, n))
print("Private Key:", (d, n))
print("Original Message:", message)
print("Encrypted Message:", cipher)
print("Decrypted Message:", decrypted)