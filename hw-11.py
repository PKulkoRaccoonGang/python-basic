CONTINUE_OPTIONS = ['y', 'yes']

while True:
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

    continue_choice = input('Do you want to continue? (y/n): ')

    if continue_choice.lower() not in CONTINUE_OPTIONS:
        break
