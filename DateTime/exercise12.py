import time


def get_mil_second():
    milli_sec = int(round(time.time() * 1000))
    print(milli_sec)


get_mil_second()
