a = int(input('enter a:'))
b = int(input('enter b:'))
sign = input('Sign +, -, *, /, **:')
if sign == '+':
     print(a + b)
elif sign == '-':
     print(a - b)
elif sign == '*':
     print(a * b)
elif sign == '**':
     print(a ** b)
elif sign == '/' :
     if b != 0:
          print(a / b)
     else:
          print('Divide by 0!')