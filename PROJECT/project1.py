import random
user_config = {}

# ************************************************************
def user_ascii_symbol(num) :
    """return symbol ascii range code"""
    if num == 0 :
        return 33,48   
    elif num == 1 :
        return 58,65
    elif num == 2 :
        return 91,97
    elif num == 3 :
        return 123,127
    
# ************************************************************
def generat_user_ascii(num) :
    """return char between symbol & number & upper-lower alpha & space"""
    if num == 0 :
        a,b = user_ascii_symbol(random.randrange(0,4))
        return chr(random.randrange(a,b) )   
    elif num == 1 :
        return chr(random.randrange(48,58))
    elif num == 2 :
        return chr(random.randrange(65,91))
    elif num == 3 :
        return chr(random.randrange(97,122))
    elif num == 4 :
        return chr(32)

# ************************************************************
def genarat_user_pass(num) :
    """creat password """
    password_user = []
    for i in range(num) :
        while True : #for select true config
            index_user = random.randrange(0,5)
            if list(user_config.values())[index_user] :
                break
        
        password_user.append( generat_user_ascii(index_user))
    print (f"your password is :   {password_user}" )

# ************************************************************
def select_config_user(select_number) :
    """craet dict of config with user select"""
    
    if select_number == 0 :
        user_select = 'symbol'
    elif select_number == 1 :
        user_select = 'number'
    elif select_number == 2 :
        user_select = 'upper alpha'
    elif select_number == 3 :
        user_select = 'lower alpha'
    elif select_number ==4 :
        user_select = 'space'
    
    yes_no = input(f"please select copelex input : {user_select}:  yes/no  ") 
    # if not (yes_no.isalpha()) :
    #     print("select y or n ")
    #     select_config_user(select_number) 
        
    if yes_no == 'y' :
        user_config[user_select] = True
     
    elif yes_no == 'n' :
        user_config[user_select] = False
    # else :
    #     print("select y or n ")
    #     select_config_user(select_number) 
       
# ************************************************************
def start() :
    """start program"""
    try :
        num = int(input ("enter number of char that you like give password"))
    except:
        print("enter number")
        start()
        
    for i in range (5) :
        select_config_user(i)
    
    genarat_user_pass(num)
    

start()
