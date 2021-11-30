print("Hello User, I'm KDNL Programming")
print("\nCreate a password that contains:")
print("Greater than 15 letters \nHave at least one capital letter \nHave at least one number \nHave at least one special char ")

User_Password= input("\nPassword: ")
Password_value = True
Character_Special=['!', '@', '#',"$", "%", "^", "&", "*", "(",")","_","+"]

while Password_value:  
    if (len(User_Password)<15):
        print("It must contain greater than 15 letters")
        Password_value=False

    if not any(char.isupper() for char in User_Password):
        print("It must contain atleast one capital letter")
        Password_value= False

    if not any(char.isdigit() for char in User_Password):
        print("It must contain atleast one number")
        Password_value= False

    if not any(char in Character_Special for char in User_Password):
        print("It must contain atleast one special character")
        Password_value= False
        
    if Password_value:
        print("Your Password is Valid")
        break
   
        