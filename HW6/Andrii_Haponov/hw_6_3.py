# Task3. Write a function that calculates the number of characters included in a given string

# input: “hello”
# output: {“h”:1, “e”:1, “l”:2, “o”:1}

# Задача3. Напишите функцию, которая вычисляет количество символов, содержащихся в заданной строке.

# ввод: “hello”
# вывод: {"h":1, "e":1, "l":2, "o":1}

def f(l: str) -> dict:
    q = {i: l.count(i) for i in l}
    return f"Your string contains the following number of characters: {q}"

def f2(l):
    q = {}
    for i in l:
        q[i] = l.count(i)
    return f"Your string contains the following number of characters: {q}"

print(f("hello"))
print(f2("hello"))




        