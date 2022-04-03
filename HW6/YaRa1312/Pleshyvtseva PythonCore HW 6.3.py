# 6.3

def characters_number_calculation(user_string):
    result = {}
    for i in user_string:
        result[i] = user_string.count(i)
    return result

user_string = input("Enter a string to calculate the number of its characters: ")
print(characters_number_calculation(user_string))
