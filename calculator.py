from decimal import Decimal

def calculate_mortgage(principal, years, rate):
    r = rate / 100 / 12
    n = years * 12
    monthly_payment = principal * r / (1 - (1 + r) ** -n)
    return monthly_payment

def calculate_total(principal, years, rate):
    monthly_payment = calculate_mortgage(principal, years, rate)
    total_payment = monthly_payment * years * 12
    return total_payment

def payment_schedule(principal, years, rate):
    r = rate / 100 / 12
    n = years * 12
    monthly_payment = calculate_mortgage(principal, years, rate)
    remaining_balance = principal
    schedule = []
    for i in range(1, n + 1):
        interest = remaining_balance * r
        principal_paid = monthly_payment - interest
        remaining_balance -= principal_paid
        schedule.append((i, monthly_payment, interest, principal_paid, remaining_balance))
    return schedule