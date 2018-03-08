"""
iterate over 12 months
"""
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# minimum monthly payment
# Math
b12 = balance * (1 - monthlyPaymentRate)**12 * (1 + annualInterestRate/12)**12
print("Remaining balance: ", round(b12, 2))

# Logic
for m in range(12):
    mininumb = balance * monthlyPaymentRate
    unpaidBalance = balance - mininumb
    balance = unpaidBalance + annualInterestRate/12 * unpaidBalance
    print("Month", m+1, "Remaining balance:", round(balance, 2))
print("Remaining balance: ", round(balance, 2))

# the minimum fixed monthly payment
balance = 4773
annualInterestRate = 0.2
#fixedPayment = 10
#for m in range(12):
#    unpaidBalance = balance - fixedPayment
#    interest = annualInterestRate/12.0 * unpaidBalance
#    balance = unpaidBalance + interest
#    print("fixed payment", fixedPayment, "balance", balance)
fixedPayment = 10
while True:
    upBalance = balance
    for m in range(12):
        unpaidBalance = upBalance - fixedPayment
        interest = annualInterestRate/12.0 * unpaidBalance
        upBalance = unpaidBalance + interest
    # if upBalance <= 0:
    #     print("Lowest Payment:", fixedPayment)
    #     break
    # else:
    #     fixedPayment += 10
    if upBalance > 0:
       fixedPayment += 10
    else:
       break
print("Lowest Payment:", fixedPayment)

# Bisection search
epsilon = -0.01
lower = balance / 12
upper = (balance * (1 + annualInterestRate/12)**12) / 12
fixedPayment = (lower + upper) / 2

while True:
    upBalance = balance
    for m in range(12):
        unpaidBalance = upBalance - fixedPayment
        interest = annualInterestRate/12.0 * unpaidBalance
        upBalance = unpaidBalance + interest

    if upBalance <= 0 and upBalance > epsilon:
        break
    else:
        if upBalance > 0:
            lower = fixedPayment
        else:
            upper = fixedPayment
        fixedPayment = (lower + upper) / 2
