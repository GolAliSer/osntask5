#задание 1(ср5) 
def A(n):#функция перевода в двоичную систему
    n1 = int(n)
    if "." in str(n):
        n2 = float("0" + "." + str(n).split(".")[-1])
    s1 = ""
    s2 = ""
    while n1 > 0:#перевод целой части числа
        s1 = str(n1 % 2) + s1
        n1 //= 2
    if n2 != 0:#перевод дробной части числа
        while n2 != 1 and len(s2) < 10:
            n2 = n2 * 2
            if n2 >= 1:
                s2 = s2 + "1"
                n2 = n2 - int(n2)
            else:
                s2 = s2 + "0"
        s2 = "." + s2
    return s1 + s2 + "₂"

def B(n):#функция перевода в восьмеричную систему
    n1 = int(n)
    if "." in str(n):
        n2 = float("0" + "." + str(n).split(".")[-1])
    s1 = ""
    s2 = ""
    while n1 > 0:#перевод целой части числа
        s1 = str(n1 % 8) + s1
        n1 //= 8
    if n2 != 0:#перевод дробной части числа
        while n2 != 8 and len(s2) < 10:
            n2 = n2 * 8
            if n2 >= 1:
                s2 = s2 + str(int(n2))
                n2 = n2 - int(n2)
            else:
                s2 = s2 + "0"
        s2 = "." + s2
    return s1 + s2 + "₈"

while True:
    try:
        x = float(input("Введите число: "))
        break
    except ValueError:#проверяем на ошибку ввода 
        print("Вы ввели число. Попробуйте снова: ")

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
    print("Вывод: ", x, "₁₀", " -> ", A(x), sep="")
elif sp == 8:
    print("Вывод: ", x, "₁₀", " -> ", B(x), sep="")
