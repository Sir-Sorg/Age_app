import datetime

person_age = input()
person_age = person_age.split('/')  # Format : 1995 8 25
person_age = list(map(lambda this_date: int(this_date), person_age))
if person_age[1] > 12:
    print('WRONG')
elif person_age[2] > 31:
    print('WRONG')
else:
    person_age = datetime.datetime(person_age[0], person_age[1], person_age[2])
    time_of_now = datetime.datetime.now()
    day_difference = int(time_of_now.strftime('%j')) - \
        int(person_age.strftime('%j'))
    yer_difference = int(time_of_now.strftime('%Y')) - \
        int(person_age.strftime('%Y'))
    age = yer_difference if day_difference >= 0 else yer_difference-1
    print(age)
