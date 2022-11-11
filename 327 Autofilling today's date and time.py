#The 2 lines of code below mean the same
today = datetime.today()
today = datetime(year=2022, month=11, day=10)


print(today) #2022-11-11 16:38:15.214336

today_format_changed = today.strftime("%Y%m%d") #look into this: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
print(today_format_changed) #20221111

today_format_changed2 = today.strftime("%Y-%m%d")
print(today_format_changed2) #2022-1111

today_format_changed3 = today.strftime("%Y-%m**%d")
print(today_format_changed3) #2022-11**11

