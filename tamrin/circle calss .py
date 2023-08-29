import os
os.system('cls')
class Circle :
    
    def __init__(self,radiyan):
        self.radiyan = radiyan
        self.p = 3.14
    def mohit_circle (self) :
        return f'the mohit of circle is : {2*self.p*self.radiyan} '
    def masahat_circle (self) :
        return f'the masahat of circle is : {2*self.p*(self.radiyan **2)}'
    
radiyan = int(input("enter your radiyan of circle"))
circle1 = Circle(radiyan)
print(circle1.mohit_circle())  
print(circle1.masahat_circle()) 
        