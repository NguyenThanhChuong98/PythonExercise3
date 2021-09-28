import time


def get_first_monday(input_data):
    print(time.asctime(time.strptime(input_data, '%Y %W %w')))


given_week = '2015 50 1'
get_first_monday(given_week)
