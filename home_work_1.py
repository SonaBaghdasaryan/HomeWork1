#Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = int(input('Enter the side length a : '))
b = int(input('Enter the side length b : '))
c = int(input('Enter the side length c : '))
if a + b <= c or a + c <= b or b + c <= a:
    print('The triangle does not exist')
elif a != b != c:
    print('Versatile Triangle (Разносторонний)')
elif a == b == c:
    print('Equilateral Triangle (Равносторонний)')
else:
    print('Isosceles Triangle (Равнобедренный)')