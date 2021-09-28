import datetime


def get_week():
    get_week_number = datetime.date(2015, 6, 16).isocalendar()[1]
    print(get_week_number)


get_week()
