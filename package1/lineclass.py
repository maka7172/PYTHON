class Linetwo :
    def __init__(self,x1,y1,x2,y2) -> None:
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def line_leght(self) :
        """this method return lengh of line """
        return (((self.y2 - self.y1)**2)+((self.x2 - self.x1)**2))**(1/2)
    
    def line_dip(self) :
        """this method return dip of line"""
        return ((self.y2 - self.y1) /(self.x2 - self.x1))
    # def __del__(self) :
    #     print( f"you try to delete instance of linetwo" )

    def __str__(self) :

        return f"this object is line whit points : a({self.x1},{self.y1}) , b({self.x2},{self.y2})"
    
    def line_whight(self) :
        raise NotImplementedError("this is polymorphism method")
    
#**********************************************************************
class Linethree(Linetwo):
    def __init__(self,x1,y1,x2,y2,x3,y3) -> None:
        super().__init__(x1,y1,x2,y2)
        self.x3 = x3
        self.y3 = y3

    def __str__(self) :

        return f"this object is line whit points : a({self.x1},{self.y1}) , b({self.x2},{self.y2} , c({self.x3},{self.y3}))"
    

    def line_lenghs (self) :
        """this method return lenghs : (x1,y1)-->(x2,y2) , (x2,y2)-->(x3,y3)"""
        return ((self.y2 - self.y1) /(self.x2 - self.x1)) , ((self.y3 - self.y2) /(self.x3 - self.x2))
    
    def line_whight(self) :
        """this method return sum of 3(x) """
        return self.x3 + self.x2 + self.x1
    
 #**********************************************************************   

if __name__ == '__main__' :
    line1 = Linetwo(4,2,8,6)
    print(line1.line_leght())
    print(line1.line_dip())
    # del line1 
    # print(line1)
    line2 = Linethree(8,8,9,9,12,12)
    print(line2.line_whight())
    

