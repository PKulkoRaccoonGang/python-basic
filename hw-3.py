user_number = int(input('Enter a 5-digit number: '))

reversed_number = (user_number % 10) * 10000 + ((user_number // 10) % 10) * 1000 + ((user_number // 100) % 10) * 100 + ((user_number // 1000) % 10) * 10 + (user_number // 10000)

print('Result: ', reversed_number)
