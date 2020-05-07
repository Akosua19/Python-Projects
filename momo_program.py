class MOMO:
    def __init__(self, name, balance, pin):
        self.name = name
        self.balance = balance
        self.pin = pin

    
    def get_balance(self):
        return self.balance

    def get__name(self):
        return self.name

    def get__pin(self):
        return self.pin


momo = {
      'number' : '0571971853',
      'pin' : 2020,
      'balance' : 50,
}



while True:

   p = int(input("\nEnter your momo pin: "))
   while p == 2020:
    print("\n1 - CashIn \n2 - Allow CashOut \n3 - Buy Airtime \n4 - Check Balance \n5 - Pay Utilities \n6 - Exit  ")
    choose= int(input("\nChoose your choice :"))


            # CASH IN

    if choose ==1:
        amt = float(input("\nEnter amount you wish to send: "))
        print("Successful !")


           # WITHDRAWAL

    if choose ==2:
        print(input("\nEnter amount you want to withdraw: "))
        withdraw = input("Do you want to withdraw more than that, Yes or No ? ")


          # BUY AIRTIME
   
    if choose ==3:
        print(input("\nEnter amount you want to buy: "))
        airtime = input("Select the payment options ; 1. Mobile Money 2. ATM ? ")
        
    if  airtime =="Mobile Money":
        print('Successfully Purchased ! ')


         # CHECK BALANCE

    if choose ==4:
         print('\nbalance:  ')



         # PAY UTILITIES


    elif choose ==5:
         print ('Pay Utilities')
         print(input("\nHow much do you want to pay? "))
         print('Done !')


         # EXIT

    elif choose ==6:
         print("\nTransaction is now complete.")
exit()
