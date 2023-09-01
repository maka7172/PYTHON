class Time :
    def __init__(self,hour,minit,secont) :
        # if int(hour) >= 24 :
        #     raise ValueError("the hour number not be grater than 24")
        # if int(minit) > 59 :
        #     raise ValueError("the minit number not be grater than 59")
        # if int(secont) > 59 :
        #     raise ValueError("the sec number not be grater than 59")
        self.hour = hour
        self.minit = minit
        self.secont = secont
    def hour_time (self) :
        return f"the hour is : {self.hour}" 
    def minit_time (self) :
        return f"the miniut is : {self.minit }"
    def secont_time (self) :
        return f"the secont is :{self.secont}"
    def __str__(self) :
        raise NotImplementedError('you should crate method with your idea')
    
class TimeShow (Time) :
        def __str__(self) :
            return f"the time is : {self.hour:02} : {self.minit:02} : {self.secont:02}"
        
        def __add__(self,x): #craet temp object and give two object for plus together
            secont = self.secont + x.secont
            minit = self.minit + x.minit + (secont //60)
            hour = self.hour + x.hour + (minit //60)
                       
            temp = TimeShow(hour %24,minit %60,secont%60)
            return temp 
        
        def __eq__(self, x) :
            if self.hour == x.hour and self.minit == x.minit and self.secont == x.secont :
                return True
            else :
                return False
                
    
    



if __name__ == '__main__':
    date1= TimeShow(10,22,33)
    print(date1)
    print(date1.hour_time())