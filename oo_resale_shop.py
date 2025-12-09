#from typing import Dict, Optional
from computer import Computer
inventory : list[Computer] = []
#Information we need for this file 

class ResaleShop: #Attributes & methods of a resale shop

    # What attributes will it need?
    inventory = [] #the inventory list of type array
    # itemID : int... this is not necessary in my opinion. 
    store_balance : int #This is not required, but an extra step I did

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)

    def __init__(self, sBalance:int):
        #self.itemID = item_id
        #you do not need the item id since each is defined as an object
        #item id wouldve been needed for procedural
        self.inventory = []
        self.store_balance = sBalance

    def buy(self, computer1:Computer):
        if computer1 in inventory:
            print ("This instance of this computer is already bought by the resale shop. Please try again.")
        else: 
            inventory.append(computer1)
            self.store_balance = self.store_balance + computer1.price
            print ("The computer cost", computer1.price)
            print ("The store balance is", self.store_balance)

    def sell(self, computer1:Computer):
        #sell_computer = computer1.computer_information()
        if computer1 in inventory:
            inventory.remove(computer1)
            self.store_balance = self.store_balance - computer1.price
            print ("The computer is worth", computer1.price)
            print (self.store_balance)
        else:
            print("This computer is NOT in the inventory and cannot be sold")

        
    def printInventory (self):
         for i in inventory:
             print(" ")
             print ("Information for this computer")
             print (" ")
             print(i.description)
             print (i.processor_type)
             print (i.hard_drive_capacity)
             print (i.memory)
             print(i.operating_system)
             print (i.year_made)
             print (i.price)

    #I concluded that I do not need this method since...
    #I can print the inventory directly from the 'main' procedure

    def refurbish (self, computer1:Computer):
        if computer1 in inventory:
            if int (computer1.year_made) < 2000:
                 computer1.price = 0 
                 # Any computer that is made in a year before 2000 is assigned a price of zero
            elif int(computer1.year_made) < 2012:
                 computer1.price = 250
                 # Any computer that is made between 2000-2012 is assigned a price of 250
            elif int(computer1.year_made) < 2018:
                 computer1.price = 550
                 # Any computer that is made between 2012-2018 is assigned a price of 550
            else:
                 computer1.price = 1000
                 # Any computer that is made after 2018 is assigned a price of 1000
        else:
            print ("This item is NOT in the resale shop inventory and CANNOT be refurbished")

def main():
    NewResaleShop : ResaleShop = ResaleShop (10000)
    NewComputer : Computer = Computer ("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",1024, 64,
        "macOS Big Sur", 2013, 1500)
    NewComputer2 : Computer = Computer ("OmniBook X",
        "3.5 GHc 6-Core Intel Xeon E5",1024, 32,
        "macOS Big Sur", 2020, 3000)
    
    NewResaleShop.buy(NewComputer)
    print (NewComputer.price)
    NewComputer.comp_price(400)
    print (NewComputer.price)
    NewResaleShop.buy(NewComputer)
    NewResaleShop.printInventory()
    NewResaleShop.sell(NewComputer2)
    NewResaleShop.refurbish(NewComputer2)
    NewResaleShop.refurbish(NewComputer)
    NewResaleShop.printInventory()
    print (NewComputer.price)
    
    #This main tests all of the possibilities.

main()

