Взаимодействие с другими людьми#Задача 1
print('Введите число А')
a = int(input())
print('Введите число В')
b = int(input())
if a<b:
  for i in range(a, b):
    print(i)
elif a>b:
  for i in range(b, a):
    print(i)
else:
   print('Числа равны между собой')
