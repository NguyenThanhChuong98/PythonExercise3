from datetime import datetime, date


def get_date():
    get_date_today = date.today()
    print(datetime.combine(get_date_today, datetime.min.time()))


get_date()


