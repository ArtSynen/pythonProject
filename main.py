'''
while True:
    type_ = input('Введіть +,-,/,*,^n (для виходу впишіть exit) ')
    if type_ == 'exit':
        break
    try:
        if type_ == '+':
            a = int(input('Введіть перше число '))
            b = int(input('Введіть друге число '))
            c = a + b;
            print('c = ' , a , ' + ' , b , ' = ' , c)
        if type_ == '-':
            a = int(input("Введіть перше число "))
            b = int(input("Введіть друге число "))
            c = a - b;
            print('c = ' , a , ' - ' , b , ' = ' , c)
        if type_ == '/':
            a = int(input('Введіть перше число '))
            b = int(input('Введіть друге число '))
            c = a / b;
            print('c = ' , a , ' / ' , b , ' = ' , c)
        if type_ == '*':
            a = int(input('Введіть перше число '))
            b = int(input('Введіть друге число '))
            c = a * b;
            print('c = ' , a , ' * ' , b , ' = ' , c)
        if type_ == '^n':
            a = int(input('Введіть перше число '))
            b = int(input('Введіть степінь '))
            c = pow(a, b)
            print('c = ' , a , ' ^ ' , b , ' = ' , c)
    except:
        print('Введіть дані коректно')
'''
'''
while True:
    type_ = input('Введіть +,-,/,*,^n (для виходу впишіть exit) ')
    if type_ == 'exit':
        break
    a = int(input('Введіть перше число '))
    try:
        if type_ == '+':
            b = int(input('Введіть друге число '))
            c = a + b;
            print('c = ' , a , ' + ' , b , ' = ' , c)
        if type_ == '-':
            b = int(input("Введіть друге число "))
            c = a - b;
            print('c = ' , a , ' - ' , b , ' = ' , c)
        if type_ == '/':
            b = int(input('Введіть друге число '))
            c = a / b;
            print('c = ' , a , ' / ' , b , ' = ' , c)
        if type_ == '*':
            b = int(input('Введіть друге число '))
            c = a * b;
            print('c = ' , a , ' * ' , b , ' = ' , c)
        if type_ == '^n':
            b = int(input('Введіть степінь '))
            c = pow(a, b)
            print('c = ' , a , ' ^ ' , b , ' = ' , c)
    except:
        print('Введіть дані коректно')
'''
while True:
    type_ = input('Введіть +,-,/,*,^n (для виходу впишіть exit) ')
    if type_ == 'exit':
        break
    a = int(input('Введіть перше число '))
    b = int(input('Введіть друге число '))
    try:
        if type_ == '+':
            c = a + b;
        elif type_ == '-':
            c = a - b;
        if type_ == '/':
            c = a / b;
        if type_ == '*':
            c = a * b;
        if type_ == '^n':
            b = int(input('Введіть степінь '))
            c = pow(a, b)
        print(c)
    except:
        print('Введіть дані коректно')