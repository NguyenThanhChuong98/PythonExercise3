from datetime import date, timedelta


def get_day():
    get_today = date.today()
    for x in range(0, 5):
        print(get_today + timedelta(x))

get_day()
