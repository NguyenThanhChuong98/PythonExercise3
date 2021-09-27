from datetime import date, timedelta


def get_day():
    get_today = date.today()
    get_tomorrow = date.today() + timedelta(1)
    get_yesterday = date.today() - timedelta(1)
    print(get_today)
    print(get_tomorrow)
    print(get_yesterday)


get_day()
