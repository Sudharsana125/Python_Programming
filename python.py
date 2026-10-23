num = int(input("Enter a number: "))
total = 0
original = num
while num > 0:
    digit = num % 10
    total = total + digit ** 3
    num = num // 10
if original == total:
    print("amstrong")
else:
    print("not amstrong")


num = int(input("Enter a number: "))

total = 1

while num > 0:
    digit = num % 10
    total = total *  digit
    num = num // 10

print("Sum of digits:", total)


num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    num = num // 10
    reverse = reverse * 10 + digit

print("Reverse:", reverse)