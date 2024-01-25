import calendar

god = int(input("Введiть рiк: "))
mesac = int(input("Введiть мiсяць (число вiд 1 до 12): "))

calc = calendar.monthcalendar(god, mesac)

print(f"{'-'*10}\n{calendar.month_name[mesac]} {god}\n{'-'*10}\nПн Вт Ср Чт Пт Сб Нд")

for week in calc:
    for day in week:
        if day == 0:
            print("  ", end=" ")
        else:
            print(f"{day:2d}", end=" ")
    print()