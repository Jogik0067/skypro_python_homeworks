def bank(y,x):
    for n in range(1, y+1): x=x+x*(0.1)

    return x        

YEARV=int(input("Введите срок вклада(в годах): "))
DENGI=float(input("Введите сумму вклада: "))
print("Сумма вклада за ", YEARV, " лет - ", float(bank(YEARV,DENGI)))            