import random

class MyFor:
    def ForN(n):
        if(n<0):
            return
        print("Перебираем числа от 1 до " + str(n) + " :")
        for i in range(0, n):
            print("    i = " + str(i) + ", случайное число это " + str(random.randint(-i, i)))

if __name__ == "__main__":
    MyFor.ForN(int(input("Введите число (больше 1) n = ")))