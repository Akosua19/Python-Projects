class ATM:
    def _init_(self, name, balance, pin):
        self.name = name
        self.__balance = balance
        self.__pin = pin

    def withdraw(self, amount):
        self.__balance -= amount



    def get__balance(self):
        return self.__balance

    def get__name(self):
        return self.__name

    def get__pin(self):
        return self.__pin




account = {
    'name' :'Rashida' ,
    'pin' : 1000 ,
    'balance' : 400
}


message = {

"""    
          **********************************************************
             ################################################

                Welcome to An ATM Program created by CURFUL 

                      
            ##################################################
           *********************************************************
        """




        '''
        
============= SELECTION =================



        A . DEPOSIT
        B . WITHDRAW
        C . CHECK BALANCE
        D . EXIT
        
    +++++++++++++++++++++++++++++++
        
        
        '''
          }

while True:

    y = int(input("\nEnter pin number: "))
    while y < 1000 or y > 9999:
        y = int(input("\nWrong Id.. re- enter: "))

    while True:
        print("\n1 - Deposit \n2 - Withdraw \n3 - Check Balance \n4 - Exit")
        selection = int(input("\nEnter your selection :"))

        #deposit


        if selection ==1:
            amt = float(input("\nEnter amount you want to deposit: "))
            deposit = input("Do you wish to make changes , Yes, No ? ")


            if deposit == "yes":
                print("\nUpdated Balance: 400")




        #withdrawal


        elif selection ==2:
            amt = float(input("\nEnter amount you want to withdraw: "))
            withdraw = input("Do you want to keep this , Yes , or No ? ")

            if withdraw == "Yes" :
                print("Withdrawal Verified !")

            else:
                print("\nyour balance is lesser than the amount you want to withdraw")
                print("\nMake a deposit")

                break

        #check Balance


        elif selection ==3:
               print('balance:  ')


        else:
            


         if selection ==4:
            print("\nTransaction is now complete.")
            
            exit()
           
        if selection ==6:
            print("\nEnter your selection again : ")
