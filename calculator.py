from decimal import Decimal
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time

standard_rate = 10

def calculate_mortgage(principal, years, rate):
    r = rate / 100 / 12
    n = years * 12
    monthly_payment = principal * r / (1 - (1 + r) ** -n)
    return monthly_payment

def calculate_total(principal, years, rate):
    monthly_payment = calculate_mortgage(principal, years, rate)
    total_payment = monthly_payment * years * 12
    return total_payment

def create_calendar(number_of_payments):
    calendar = []
    starting_date = datetime.now()
    for i in range(number_of_payments):
        calendar.append((starting_date + relativedelta(months=i+1)).strftime("%b, %Y"))
    return calendar

def payment_schedule(principal, years, rate):
    r = rate / 100 / 12
    n = years * 12
    monthly_payment = calculate_mortgage(principal, years, rate)
    remaining_balance = principal
    schedule = []
    months_to_append = create_calendar(n)
    for i in range(1, n + 1):
        interest = remaining_balance * r
        principal_paid = monthly_payment - interest
        remaining_balance -= principal_paid
        if remaining_balance < 0:
            remaining_balance = 0
        else:
            remaining_balance = remaining_balance
        schedule.append((i, months_to_append[i-1], monthly_payment, interest, principal_paid, remaining_balance))
    return schedule

def print_payment_schedule(schedule):
    print("Payment schedule:")
    print("№\tDate\t\tPayment\t\tInterest\tPrincipal\tRemaining balance")
    
    for payment in schedule:
        print("%d\t%s\t%.2f\t\t%.2f\t\t%.2f\t\t%.2f" % payment)

#print_payment_schedule(payment_schedule(100000, 10, 5))

def input_personal_info():
    while True:
        first_name=input("What is your first name? ")
        if first_name.isalpha():
            break
        else:
            print("Please enter a valid name. We don't accept numbers or special characters.")
            continue
    while True:
        last_name=input("What is your last name? ")
        if last_name.isalpha():
            break
        else:
            print("Please enter a valid name. We don't accept numbers or special characters.")
            continue
    while True:
        email=input("What is your email address? ")
        if "@" in email and "." in email:
            break
        else:
            print("Please enter a valid email address.")
            continue
    print("Ok, thank you for providing your personal information. I think we are ready to discuss the loan.")
    return first_name, last_name, email

def input_principal():
    while True:
        principal = input("What is the loan amount you'd like to borrow? Please enter a number: ")
        try:
            principal = int(principal)
        except ValueError:
            print("Please enter a valid number. We don't accept letters or special characters.")
            continue
        if principal < 0:
            print("Please enter a positive number")
            continue
        if principal < 5000:
            print("I don't think you can buy a house with that amount. Please enter a higher number.")
            continue
        if principal > 1000000:
            print("""That's a lot of money! I hope you undestand that we can't lend you that amount. \nPlease enter a number between 5000 and 1000000.""")
            continue
        return principal

def get_yes_or_no():
    while True:
        answer = input("Please enter 'yes' or 'no': ")
        if answer == "yes" or answer == "no":
            break
#Do i need these lines?
        # else:
        #     print("Please enter 'yes' or 'no'.")
        #     continue
    return answer

def input_loan_parameters():
    while True:
        years = input("How many years do you plan to pay off the loan? Please enter a number between 1 and 40: ")
        try:
            years = int(years)
        except ValueError:
            print("Please enter a valid number. We don't accept letters or special characters.")
            continue
        if years < 2:
            print("Please enter a positive number bigger than 1.")
            continue
        if years > 40:
            print("I'm sorry, but we don't offer loans for more than 40 years. Please enter a number between 1 and 30.")
            continue
        break
    while True:
        special_conditions = input("Are you eligible for any special conditions? (yes/no) ")
        if special_conditions == "yes":
            rate = standard_rate - 2
            break
        elif special_conditions == "no":
            rate = standard_rate
            break
        else:
            print("Please enter 'yes' or 'no'.")
            continue
    print("Ok, thank you for answering our questions. I think we are ready to calculate your mortgage. It make take a moment.")
    return years, rate

print("Welcome to our Bank! I understand that you are interested in taking a loan. Is that correct? (yes/no)")
first_answer = get_yes_or_no()
if first_answer == "no":
    print("Ok, have a nice day! Come back when you are ready to take a loan.")
    exit()
print("Let's start by getting to know you better.")
first_name, last_name, email = input_personal_info()
principal = input_principal()
years, rate = input_loan_parameters()
monthly_payment = calculate_mortgage(principal, years, rate)
time.sleep(3)
print("""So here are the details of your loan:
      First name: %s
      Last name: %s
      Email: %s
      Loan amount: %.2f
      Loan term: %d years
      Interest rate: %.2f
      Monthly payment: %.2f""" % (first_name, last_name, email, principal, years, rate, monthly_payment))
print("Would you like to see the payment schedule?")  
second_answer = get_yes_or_no()
if second_answer == "yes":
    print("Ok, here is the payment schedule:")
    print_payment_schedule(payment_schedule(principal, years, rate))
    print("Thank you for using our service. Have a great day!")
else:
    print("Thank you for using our service. Have a great day!")