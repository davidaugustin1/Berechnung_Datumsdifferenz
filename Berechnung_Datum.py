tag1=30
monat1=11
jahr1=1999
tag2=30
monat2= 12
jahr2=1999

def days_per_month(month, year):
    if month == 2 :
        return 28 + is_schaltjahr(year)
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    else: 
        return 30

def is_schaltjahr (year):
 if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
    return 1
 else: 
     return 0

def calc_difference(tag1, monat1, jahr1, tag2, monat2, jahr2):
    days = 0
    for i in range(monat1, 13):
        days += days_per_month(i, jahr1)
    days -= tag1
    if jahr1 == jahr2:
        for j in range(monat2, 13):
            days -= days_per_month(j, jahr2)
        days += tag2
    else:
        for j in range(jahr1 +1, jahr2 +1):
            days += 365 + is_schaltjahr(j)
        for k in range(monat2, 13):
            days -= days_per_month(k, jahr2)
        days += tag2
    return days
        

print(calc_difference(tag1, monat1, jahr1, tag2, monat2, jahr2))
