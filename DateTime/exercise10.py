import datetime


def add_second():
    get_current_date = datetime.datetime.now()
    add_more_second = get_current_date + datetime.timedelta(0, 5)
    print(get_current_date.time())
    print(add_more_second.time())


add_second()
