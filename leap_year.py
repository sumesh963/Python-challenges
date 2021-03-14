import calendar
y=int(input())
if y in range(1900,pow(10,5)):
    if (calendar.isleap(year=y)==True):
        print("True")
    else:
        print("False")