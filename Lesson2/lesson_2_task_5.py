def month_to_season(mesyac):
        if mesyac >12 or mesyac <1: print("Введите корректный номер месяца")
        elif mesyac > 2 and mesyac <6: print("Весна")
        elif mesyac > 5 and mesyac <9: print("Лето")
        elif mesyac > 8 and mesyac <12: print("Осень")
        else: print("Зима")

month_to_season(int(input("Введите номер месяца: ")))
