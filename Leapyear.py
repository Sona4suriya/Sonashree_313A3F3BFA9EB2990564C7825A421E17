# Write a program that determines whether a year entered by user is leap year or not by using if-elif-else statement
year = int(input("Enter a year: "))


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
