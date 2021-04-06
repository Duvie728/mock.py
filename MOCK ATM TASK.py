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

        selectedOption = int( input('Please select an option:'))

        print(selectedOption == 1)

        if(selectedOption ==1):
            print('you selected %s' % selectedOption)
          
        elif(selectedOption == 2):
            print('you selected %s' % selectedOption)
            
        elif(selectedOption == 3):
            print('you selected %s' % selectedOption)
            
        else:
            print('Invalid Option selected, please try again')
        
    else:
        print('Password Incorrect, please try again')

else:

    print('Name not found, please try again')
