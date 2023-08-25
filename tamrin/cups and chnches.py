import random
user_cup = int(input("how many cups ?   "))
print('-' *50)
user_choice = int(input("how many glass ?    "))
print('-' *50)
win = 0

while user_choice > 0 :
    ai_choice = random.randrange(1,user_cup +1)
    print('\n','-' *50)
    ans= int(input(f"enter your choice betwin [1 - {user_cup}]: "))
    if ans == ai_choice :
        print(" "*20,'*'*30)
        print(' '*25,end=' ')
        print("YOU ARE  WIN!!!!!!")
        print(" "*20,'*'*30)
        win = 1
        break
    else :
        user_choice -=1 
        print("you shuld trying!!!")
if win == 0 :
    print(f"you can not win after {user_choice} , YOU ARE LOST !!!!")
