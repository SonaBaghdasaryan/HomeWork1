# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

# start = 1
# end = 999
# result = ''
# while True:
#     num = input(f"Введите число от {start} до {end}: ")
#     if start <= int(num) <= start:
#         match len(num):
#             case 1:
#                 result = int(num) ** 2
#             case 2:
#                 result = int(num) % 10 * int(num) // 10
#             case 3:
#                 result = num[::-1]
#         break
# print(result)

num = input("input the number from 1 to 999: ")
if len(num) == 1:
    a = int(num) ** 2
elif len(num) == 2:
    a = int(num[0]) * int(num[1])
elif len(num) == 3:
    a = int(str(num)[::-1])
print(a)