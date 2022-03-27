# Task2. Write a script that checks the login that the user enters. 
# If the login is "First", then greet the users. If the login is different, send an error message. 
# (need to use loop while)

# Задача2. Напишите скрипт, проверяющий логин, который вводит пользователь.
# Если логин «Первый», то приветствуйте пользователей. Если логин другой, отправьте сообщение об ошибке.
# (необходимо использовать цикл while)

checks_the_login = []
item = input("Enter login : ")
while item != "finish":
    checks_the_login.append(item)
    item = input("Enter login : ")
print(checks_the_login)

login = input("Enter login : ")
if login in checks_the_login:  
    print(f"Hello {login}!")
else:    
    print("Error: This login was not found.")
       




