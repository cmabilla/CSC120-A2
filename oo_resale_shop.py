from typing import Dict, Optional
inventory : list = []
from computer import Computer
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
        buy_computer = computer1.computer_information()
        inventory.append(buy_computer)
        self.store_balance = self.store_balance + computer1.price
        print ("The computer cost", computer1.price)
        print (self.store_balance)

    def sell(self, computer1:Computer):
        sell_computer = computer1.computer_information()
        inventory.remove(sell_computer)
        self.store_balance = self.store_balance - computer1.price
        print ("The computer is worth", computer1.price)
        print (self.store_balance)
        
    # def printInventory (self):
    #     print (inventory)
    #I concluded that I do not need this method since...
    #I can print the inventory directly from the 'main' procedure

    def refurbish (self, computer1:Computer):
        if computer1.computer_information is not None:
            if int (computer1.year_made) < 2000:
                 computer1.price = 0 
                 #
            elif int(computer1.year_made) < 2012:
                 computer1.price = 250
                 #
            elif int(computer1.year_made) < 2018:
                 computer1.price = 550
            else:
                 computer1.price = 1000
        else:
            print ("There is no item to refurbish")

def main():
    NewResaleShop : ResaleShop = ResaleShop (567, 10000)
    NewComputer : Computer = Computer ("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",1024, 64,
        "macOS Big Sur", 2013, 1500)
    
    NewResaleShop.buy(NewComputer)
    print (inventory)
    NewResaleShop.sell(NewComputer)
    print (inventory)
    NewResaleShop.refurbish(NewComputer)
    print (NewComputer.price)

main ()