# Email Slicer Program

#function to get email id
def get_email():
    email = input("Enter your email: ")
    email.strip()
    return email

#function to slice email id
def slice_email(email):
    # slice username and domain name using index slicing
    username = email[:email.index('@')]
    domain_name = email[email.index('@')+1:]
    return username, domain_name

#function to run the program and print sliced values
def main():
    email = get_email()
    username, domain_name = slice_email(email)
    print("Your Username is: ",username)
    print("Your Domain name is: ",domain_name)

#run main function
if __name__ == '__main__':
    main()