from package1.bankacount import Bank
import os
os.system('cls')
mohammad = Bank('mohammad',10000)
mohammad2 = Bank('mohammad2',10000)
mohammad3 = mohammad + mohammad2
mohammad += mohammad2
mohammad.transfer(mohammad2,20000) 
print (mohammad)
print(mohammad2)
print(mohammad3)






