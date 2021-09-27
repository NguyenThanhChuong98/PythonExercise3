def check_leap_year(year_input):
    if (year_input % 4) == 0:
        if (year_input % 100) == 0:
            if (year_input % 400) == 0:
                print("This is a leap year".format(year_input))
            else:
                print("This is not a leap year".format(year_input))
        else:
            print("This is a leap year".format(year_input))
    else:
        print("This is not a leap year".format(year_input))


year = 1600
check_leap_year(year)
