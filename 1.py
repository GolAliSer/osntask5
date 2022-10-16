#задание 1(ср5) 
def A(n):#фунцкия перевода в двоиную систему для целых чисел
    s = ""
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s

def B(m):#функция перевода в восьмеричную систему для целых чисел
    d = ""
    while m > 0:
        d = str(m % 8) + d
        m //= 8
    return d

while True:
    try:
        x = int(input("Введите число: "))
        break
    except ValueError:#проверяем на ошибку ввода 
        print("Вы ввели не целое число. Попробуйте снова: ")

while True:
    try:
        sp = int(input("Введиет целевую систему счисления (2 или 8): "))
        if sp == 2 or sp == 8:#проверяем на правильный ввод
            break
        else:
            raise ValueError
    except ValueError:#проверяем на ошибку ввода
        print("Вы ввели что-то не так. Попробуйте снова: ")

if sp == 2:
    print("Вывод:", x, "->", A(x))
elif sp == 8:
    print("Вывод:", x, "->", B(x))
