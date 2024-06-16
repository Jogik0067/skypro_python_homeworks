
def is_year_leap(yearV):
 if (yearV % 4 ==0): return True  
 else:return False
Year_V =int(input("Введите год:"))
print("Год: ", Year_V," : ",is_year_leap(Year_V))