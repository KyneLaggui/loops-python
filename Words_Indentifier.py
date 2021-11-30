import colorama
colorama.init 

User_Words=input("Input: ")

User_Words_Vowels=0
User_Words_Consonants=0

Without_SC_Space = ''.join(filter(str.isalnum, User_Words.lower()))
#Removes the Special Characters and Space. Automatically lowercase the uppercase letters. 

User_Number_of_Words = len(User_Words.split())
#Count the number of words

for k in Without_SC_Space:
    if(k == 'a'or k == 'e'or k == 'i'or k == 'o'or k == 'u'):
           User_Words_Vowels= User_Words_Vowels+1
    else:
        User_Words_Consonants=User_Words_Consonants+1

print(colorama.Fore.GREEN + f"\nThe number of words are {User_Number_of_Words}")
print(colorama.Fore.CYAN + f"The number of vowels are {User_Words_Vowels}")
print(colorama.Fore.YELLOW + f"The number of consonants are {User_Words_Consonants}")
