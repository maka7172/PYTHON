# a=int(input("enter number betwin 0-10 :   "))
# if a < 2 :
#     print("ok")

# elif a<5 :
#     print("elif")
# else :
#     print("else")
# user_word = input("enter word!")
# if len(user_word) % 2 ==0 :
#     print(f'the word: {user_word} is EVEN')
# else :
#     print(f'the word: {user_word} is ODD')
# user_price = int(input("enter number"))
# if user_price > 1000 : 
#     print("very expensive")
# elif user_price <= 1000 and user_price >= 500 :
#     print("expensive")
# elif user_price >= 100 and user_price <500  :
#     print("is very mamoli")  
# elif user_price <0 :
#     print("the price dos'nt negative")
# else :
#     print("kheyli khari")

# number1 = int(input("enter number 1 :  "))
# number2 = int(input("enter number 2 :  "))
# opration = input("choice \'plus\' or \'menus\' or \'multiple\' (pl,me,mu) :  ")
# op_duct = {
#     "pl" : "plus",
#     "me" : "menus",
#     "mu" : "multiple"
# }
# print(op_duct.keys())
# print(opration)
# if opration not in  op_duct.keys() :
#     print("your choice is wrong")
# elif opration == 'pl' :
#     print(f"you choice : {op_duct[opration]} . number1 :{number1}  {op_duct[opration]} number2 :{number2} is :" , number1 + number2)
# elif opration == 'me' :
#     print(f"you choice : {op_duct[opration]} . number1 :{number1}  {op_duct[opration]} number2 :{number2} is :" , number1 - number2)
# elif opration == 'mu' :
#     print(f"you choice : {op_duct[opration]} . number1 :{number1}  {op_duct[opration]} number2 :{number2} is :" , number1 * number2)
#************************************
# import random
# mylist =[]
# for i in range (1,random.randrange(5,10)) :
#     # number = int(input("enter number"))
#     mylist.append(int(input("enter number"))) 
# listlen = len(mylist)
# if listlen % 2 == 0 :
#     print(f"your list len is : {listlen}")
#     print(f" the middle of list is : {(mylist[listlen//2 -1] + mylist[listlen//2 ])/2}")    

# else :
#     print(f"your list len is : {listlen}")
#     print(f"the middle of list is : {mylist[listlen//2]}")   

# number1 = int(input("enter number 1 :  "))
# number2 = int(input("enter number 2 :  "))
# sum = number1 + number2 
# if sum <=20 and sum >18 :
#     print (20)
# elif sum <=18 and sum >15 :
#     print (18)
# elif sum <= 15 and sum >10 :
#     print (15)
# elif sum <= 10 :
#     print ("you donot give enufe core"
# my_list = [2,4,3,7,5,6,9,8,0,1]
# print(my_list) 
# my_list.sort() 
# print(f"the list after sort is : {my_list}")
# print(f"the avrage betwine min and max is {(max(my_list) + min(my_list))/2} ")
#******************************************

# my_year = {
#     "spring" : {
#         "far" : 31 ,
#         "ordi": 31 ,
#         "khordad" : 31 
#     },
#     "summer" : {
#         "tir" : 31 ,
#         "mor" : 31 ,
#         "sha" : 31
#     },
#     "fall"   : {
#         "mehr" : 30 ,
#         "aban" : 30 ,
#         "azar" : 30
#     },
#     "winter" : {
#         "dey" : 30 ,
#         "bah" : 30 ,
#         "esf" : 29
#     }
# }

# user_mon = input ("enter your faver mon") 
# seseens = my_year.keys()
# for sessen in seseens :
#    if user_mon in  my_year[sessen].keys() :
#       print(f"your mon is in sessen : {sessen} ." , f"your mon have  {my_year[sessen][user_mon]} days ")
#**********************************************************************

# user_word = input ("enter your word")
# if user_word == user_word[::-1] :
#     print("your word is clender")
# else :
#     print("your word is mozakhraf")
#************************************
# user_number = int(input("enter number"))
# if user_number % 3 == 0 and user_number % 5 != 0 :
#     print("number is 3 mazrab")
# if user_number % 5 == 0 and user_number % 3 != 0 :
#     print("number is 5 mazrab") 
# if user_number % 3 == 0 and user_number % 5 == 0 :
#     print("number is 3 ,5 mazrab") 
#************************************
# char = input("enter one character") 
# if len(char) == 1 :
#     print("true ")
# else :
#     print("mage khari ? 1 char bezan")
#*****************************
# number =int(input("enter number"))
# sum = 0 
# while number != 0 :
#     sum += number % 10 
#     number = number//10
# print(f"the sum of num is : {sum}")    
my_list = [4,5,6,7,8,9]

for index , i in enumerate (my_list) :
    print (index,i)
