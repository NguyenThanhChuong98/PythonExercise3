import datetime
from datetime import date


def add_years(d, years):
    try:
        return d.replace(year=d.year + years)
    except ValueError:
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))


print(add_years(datetime.date(2015, 1, 1), -1))
print(add_years(datetime.date(2015, 1, 1), 0))
print(add_years(datetime.date(2015, 1, 1), 2))
print(add_years(datetime.date(2000, 2, 29), 1))
