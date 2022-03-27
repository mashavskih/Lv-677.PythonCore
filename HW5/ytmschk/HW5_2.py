dict_keys = ['First', 'Second', 'Third']
login_pass = dict.fromkeys(dict_keys, 0)

login = input('Enter your login: ')
# if input in login_pass:
#     print ("Nice to see you again!")
#     else:
#         while input not in login_pass:
#             print ('Please try again')
#             input = input('Enter your login:')

while login in login_pass:
    if login not in login_pass:
        print ('Please try again')
        print (input('Enter your login: '))
    print ("Nice to see you again!")

# while input in login_pass:
#     print ('The login is missing')
#     input = input('Enter your login: ')