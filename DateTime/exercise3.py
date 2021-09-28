from datetime import datetime


def conv_str():
    date_time = datetime.strptime('Jul 1 2014 2:43PM', '%b %d %Y %I:%M%p')
    print(date_time)


conv_str()
