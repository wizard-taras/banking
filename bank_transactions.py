## Additional modules importing
import random

## GENERATORS

#region
# Card number generator
#region
def card_number_generator():
    # Clearing a 'card_number' list to store new user's values
    card_number = [] # used for internal code references
    card_number_output = [] # used for printing out purposes
    # Populating a list with 16 digits (in a text form)
    while len(card_number) != 16:
        card_number.append(str(random.choice(range(0, 9, 1))))
    
    # Making a copy of a 'card_number' list that will be used for the output purposes
    card_number_output = card_number[:]
    # Separating every 4 digits with a blank space (for the output purposes only)
    for i in range(4, len(card_number), 5):
        card_number_output.insert(i, ' ')
    # Joining the characters of both lists into one string
    card_number_output = ''.join(card_number_output) # An example of a resulting string: '5750 7835 6158 7775' 
    card_number = ''.join(card_number) # An example of a resulting string: '5750783561587775' 

    # Return a tuple of the two lists
    return (card_number, card_number_output)
#endregion
#endregion

## DEFINING CONSTANTS
TRANSFER_LIMIT = 5000
TRANSFER_FEE = 0.05

## MAIN BODY
# Welcoming message
print("Hello! We welcome you in our bank")

# STEP 0. Creating a user account
#region

# Initializing a dictionary that holds an information about clients, such as:
clients = {}
clients_keys = ('full_name', 'age', 'tnn', 'payment_system', 'currency', 'card_balance', 'banking_plan')

# Client personal data input
#region
personal_data = input("Please, enter the client full name, age, TNN, desired payment system (Visa/Mastercard), "\
                      "currency option (UAH, USD, EUR, DEM) and card balance (all of the values must be separated by comma): ")
banking_plan = input("Please select the desired banking plan: \n\t1: Blue collar \n\t2: Pro \n\t3: Rockefeller\n")

# Making a list personal data of values (full name, age, TNN, and card balance) that will be stored in the 'clients' dict
banking_plan_map = {'1': 'Blue collar', '2': 'Pro', '3': 'Rockefeller'}
# Concatenating personal data list and banking plan option
client_data_values = personal_data.split(',') + [banking_plan_map.get(banking_plan)]
# Assigning values to the respective keys of the 'clients' dict
for key, value in zip(clients_keys, client_data_values):
    clients[key] = str(value).strip()
#endregion

# STEP 1. Defining a dict of available operations
operations = {'money_transfer': 'Money transfer',
              'phone_topup': 'Phone top-up',
              'deposit': 'Open/Calculate a deposit',
              'loan': 'Open/Calculate a loan',
              'insurance': 'Pay for an insurance'
              }


# TRANSACTIONS
print("\nPlease choose yourself from the next list and the recepient (one digit for sender, one for receiver):")
iter = 1
for k, v in clients.items():
    print("\nThe client {number}: {cli_name} has {balance} UAH on his account".format(
        number=iter, cli_name=k, balance=v))
    iter += 1

sender = int(input('\nSender: '))
sender_balance = int(clients[list(clients.keys())[sender-1]])
receiver = int(input('Receiver: '))
receiver_balance = int(clients[list(clients.keys())[receiver-1]])

money_transfer = int(input(f"\nNext, enter the amount of money you want to transfer " \
      "(limit per transaction is 5000 UAH, your balance is " \
      f"{sender_balance} UAH): "))

if sender_balance >= money_transfer <= TRANSFER_LIMIT:
    fee_paym = input("Who is going to pay the transfer fee?" \
                    "\nSender: type 's', Receiver: type 'r': ")
    if fee_paym == 's':
        sender_balance -= money_transfer*(1 + TRANSFER_FEE)
        receiver_balance += money_transfer
        print("Transaction is successful!" \
            "\n\tThe amount of money withdrawn from your account is " \
            f"{money_transfer} and your current balance is {sender_balance} UAH." \
            f"\n\tThe receiver's current balance is: {receiver_balance} UAH. ")
    elif fee_paym == 'r':
        receiver_balance += money_transfer*(1 - TRANSFER_FEE)
        sender_balance -= money_transfer
        print("Transaction is successful!"\
            "\n\tCurrent receiver's balance is: {rec_bal} UAH. \n\tYour current balance is: {send_bal} UAH.".format(
            rec_bal=receiver_balance, send_bal=sender_balance))
elif sender_balance < money_transfer:
    print("Unfortunately, you don't have enough funds to transfer the desired amount of money.")