##Напишите программу, которая запрашивает год и проверяет его на високосность.
##Распишите все возможные проверки в цепочке elif
##Откажитесь от магических чисел
##Обязательно учтите год ввода Григорианского календаря
##В коде должны быть один input и один print

check_1 = 4
check_2 = 100
check_3 = 400
start_year = 1582
result = ''
year = int(input('Input the year: '))
if year < start_year:
    result = 'You may have entered incorrect date'
elif year % check_1:
    result = 'Normal'
elif not year % check_2:
    if not year % check_3:
        result = 'Viscous'
    else:
        result = 'Normal'
else:
    result = 'Viscous'
print(result)
