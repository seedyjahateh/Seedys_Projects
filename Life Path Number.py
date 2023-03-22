######################################################################
# Author: Seedy Jahateh
# Username: jahatehs
# Assignment: A04: A Bug's Life
#
# Purpose: Demonstrates the use of division and modulus operations,
#
# This program calculates your Life Path Number.
#
######################################################################

def get_life_path_number():
    """
    This function inputs date of birth and calculates Life Path Number.
        Param: No parameters. But takes user inputs.
        :return: Life Path Number
        """
    digit_list = []
    month = input("In what month were you born? ")

    # Checks if input is a multiple of 11.
    if int(month) % 11 == 0:
        digit_list.append(int(month))
    else:
        # Separates the digits of the input and appends them to a list as individual integer.
        for i in month:
            digit_list.append(int(i))

    day = input("In what day of that month were you born? ")

    if int(day) % 11 == 0:
        digit_list.append(int(day))

    elif int(day) >= 28:
        int_day = 0
        for k in day:
            int_day += int(k)
        digit_list.append(int_day)

    else:
        for z in day:
            digit_list.append(int(z))

    year = input("In what year were you born? ")
    if int(year) % 11 == 0:
        digit_list.append(int(year))
    else:
        sum_of_year_digits = 0
        for year_digit in year:
            sum_of_year_digits += int(year_digit)

        if int(sum_of_year_digits) % 11 == 0:
            digit_list.append(int(sum_of_year_digits))

        elif int(sum_of_year_digits) <= 28:
            sum_of_sum_of_year_digits = 0
            for dig in str(sum_of_year_digits):
                sum_of_sum_of_year_digits += int(dig)

            digit_list.append(int(sum_of_sum_of_year_digits))
        num = 0
        for d in digit_list:
            num += int(d)

        if num % 11 == 0:
            print(f"Your Life Path Number is {num} ")

        elif num >= 10:
            sum_of_num_digits = 0
            for y in str(num):
                sum_of_num_digits += int(y)
            print("")
            print(f"Your Life Path Number is {sum_of_num_digits}. ")


def main():
    """
    This is the main function. It calls all the other functions above.
    :return: None
    """
    get_life_path_number()


if __name__ == "__main__":
    main()