prime_numbers_of_given_numbers = []
prime_numbers_for_lcm = []
given_number = []
prime_numbers_answer = []

def find_first(number):

    """
    Function to calculate all prime numbers of given number
    :param number: given number
    :return: list of prime numbers of number
    """

    first_numbers = []
    new_number = number
    while new_number != 1:
        for num in range(2, abs(new_number) + 1):
            if new_number % num == 0:
                first_numbers.append(num)
                new_number = int(new_number / num)
                break
        continue
    return first_numbers


def define_numbers():

    """
    Function responsible for taking n-numbers from user

    """

    while True:
        try:
            how_many = int(input('How many numbers would You like to check 2 or 3 :  '))
            if isinstance(how_many, int) and 4 > how_many > 1:
                break
        except ValueError:
            print('Please input number!!')
    for i in range(1, how_many+1):
        while True:
            try:
                num = int(input('Please give me no.' + str(i) + ' number: '))
                if isinstance(num, int) and num > 0:
                    given_number.append(num)
                    break
            except ValueError:
                print('Please input number!!')


define_numbers()

"""
Placing prime numbers of each number to separate lists
"""

for number in given_number:
    if number == 1:
        prime_numbers_of_given_numbers.append([1])
        prime_numbers_for_lcm.append([1])
    else:
        prime_numbers_of_given_numbers.append(find_first(number))
        prime_numbers_answer.append(find_first(number))
        prime_numbers_for_lcm.append(find_first(number))


new_list = prime_numbers_of_given_numbers
new_list_lcm = prime_numbers_for_lcm
nnw_given_numbers = given_number

"""
lcd - least common divider
lcm - least common multiple
"""

lcd = 1
lcm = 1
lcd_for_lcm = 1
while len(new_list) != 1:
    lcm = 1
    lcd = 1
    lcd_for_lcm = 1
    for number in new_list[0]:
        if number in new_list[1]:
            lcd *= number
            new_list[1].remove(number)
        pass
    new_list[0:2] = [find_first(lcd)]
    for number in new_list_lcm[0]:
        if number in new_list_lcm[1]:
            lcd_for_lcm *= number
            new_list_lcm[1].remove(number)
        pass

    lcm = int((nnw_given_numbers[0] * nnw_given_numbers[1]) / lcd_for_lcm)
    new_list_lcm[0:2] = [find_first(lcm)]
    nnw_given_numbers[0:2] = [lcm]

print(prime_numbers_answer)
print(lcd)
print(lcm)


"""
LCD different idea without prime numbers


sorted_numbers = sorted(given_number)
number = min(sorted_numbers)
# for num in sorted_numbers:
while number != 1:
    if all([numbers % number == 0 for numbers in sorted_numbers]):
        print(number)
        break
    number -= 1
else:
    print('None')

"""