from datetime import date
today = date.today()
love = date(2022, 9, 28)
d_day = today - love + 1
print("영주야")
print(d_day.days, "일")
print("축하해")

