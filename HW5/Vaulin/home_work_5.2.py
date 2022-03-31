# Lv-677_Ivan_Vaulin
# Task2. Write a script that checks the login that the user enters. 
# If the login is "First", then greet the users. If the login is different, send an error message. 
# (need to use loop while)

x1 = {1: 'First'}
while True:
    login = input("Enter your login: ")
    if login == x1[1]:
        print("Good job")
        break
    else:
        print ("Try again ")