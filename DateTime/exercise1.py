from _datetime import datetime


def date_time_format():
    get_current_date_time = datetime.now()
    print(get_current_date_time)
    print(get_current_date_time.year)
    print(get_current_date_time.month)
    print(get_current_date_time.strftime("%U"))
    print(get_current_date_time.strftime("%w"))
    print(get_current_date_time.strftime("%j"))
    print(get_current_date_time.strftime("%d"))
    print(get_current_date_time.strftime("%A"))


date_time_format()

date_time_format()
