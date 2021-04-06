print("ZURI BANK ATM")


name = input("Enter Account name\n")
allowedUsers = ['Duvie','Lizzy','Tonye']
allowedPassword = ['pDuvie','pLizzy','pTonye']

if(name in allowedUsers):
    password = input("Enter Your password?\n")
    userId = allowedUsers.index(name)
    

    if(password  == allowedPassword[userId]):
        print('Welcome %s' % name)
        from datetime import datetime
        now = datetime.now()
        date = now.strftime("%x")
        time = now.strftime("%I:%M %p")
        print("Date: {} , {}".format(date,time))
        print(' Available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')
        
        selectedOption = int( input('Please select an option:\n'))

        if(selectedOption == 1):
            WithdrawalAmount = input('How Much do you want to withdraw?\n')
            allowedAmount = ['500','1000','2000']
            amount = allowedAmount.index(WithdrawalAmount)
            print("Take your cash")
            
        if(WithdrawalAmount in allowedAmount):
            crosscheckedAmount =input('confirm withdrawal?\n')
            amount = allowedAmount.index(WithdrawalAmount)

            reponse =('yes','no')

            print('Withdrawal Successful')

        if(selectedOption == 2):
            DepositAmount = input('How Much would you like to deposit?\n')
            balance = 10,000
            print('Current Balance')

        if(selectedOption == 3):
            Issue = input('What issue will you like to report?\n')
            print("your issue is currently been resolved")
            print("Thank you for contacting us")
                          
                                    
        
        else:
            print('insufficient Funds, please try again')

##            else:
##                print('Inavlid Option selected, please try again')
##            
##            if(WithdrawalAmount in allowedAmount):
               
                
##            elif(
##                
                        

               
                               
            

    else:
        print('Passsword Incorrect, please try again')

else:

    print('Name not found, please try again')
                   













