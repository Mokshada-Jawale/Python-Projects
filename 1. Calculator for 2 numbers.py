#Calcualtor for 2 numbers

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def calculator():
    want_to_start = input("Would you want to make calculations? Enter(Yes/No): ")
    while want_to_start.capitalize() == "Yes":
        print("Which Operation you want to perform? \n"
              "1. Addition \n"
              "2. Subtraction \n"
              "3. Multiplication \n"
              "4. Division")
        operation = input("Enter choice (1/2/3/4): ")
        if operation in ("1","2","3","4"):
            first_num = int(input("Enter First Number: "))
            second_num = int(input("Enter Second Number: "))

            if operation == "1":
                print(first_num,"+",second_num,"=",add(first_num,second_num))
            elif operation == "2":
                print(first_num, "-", second_num, "=", subtract(first_num, second_num))
            elif operation == "3":
                print(first_num, "*", second_num, "=", multiply(first_num, second_num))
            elif operation == "4":
                print(first_num, "/", second_num, "=", divide(first_num, second_num))

            print("Do you want to continue with next calculation?")
            want_to_continue = input("Enter (Yes/No): ")
            if want_to_continue.capitalize() == "No":
                print("That's cool, Have a good one!")
                break
        else:
            print("Invalid input, Please try again!")

    if want_to_start.capitalize() == "No":
        print("That's cool, Have a good one!")

if __name__ == "__main__":
    calculator()


