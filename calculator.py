from decimal import Decimal
from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_mortgage(principal, years, rate):
    r = rate / 100 / 12
    n = years * 12
    monthly_payment = principal * r / (1 - (1 + r) ** -n)
    return monthly_payment

def calculate_total(principal, years, rate):
    monthly_payment = calculate_mortgage(principal, years, rate)
    total_payment = monthly_payment * years * 12
    return total_payment

def create_calendar(number_of_payments, starting_date=datetime.now()):
    calendar = []
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

print_payment_schedule(payment_schedule(100000, 10, 5))