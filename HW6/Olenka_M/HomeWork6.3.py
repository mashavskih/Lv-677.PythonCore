def calculate_characters(some_string: str) -> dict:
    """ 
    Function calculates the number of characters included in a given string 
    and returns dict where keys are unique characters of given string
    and values are number of relevant character of given string
    """
    return {char: some_string.count(char) for char in some_string}


# print(calculate_characters("gfvgcvxdx kjhjv 1n43!"))