print('Введите 4-значное число')
a = int(input())
print('Введите второе 4-значное число')
b = int(input())
if (a>b):
  for i in range(a,b+1):
    if ((i // 1000) == (i % 10)) and (((i // 100) % 10) == ((i % 100) // 10)):
      print(i)
