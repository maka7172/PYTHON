user_text = input("enter your TEXT:   ")
enription_number = 22 
encryption_list = []
decryption_list = []
for ch in user_text :
    encryption_list.append(ord(ch)+ enription_number)

print("choice 1-3 :")
print(" 1-encode")
print(" 2-decode")
print(" 3-encode and decode")
choice = int(input())
if choice == 1 :
    print(encryption_list)
elif choice == 2 :
    # print(user_text)
    for i in encryption_list :
        decryption_list.append(chr(i-enription_number))
    for ch in decryption_list :
        print(ch,end='')

elif choice == 3 :
    print(encryption_list)
    print('-' * 30)
    for i in encryption_list :
        decryption_list.append(chr(i-enription_number))
    for ch in decryption_list :
        print(ch,end='')