class Computer: #DEFINING a computer object and all of its attributes & methods 

    description : str #Computer description of type string
    processor_type : str # computer processor type of type string
    hard_drive_capacity : int # computer hard drive capacity of type integer
    memory: int # computer memory of type integer
    operating_system: str # computer operating system of type string
    year_made : int # computer year made of type integer
    price: int # computer price of type integer

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description:str, processorType:str, capacity:int, memory:int, OS:str, yearMade:int, amount:int):
        #pass... You'll remove this when you fill out your constructor
        self.description = description
        self.processor_type = processorType
        self.hard_drive_capacity = capacity
        self.memory = memory
        self.operating_system = OS
        self.year_made = yearMade
        self.price = amount
        
    # What methods will you need?
    def comp_price(self, new_price:int):
        self.price = new_price
        #This will set a new price to the computer

    def comp_OS (self, new_OS:str):
        self.operating_system = new_OS
        #This will update a new OS

    def computer_information(self):
            word1 = str(self.description)
            word2 = str(self.processor_type)
            word3 = str(self.hard_drive_capacity)
            word4 = str(self.memory)
            word5 = str(self.operating_system)
            word6 = str(self.year_made)
            word7 = str(self.price)
            total_description = word1+" "+word2+" "+word3+" "+word4+""+word5+" "+word6+""+word7
            #an innefficient way to put the computer information in inventory, but it works
            return total_description


def main ():
    NewComputer: Computer = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",1024, 64,
        "macOS Big Sur", 2013, 1500)
    
    #Below is code to test out the methods in this file. They all work.
    print (NewComputer.price)
    NewComputer.comp_price(400)
    print (NewComputer.price)
    print (NewComputer.computer_information())
    
main ()
 
