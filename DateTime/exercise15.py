from datetime import date, timedelta


def get_all_sundays(year_input):
    dt = date(year_input, 1, 1)
    dt += timedelta(days=6 - dt.weekday())
    while dt.year == year_input:
        yield dt
        dt += timedelta(days=7)


for s in get_all_sundays(2020):
    print(s)
