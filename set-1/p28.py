#Write a program to identify if the year is Leap year or not
year=int(input("enter a year:"))
if (year %4==0 and year %100!=0)or(year % 400==0):
  print("year is leap year")
else:
  print("year is not a leap year")
