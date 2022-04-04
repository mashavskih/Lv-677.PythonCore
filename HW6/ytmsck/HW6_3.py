mystring = "Hello"

def number_of_charachters(your_string):
    return {x: your_string.count(x) for x in your_string}

print(number_of_charachters('gfvgcvxdx kjhjv 1n43!'))

# def calculate_characters(some_string: str) -> dict:
#     """ 
#     Function calculates the number of characters included in a given string 
#     and returns dict where keys are unique characters of given string
#     and values are number of relevant character of given string
#     """
#     return {char: some_string.count(char) for char in some_string}


# print(calculate_characters("gfvgcvxdx kjhjv 1n43!"))