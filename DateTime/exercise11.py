from datetime import datetime


def convert_datetime():
    get_today = datetime.now()
    day_of_year = (get_today - datetime(get_today.year, 1, 1)).days + 1
    print(day_of_year)


convert_datetime()
