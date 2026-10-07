for i in range(1,6):
    print(i)

total = 0

for i in range(1,11):
    total += i
    print(total)

num = 11

for i in range(1,11):
    print(f"{num} x {i} = {num * i}")


count = 1

while count < 5:
    print(count)
    count += 1

val = 7 

for i in range(1,11):
    print(i)
    if i == val:
        break

for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)




