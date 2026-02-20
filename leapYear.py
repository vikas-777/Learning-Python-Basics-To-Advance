year = int(input("Enter the year in yyyy format..."))
if year % 4 == 0 or year % 100 == 0 :
    print(f"{year} The given year is leap year")
else :
    print(f"{year} The given year is not leap year")