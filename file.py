user ={'harshith':'24567','raji':'dhv765','kavya':'45792'}
status =" "
def display_menu():
    status = input("are you a registered user?(yes/no)?press q to quit:")
    if status == "yes":
        print (old_user())
    elif status == "no":
        print(new_user())

def new_user ():
    username =input("enter username:")
    password = input("enter password:")
    if username in user and  password == user[username]:
        print("login successful")
    else:
        print("you are not authorized person, please register first.")

def old_user():
    username =input("enter username:")
    password = input("enter password:")
    if username in user and  password == user[username]:
        print ("welcome back",user)
    else:
        print("invalid username or password.please try again.")

if status == "q":
    print(exit())
else:
     print(display_menu())



