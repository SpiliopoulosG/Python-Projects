import string


# Lesser of two evens
def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            return b
        else:
            return a
    else:
        if a > b:
            return a
        else:
            return b


# Animal_crackers
def animal_crackers(text):
    words = text.split()
    first_word = words[0].lower()
    second_word = words[1].lower()
    if first_word[0] == second_word[0]:
        return True
    else:
        return False


# Makes Twenty
def makes_twenty(n1, n2):
    if n1 == 20 or n2 == 20:
        return True
    else:
        if (n1 + n2) == 20:
            return True
        else:
            return False


# MacDonald
def old_macdonald(name):
    end_word = ''
    for i in range(len(name)):
        if i == 0 or i == 3:
            end_word += name[i].upper()
        else:
            end_word += name[i]
    return end_word


# Master Yoda
def master_yoda(text):
    my_string = " "
    my_list = text.split()
    my_list = (my_list[2], my_list[1], my_list[0])
    for a in my_list:
        my_string = my_string + ' ' + a
    return my_string


# Almost There
def almost_there(n):
    if (0 <= n - 100 <= 10) or (0 <= n - 200 <= 10):
        return True
    elif (-10 <= n - 100 <= 0) or (-10 <= n - 200 <= 0):
        return True
    else:
        return False


# Has two consecutive 3s
def has_33(nums):
    nums.append(0)
    for i in range(len(nums)):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
        else:
            continue
    return False


# Triple each letter in the word
def paper_doll(text):
    new_word = ''
    for i in text:
        for num in range(0, 3):
            new_word += i
    return new_word


# Blackjack with 3 cards
def blackjack(a, b, c):
    d = a + b + c
    if d > 21 and (a == 11 or b == 11 or c == 11):
        d -= 10
        return d
    elif d > 21:
        return 'Bust'
    else:
        return d


# Summer 69
def summer_69(arr):
    total = 0
    till_next_nine = False
    for i in range(len(arr)):
        if arr[i] != 6 and till_next_nine is False:
            total += arr[i]
        elif arr[i] == 6:
            till_next_nine = True
        elif arr[i] == 9:
            till_next_nine = False
    return total


# 007
def spy_game(nums):
    while_one_0 = False
    for i in range(len(nums)):
        if nums[i] == 0:
            if while_one_0 is False:
                a = i
                while_one_0 = True
            else:
                b = i
        if nums[i] == 7:
            c = i
    if a < b < c:
        return True
    else:
        return False


# Count Primes (Failed)
def count_primes(num):
    prime_counter = 0
    for i in range(num + 1):
        if i == 0 or i == 1:
            prime_counter += 1
        elif i % i == 0 and i % 1 == 0:
            prime_counter += 1
        else:
            continue
    return prime_counter


# Print Big Letters
def print_big(letter):
    dictionary = {'a': "  *  \n * * \n*****\n*   *\n*   *",
                  'b': "**** \n*   *\n**** \n*   *\n**** \n",
                  'c': ' *** \n*   *\n*    \n*   *\n *** \n',
                  'd': '**** \n*   *\n*   *\n*   *\n**** \n',
                  'e': '*****\n*    \n*****\n*    \n*****\n'}
    if letter == 'a':
        return dictionary['a']
    if letter == 'b':
        return dictionary['b']
    if letter == 'c':
        return dictionary['c']
    if letter == 'd':
        return dictionary['d']
    if letter == 'e':
        return dictionary['e']


# Volume of cube
def vol(rad):
    π = 3.14
    return (4 / 3) * π * rad ** 3


# Check whether it's inside the lower and the highest
def ran_check(num, low, high):
    if low <= num <= high:
        print(f'It is between {low} and {high}')
    else:
        print(f'It is not between {low} and {high}')


# Count the amount of lower and upper letters
def up_low(s):
    uppercase = 0
    lowercase = 0
    for letter in s:
        if letter.isupper() is True:
            uppercase += 1
        elif letter.islower() is True:
            lowercase += 1
    print(f'It has {uppercase} capital letters and {lowercase} lower letters')


# Returns unique elements from a list
def unique_list(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
        else:
            continue
    print(new_list)


# Multiply all numbers in the list
def multiply(numbers):
    result = 1
    for i in numbers:
        result *= i
    return result


# Check whether the word is read the same forward and backwards
def palindrome(s):
    if s[::-1] == s:
        return True
    else:
        return False


def i_span_gram(str1):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    for i in str1:
        for n in range(len(alphabet)):
            if i == alphabet[n - 1]:
                alphabet.pop(n - 1)
            else:
                continue
    if alphabet is []:
        return True
    else:
        return False
