# age = 16
# money = 500
# season = 'autumn'

# if age>=16 and money>400 and (season=='summer' or season=='autumn'):
#     print('yes')
# else:
#     print('no')

import datetime
curr_date = datetime.datetime.now()
birth_date = datetime.datetime(2004,5,14)
date_diff = curr_date - birth_date
print(date_diff)
if date_diff.days / 365 > 18:
    print('YES')
else:
    print('NO')
