name = input("What is your name?\n")
allowedUsers = ['Elizabeth','Mike','Love']
allowedPassword = ['pElizabeth','pMike','pLove']


if(name in allowedUsers):
    password = input("Your password?\n")
    userId = allowedUsers.index(name)

else:
    print('Name not found, please try again')
    

    
if(password == allowedPassword[userId]):
        
        print('Welcome %s' % name)
else:
    print:('password incorrect, please try again')
    
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')

    selectedOption = int( input('Please select an option:\n'))

    if(selectedOption ==1):
        withdrawalAmount = input('How Much do you want to withdraw?\n')
    allowedAmount = ['100','500','1000','5000']
            
            
    if(WithdrawalAmount in allowedAmount):
        crosscheckedAmount =input('confirm withdrawal?\n')
    amount = allowedAmount.index(WithdrawalAmount)

    reponse =('yes','no')

    print('Withdrawal Successful')
                                    
        
    else:
        print('insufficient Funds, please try again')


else:
    print('Invalid Option selected, please try again')

     



