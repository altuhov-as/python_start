my_list = [7, 5, 3, 3, 2]
used_number = int(input("Введите число: "))
"""если число содержится в списке"""
if used_number in my_list:
    ind = 0
    if my_list.count(used_number) == 1:
        ind = my_list.index(used_number)
    else:
        for i in range(my_list.count(used_number)):
            ind = my_list.index(used_number, ind) + 1
        ind -= 1
    for i, v in enumerate(my_list):
        if i == ind:
            print(v, used_number, end=" ")
        else:
            print(v, end=" ")
else:
    """если число меньше последнего значения в списке"""
    if used_number < my_list[-1]:
        print(" ".join([str(x) for x in my_list]), used_number)
    else:
        for i in my_list:
            if used_number > i:
                print(used_number, i, end=" ")
                used_number *= 0
            else:
                print(i, end=" ")
print("")
print("Исходный не возрастающий набор натуральных чисел: ", my_list)
