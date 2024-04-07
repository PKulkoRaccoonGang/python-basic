# 0 -> 0 днів, 00:00:00
# 224930 -> 2 дні, 14:28:50
# 466289 -> 5 днів, 09:31:29
# 950400 -> 11 днів, 00:00:00
# 1209600 -> 14 днів, 00:00:00
# 1900800 - > 22 дні, 00:00:00
# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59

TOTAL_SECONDS_LIMIT = 8640000
SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24

seconds_value = int(input('Enter seconds value: '))

if 0 <= seconds_value < TOTAL_SECONDS_LIMIT:
    days, remaining_seconds = divmod(seconds_value, HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE)
    hours, remaining_seconds = divmod(remaining_seconds, MINUTES_IN_HOUR * SECONDS_IN_MINUTE)
    minutes, seconds = divmod(remaining_seconds, SECONDS_IN_MINUTE)

    is_singular_day_except_11 = (days % 10 == 1 and days % 100 != 11)
    is_plural_days = (days % 100 < 10 or days % 100 >= 20)

    if days == 1 or is_singular_day_except_11:
        days_str = 'день'
    elif 2 <= days % 10 <= 4 and is_plural_days:
        days_str = 'дні'
    else:
        days_str = 'днів'

    print(f'{days} {days_str}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}')
