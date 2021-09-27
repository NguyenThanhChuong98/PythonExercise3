from datetime import date, timedelta


def subtract_day():
    get_five_days_ago = date.today() - timedelta(5)
    print(get_five_days_ago)


subtract_day()
