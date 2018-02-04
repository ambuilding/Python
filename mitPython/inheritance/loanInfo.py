# calculating payment
def _calculate_payment(principle, interest_rate_per_year, duration):
    if interest_rate_per_year==0:
        return principle/(duration*12)

    r=interest_rate_per_year/100/12
    n=duration*12

    montly_payment=principle*(r*((1.0+r)**n))/(((1.0+r)**n)-1)
    return montly_payment

# calculating remaining balance
def _calculate_balance(principle, interest_rate_per_year, duration, number_of_payments):
    if interest_rate_per_year==0:
        return principle-number_of_payments*(principle/(duration*12.0) )

    r=interest_rate_per_year/100/12.0
    n=duration*12

    balance=principle*((1.0+r)**n - (1.0+r)**number_of_payments) / (((1.0+r)**n)-1)
    return balance

# main program
principle=float(input("Enter loan amount: "))
annual_interest_rate=float(input("Enter annual interest rate (percent): "))
duration=int(input("Enter loan duration in years: "))

monthly_payment=_calculate_payment(principle, annual_interest_rate, duration)
print('LOAN AMOUNT:',principle,'INTEREST RATE (PERCENT):', annual_interest_rate)
print('DURATION (YEARS):',duration,'MONTHLY PAYMENT:',int(monthly_payment))

for year_number in range(1,1+duration):
    y=_calculate_balance(principle, annual_interest_rate, duration, year_number*12)
    print('YEAR:', year_number, 'BALANCE:', int(y), 'TOTAL PAYMENT', int(monthly_payment*year_number*12))
