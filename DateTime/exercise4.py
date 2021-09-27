from _datetime import datetime


def get_current_time():
    get_current_date_time = datetime.now()
    print(get_current_date_time.time())


get_current_time()
