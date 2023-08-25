number = int(input("enter your number"))
count = 0 
for i in range(2,number) :
    if number%i == 0 :
        print(f"your number : {number} is'nt prime ")
        print(f"your number bakhsh pazir to : {i}")
        count +=1
        break 

if count == 0 :
    print(f"your number : {number} is prime ")
