
import random

choices = ['r', 'p', 's']

choice_meaning = {
    'r': 'Rock',
    's': 'Scissors',
    'p': 'Paper'
}
user_score = 0
ai_score = 0 
for i in range(5) :
    user_choice = input('Select from Rock, Paper, Scissors: (r, p, s) ')

    ai_choice = random.choice(choices)

    if user_choice in choices:
        print(f'Your choice is {choice_meaning[user_choice]}. AI choice is {choice_meaning[ai_choice]}.')
        # r > s - p > r - s > p
        if user_choice == ai_choice:
            # print('Tie')
            user_score += 1
            ai_score += 1 
        elif user_choice == 'r' and ai_choice == 's':
            # print('You Won!')
            user_score +=1
        elif user_choice == 'p' and ai_choice == 'r':
            # print('You Won!')
            user_score += 1
        elif user_choice == 's' and ai_choice == 'p':
            # print('You Won!')
            user_score += 1
        else:
            # print('You Lost!')
            ai_score +=1
    else:
        print('Invalid input')
    print( \n )    
if user_score >ai_score :
    print(f"uuser with {user_score} score WIN!")
elif user_score == ai_score :
    print(f"you and ai pie!!")
else :
    print(f"AI with {ai_score} score WIN! ,you LOST !!!")