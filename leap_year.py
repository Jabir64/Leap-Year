def leap_year():
    year = int(input("ENTER THE YEAR: "))
    if (year % 4 == 0) and (year % 100 != 0):
        print(year, "IS LEAP YEAR")
    elif (year % 400 == 0) and (year % 100 == 0):
        print(year, "IS LEAP YEAR")
    else:
        print(year, "IS NOT LEAP YEAR")
leap_year()