def NatSum(N):
    """ Функция принимает целое число и находит сумму чисел кратных ТРЕМ или ПЯТИ """
    ret = 0  # переменная, хранимая в себе сумму

    for i in range(N):
        if i % 3 == 0 or i % 5 == 0:
            ret += 1
    return print(" NatSum = ", ret)


NatSum(1000)
