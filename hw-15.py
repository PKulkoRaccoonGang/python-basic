# 0 -> 0 днів, 00:00:00
# 224930 -> 2 дні, 14:28:50
# 466289 -> 5 днів, 09:31:29
# 950400 -> 11 днів, 00:00:00
# 1209600 -> 14 днів, 00:00:00
# 1900800 - > 22 дні, 00:00:00
# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59

number = int(input('Enter seconds value: '))

if 0 <= number < 8640000:
    days, remaining_seconds = divmod(number, 24 * 60 * 60)
    hours, remaining_seconds = divmod(remaining_seconds, 60 * 60)
    minutes, seconds = divmod(remaining_seconds, 60)

    if days == 1 or (days % 10 == 1 and days % 100 != 11):
        days_str = 'день'
    elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
        days_str = 'дні'
    else:
        days_str = 'днів'

    print(f'{days} {days_str}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}')
