first_number = int(input('Enter your first number: '))
second_number = int(input('Enter your second number: '))

action = input('Do you want to: ')

if action == '+':
    print(first_number + second_number)
elif action == '-':
    print(first_number - second_number)
elif action == '*':
    print(first_number * second_number)
elif action == '/':
    if second_number != 0:
        print(first_number / second_number)
    else:
        print('You cannot divide by zero')
else:
    print('Invalid operator')
