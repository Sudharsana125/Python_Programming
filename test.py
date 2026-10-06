rows = int(input("Enter number of rows: "))
i = rows
while i >= 1:
    j = 1
    while j <= i:
        print("*", end=" ")
        j = j + 1

    print()
    i = i - 1

n = int(input("Enter number: "))
i = 1
while i <= n:
    if i % 3 == 0:
        i = i + 1
        continue
    print(i)
    i += 1
num = int(input("Enter number: "))
total = 0
while num != 0:
    if num > 0:
        total += num
    num = int(input("Enter number: "))
print("Pos num ", total)

num = int(input("Enter number: "))
total = 0

while num != 0:
    total = total + num
    num = int(input("Enter number: "))

print(total)

n = int(input())
i = 0
while i <= n:
    print(i)
    i += 1

n = int(input())
i = 1
total = 0
while i <= n:
    if i % 2 == 0:
        total += i
    i = i + 1
print(total)

