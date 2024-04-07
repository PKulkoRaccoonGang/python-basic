# 999 -> 2
# 1000 -> 0
# 423 -> 8
# 33 -> 9
# 25 -> 0
# 1 -> 1

num = int(input('Enter your number: '))

while num >= 10:
    product = 1
    while num > 0:
        digit = num % 10
        product *= digit
        num //= 10
    num = product

print(num)
