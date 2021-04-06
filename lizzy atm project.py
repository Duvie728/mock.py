name = input("What is your name?\n")
allowedUsers = ['Elizabeth','Mike','Love']
allowedPassword = ['passwordElizabeth','passwordMike','passwordLove']

if(name in allowedUsers):
    password = input("Your password?\n")
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
        
        print('Welcome %s' % name)
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int( input('Please select an option:\n'))


        if(selectedOption ==1):
            WithdrawalAmount = input('How Much do you want to withdraw?\n')
            allowedAmount = ['100','500','1000','5000']
            
        if(withdrwalAmount == allowedAmount):
            crossCheckedAmount = input('Are You Sure?\n')
            response = ['ýes,No']
            print('Withdrawal Successful')

        else:
            

          
        elif(selectedOption == 2):
            print('amount for deposit %s' % selectedOption)
            
        elif(selectedOption == 3):
            print('type of complaint %s' % selectedOption)


    else:
            print('Invalid Option selected, please try again')
        
    else:
        print('Password Incorrect, please try again')

else:

    print('Name not found, please try again')
