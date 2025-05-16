import zipfile
import os

#colors
red="\033[91;1m"
green="\033[92;1m"
blue="\033[94;1m"
purple="\033[95;1m"

os.system("clear")
print(f"""{red}

░▒▓████████▓▒░▒▓████████▓▒░░▒▓██████▓▒░  
░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░           ░▒▓██▓▒░░▒▓█▓▒░        
░▒▓██████▓▒░    ░▒▓██▓▒░  ░▒▓█▓▒░        
░▒▓█▓▒░       ░▒▓██▓▒░    ░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓████████▓▒░░▒▓██████▓▒░  
                                         
{green}made by Adeesha{blue}

""")
    
zip_file=input("Enter Your Zip file path: ")
pass_file=input("Enter Your Password file path: ")

zip_file=zipfile.ZipFile(zip_file)

with open(pass_file, 'r') as pass_file:
    
    passwords=pass_file.readlines()

for password in passwords:
    password=password.strip("\n")
    
    try:
        zip_file.extractall(pwd=password.encode())
        print("="*40,"\nPassword is ", password,"\n","="*40)
        break
    except:
        pass
print(f"{green}finish")
