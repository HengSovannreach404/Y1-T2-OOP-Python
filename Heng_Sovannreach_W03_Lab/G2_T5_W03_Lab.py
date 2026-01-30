print("-------------Iteration: for and while, break, and continue-------------")

#Exercise1
print("Exercise 1 ")
my_list = [1, 2, 3, 4, 5]
for i in range(len(my_list)):
    print(my_list[i])

#Exercise2
print("Exercise 2 ")
for i in range(1, 11):
    if i > 6:
        break
    print(i)

#Exercise1
print("Exerxise 3")
for i in range(1, 11):
    if i == 4:
        continue
    if i > 6:
        break
    print(i)

print("-------------List: Definition, Methods, Syntax------------- ")

#Exercise1
print("Exercise 1")
my_fruits = ["Water melon" , "Orange" , "Mango", "Banana"]
print(my_fruits)

#Exercise2
print("Exercise 2")
my_fruits.append("Dragon Fruit")
my_fruits.append("Grape")
print("Update lists of my fruits:", my_fruits)

#Exercise3
print("Exercise 3")
my_fruits.remove('Water melon')
print("Update list of fruits after delete:",my_fruits)

#Exercise4
print("Exercise 4")

for i in range (len(my_fruits)):
    for j in range(i+1,len(my_fruits)):
        if(my_fruits[i]>my_fruits[j]):
            my_fruits[i], my_fruits[j]=my_fruits[j], my_fruits[i]
print("After sorting: ",my_fruits)


print("-------------Tuple: Definition, Methods, Syntax-------------")

#Exercise1
print("Exercise 1")
my_tuple=(1,2,3,4,5)
print(my_tuple)

#Exercise2
print("Exercise 2")
my_tuple(2) = 2
print(my_tuple)

#Exercise3
print("Exercise 3")
list_tuple=[]
for i in range(len(my_tuple)):
    list_tuple.append(my_tuple[i])
print(list_tuple)

print("-------------Dictionary: Definition, Methods, Syntax--------------")

#Exercise1
people={
    "Alice":30,
    "Bob":25,
    "Charlie":20
}
#Exercise2
def add_user():
    key=input("Enter people's name: ")
    value=int(input("Enter people's age: "))
    people[key]=value
    print(people)
add_user()
people.popitem()
print(people)

#Exercise3
for k,v in people.items():
    print(k,v)

print("--------Function: Return Type and Non-Return Type, Anonymous Function (Lambda Function)-------")
#Exercise1

def sum(a,b):
    return a+b

print(sum(3,4))

#Exercise2
def greet():
    print("Hello World!")

greet()

#Exercise3
square= lambda a:a**2
print(square(5))

# (Bonus) User Authentication System
print("--------(Bonus) User Authentication System--------")
usernames = []
user_password = {}

# 1. Register


def Register():
    while True:
        user = input("Enter a Username to register: ")
        if user in usernames:
            print("This username is already taken.")
            continue

        while True:
            password = input("Enter a password: ")
            if check_pass(password):
                usernames.append(user)
                user_password[user] = password
                print("Registration successful!")
                return


def check_pass(password):
    lower_case = False
    upper_case = False
    digit_case = False
    special_case = False

    # lowercase
    for i in password:
        if i.islower():
            lower_case = True
    # uppercase
    for i in password:
        if i.isupper():
            upper_case = True
            break
    # digit case
    for i in password:
        if i.isdigit():
            digit_case = True
            break
    # special charactircase
    special_char = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/`~"
    for i in password:
        if i in special_char:
            special_case = True
            break
    # statement
    if len(password) < 8:
        print("Password too short. Must be at least 8 characters.")
        return False
    elif not lower_case:
        print("Password must contain at least one lowercase letter.")
        return False
    elif not upper_case:
        print("Password must contain at least one uppercase letter.")
        return False
    elif not digit_case:
        print("Password must contain at least one digit.")
        return False
    elif not special_case:
        print("Password must contain at least one special character.")
        return False
    else:
        print("Registration successful with a strong password!")
    return True

# 2. Login


def Login():
    attempt = 3
    user = input("Enter username: ")
    if (user not in usernames):
        print("Username not found!Please try again!")
        return
    while attempt > 0:
        password = input("Enter password: ")
        if (user_password[user] == password):
            print("Login Successfully!")
            return
        if attempt >= 0:
            attempt = attempt - 1
            print(f"Password doesn't match try again!. You have {attempt} attempts left") 
        if attempt <= 0:
            print("Too many login fail attempts. Access blocked")
            return

# 3. Forget password


def Forget_password():
    user = input("Enter your username to retrieve your password: ")
    if user not in user_password:
        print("Username not found.")
        return
    print(f"Your password is: {user_password[user]}")


while True:
    print("\n Menu: ")
    print("1. Register")
    print("2. Login")
    print("3. Forget Password")
    print("4. Exit")
    choice = int(input("Choose an option(1-4):"))
    if choice == 1:
        Register()
    elif choice == 2:
        Login()
    elif choice == 3:
        Forget_password()
    elif choice == 4:
        print("Exiting the program. Goodbye!")
        break
