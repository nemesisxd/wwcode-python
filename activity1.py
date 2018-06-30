bill = input('How much is your total bill? ')

payment = input('How much is your payment? ')

change = int(payment) - int(bill)
print('Hi! Your change is {}'.format(change))
