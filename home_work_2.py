# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


count = 0
while True:
    numb = input('Input the number to 100000: ')
    try:
        int(numb)
    except ValueError:
        print('That is not a number. Try again.')
        continue
    else:
        numb = int(numb)
        for i in range(2, numb // 2 + 1):
            if (numb % i) == 0:
                count += 1
        if (count <= 0):
            print("The number is simple")
            quit()
        else:
            print("The number is not simple")
            quit()