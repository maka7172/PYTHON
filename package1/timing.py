class Time :
    def __init__(self,hour=None,minit=None,secont=None) :
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
            return f"the time is : {self.hour} : {self.minit} : {self.secont}"
        
        def __add__(self,x):
            temp = TimeShow()
            temp.hour = self.hour + x.hour
            temp.minit = self.minit + x.minit
            temp.secont = self.secont + x.secont
            return temp 
    



if __name__ == '__main__':
    date1= TimeShow(10,22,33)
    print(date1)
    print(date1.hour_time())