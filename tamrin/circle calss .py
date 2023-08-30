import os
os.system('cls')
class Circle :
    pi = 3.14
    def __init__(self,radiyan):
        self.radiyan = radiyan
        
    def mohit_circle (self) :
        return f'the mohit of circle is : {2*Circle.pi*self.radiyan} '
    def masahat_circle (self) :
        return f'the masahat of circle is : {Circle.pi*(self.radiyan **2)}'
    

class ball(Circle) :
    def __init__(self, radiyan,diameter):
        super().__init__(radiyan)
        self.diameter = diameter

    def shot (self) :
        print(f"shottttt :  {self.radiyan} and {self.diameter}" )





radiyan = int(input("enter your radiyan of circle"))
diameter = radiyan * 2
circle1 = ball(radiyan,diameter)
circle1.shot()
print (circle1 .mohit_circle())
print (circle1 .masahat_circle())

 
        