class Bank() :
    def __init__(self,name,mojodi) :
        self.name = name
        self.mojodi = mojodi

    def __iadd__(self, x) :
        self.mojodi  += x.mojodi
        x.mojodi = 0 
        return self

    def __add__(self,x) :
        name = self.name + x.name
        mojodi = self.mojodi + x.mojodi
        temp = Bank(name,mojodi)
        return temp 
    
        

    def __str__(self) -> str:
        return f"the name of user is : {self.name} --- his mojodi is : {self.mojodi} "

    def __eq__(self, x) :
        if self.mojodi == x.mojodi :
            return True
        else :
            return False 
    def transfer (self,x,number) :
        if number >self.mojodi :
            print("your amount not enoph")
            return
        self.mojodi -= number 
        x.mojodi += number

    def diposit (self, number) :
        self.mojodi += number
    
    def withdraw (self ,number) :
        self.mojodi -= number
