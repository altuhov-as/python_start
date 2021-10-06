num = int(input("Введите число: "))

max_num = -1
while num != 0:
    if max_num == 9:
        break
    d = num % 10
    num //= 10
    if d > max_num:
        max_num = d
print(max_num)
