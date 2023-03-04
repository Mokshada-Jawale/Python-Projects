# Program to check if year is Leap year or not

#Function to get a year
def get_year():
    year = int(input('Enter a year: '))
    return year

#Function to check if given year is leap year or not
def is_leap_year(year):
    if year%4 == 0 and (year%100 != 0 or year%400 == 0):
        return True
    else:
        return False

#Function to run the program and print leap year
def main():
    year = get_year()
    if is_leap_year(year):
        print(year,'is a leap year')
    else:
        print(year,'is not a leap year')

if __name__ == '__main__':
    main()


