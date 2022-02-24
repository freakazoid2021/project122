# str1 = 'a' + 'x' if True else 'b'
# print(str1)
#
# string1 = "abc"
# print(id(string1))
# string1 = string1[0] + 'b' + string1[2]
# print(id(string1))
#

# # задание 2
#
# word = input("Word: ")
# vowel = 0
# consonant = 0
#
# for letter in word:
#     if letter.isalpha():
#         if letter.lower() in "aeiouy":
#             vowel += 1
#         else:
#             consonant += 1
# print(vowel)
# print(consonant)
#
# if vowel == consonant:
#     print(vowel)
#
# # задание 4
# import random
# # input count digits
# # input find digit
# # input count --> 4
# for i in range(4):
#     a = int(random.random() * 1000000)
#     str1 += str(a) + " "
# print(a)
# b = str(a)
# looked_dig = input
# for i in str1.split():
#     count += i.count(looked_dig)
# print(count)

# # задание 5
#
# a = input("Введите строку: ")
# element = list(a)
# for i in element:
#     if i.isdigit():
#         print(i, end="")
# # qwert34asfsf ajdj45jnsdk --> 34 45

# input_list = ['a', 'b', 'c']
#
# print(','.join(input_list))
# string1 = "1234567890"
# #            from:to:step
# print(string1[-1::-3])
#
# for i in string1:
#     print(i)
#     print(i * 2)
#
# # 2---------------------
# word = input("Введите текст:")
# vowels = 0
# consonants = 0
# for i in word:
#     letter = i.lower()
#     # if letter in "aouiy":
#     if letter == "a" or letter == "e" or \
#             letter == "i" or letter == "o" or \
#             letter == "u" or letter == "y":
#         vowels += 1
#     else:
#         consonants += 1
# print("Vowels %i\nConsonants %i" % (vowels, consonants))
#
# # 3------------------
# import random
#
# sum = 0
# number1: int = int(input('number1 = '))
# number2: int = int(input('number2 = '))
# for _ in range(7):
#     number3: int = random.randint(1, 20)
#     number4: int = random.randint(1, 20)
#     print(number3, number4)
#     if number1 > number2 and number3 > number4:
#         sum += 1
#     print(sum)
#
# # 4---------------------------
# n = int(input("Сколько будет чисел? "))
# d = int(input("Какую цифру считать? "))
# count = 0
# for i in range(1, n + 1):
#     m = int(input("Число " + str(i) + ": "))
#     while m > 0:
#         if m % 10 == d:
#             count += 1
#         m = m // 10
#
# print("Было введено %d цифр %d" % (count, d))
#
# # 5-----------------------
# str1 = "het 385 @&6 4&&v 4 "
# str_number = ''
# str_digit = ''
# str_other = ''
#
# for i in str1:
#     if i.isalpha():
#         str_number += i
#     elif i.isdigit():
#         str_digit += i
#     else:
#         str_other += i
# print(f"{str_digit}")
#
# # 6-----------------------------
# text = 'HjkfLM'
#
# pair_lower = 0
# pair_upper = 0
#
# for i in range(1, len(text)):
#     print(text[i - 1], text[i])
#     if text[i - 1].islower() and text[i].islower():
#         pair_lower += 1
#     if text[i - 1].isupper() and text[i].isupper():
#         pair_upper += 1
# print('сколько пар (стоят рядом) верхнего регистра:', pair_upper)
# print('сколько пар (стоят рядом) нижнего регистра:', pair_lower)
# print(text, "Длина:", len(text))
# vowels = 0
# consonants = 0
# for i in text:
#     letter = i.lower()
#     if letter == "a" or letter == "e" or \
#             letter == "i" or letter == "o" or \
#             letter == "u" or letter == "y":
#         vowels += 1
#     else:
#         consonants += 1
# print("Vowels %i\nConsonants %i" % (vowels, consonants))

# 1
# import random
#
# n = int(input("Введите число: "))
# numbers = [n // 1_000_000,
#            (n // 100_000) % 10,
#            (n // 10_000) % 10,
#            (n // 1000) % 10,
#            (n // 100) % 10,
#            (n // 10) % 10,
#            n % 10]
# chet = 0
# nechet = 0
#
# for number in numbers:
#     if number % 2 == 0:
#         chet += 1
#     else:
#         nechet += 1
#
# if chet > nechet:
#     print(sum(numbers))
# else:
#     print(numbers[0] * numbers[2] * numbers[5])
#
# #2
# s = input("Введите строку:")
# count = 0
# vowels = set("aeiou")
# for letter in s:
#     if letter in vowels:
#         count += 1
# print("Количество гласных равно:")
# print(count)
#
# #3
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = random.randint(1,20)
# num4 = random.randint(1,20)
#
# # if  in range(7):
#
#
# #4
# n = int(input("Сколько будет введено чисел?: "))
# a = int(input("Какую цифру считать?: "))
# count = 0
# for i in range(1, n + 1):
#     m = int(input("Число " + str(i) + ": "))
#     while m > 0:
#         if m % 10 == a:
#             count += 1
#         m = m // 10
# print("Было введено %a цифр %a" % (count, a))

# 5
# s = input("Введите строку: ")
# l = len(s)
# integ = []
# i = 0
# while i < l:
#     s_int = ''
#     a = s[i]
#     while '0' <= a <= '9':
#         s_int += a
#         i += 1
#         if i < l:
#             a = s[i]
#         else:
#             break
#     i += 1
#     if s_int != '':
#         integ.append(int(s_int))
# print(integ)

# string.split('e', 2)

## Lessons_1
# c = int(input("введите семизначное число"))

# digits = [c // 1000000,
#           (c // 100000) % 10,
#           (c // 10000) % 10,
#           (c // 1000) % 10,
#           (c // 100) % 10,
#           (c // 10) % 10,
#           (c % 10)]
# print(digits[0], digits[1], digits[2], digits[3], digits[4], digits[5], digits[6])

# c = input("enter 7-digits: ")
#
# chetn = 0
# nech = 0
# summer = 0
#
# for i in c:
#     """part even odd numbers"""
#     if int(i) % 2 == 0:
#         chetn += 1
#     else:
#         nech += 1
#     """calculate sum of number"""
#     summer += int(i)
# #   chet > nech  ? true : false
# print(summer if chetn > nech else int(c[0]) * int(c[2]) * int(c[5]))

# print(chetn, nech)
# if chetn > nech:
#     for i in digits:
#         sum += i
#     print(sum)
# else:
#     print(digits[0] * digits[2] * digits[5])


### lessona_2
# aaaaaaaaaa==H nj*(898
# text = str(input("введите текст"))
#
# glass = "AIOEUaioeu"
# s = 0
# d = 0
# for i in text:
#     if i in glass:
#         s+=1
#     else:
#         d+=1
# print("глассные = ", s)
# print("согласные= ", d)
#
# if s==d:
#    не доделал в случае если равно не пойму как сделать


### lessons_3
# import random
# sum = 0
# a=0
# iteration4_c = 0
# iteration4_d = 0
# for i in range(7):
#     a = int(input("первое число"))
#     b = int(input("второе число"))
#     c = random.randint(1,20)
#     d = random.randint(1,20)
#     print(c,d)
#     # if a + b > c + d:
#     if a>c and b>d:
#         sum+=1
#     if i == 3:
#         iteration4_c = c
#         iteration4_d = d
#
# print(sum)
# ## не понял как вывести четвертую итерацию
#
#
#


### lessons_4
# import random
#
# n = int(input("сколько чисел будет сгенерированно"))
# s = int(input("какую цифру искать"))
#
# coll = 0
#
# for i in range(1,n+1):
#     d = random.randint(0,999)
#     print(d)
#     while d>0:
#         if d%10 == s:
#             coll+=1
#         d=d//10
# print(coll)
### lessons_5
# s = input()
# l = len(s)
# integer = []
# i = 0
# while i < l:
#     s_int = ''
#     a = s[i]
#     while '0' <= a <= '9':
#         s_int += a
#         i += 1
#         if i < l:
#             a = s[i]
#         else:
#             break
#     i += 1
#     if s_int != '':
#         integer.append(int(s_int))
#
# print(integer)
# s = input("Введите строку: ")
# l = len(s)
# integ = []
# i = 0
# while i < l:
#     s_int = ''
#     a = s[i]
#     while '0' <= a <= '9':
#         s_int += a
#         i += 1
#         if i < l:
#             a = s[i]
#         else:
#             break
#     i += 1
#     if s_int != '':
#         integ.append(int(s_int))
# print(integ)

import random

# test_1
# num = input("Enter 7 digit number: ")
# count = 0
# sum_ = 0
# for i in range(7):
#     sum_ += int(num[i])
#     if int(num[i]) % 2 == 0:
#         count += 1
# prod = int(num[0]) * int(num[2]) * int(num[5])
#
# if count > 3:
#     print(sum_)
# else:
#     print(prod)
# print("____________________________________\n")
#
#
# # test_2
# string = input("Enter some text: ").lower().replace(' ', '')
# vowels_count = 0
# vowels = ''
# for i in string:
#     if i in ['a', 'e', 'i', 'o', 'u', 'y']:
#         vowels += i + ' '
#         vowels_count += 1
# consonants_count = len(string) - vowels_count
#
# msg = ""
# if consonants_count == vowels_count:
#     msg = f"{vowels}"
# else:
#     msg = f"Vowels: {vowels_count} \nConsonants: {consonants_count}"
#
# print(msg)
# print("____________________________________\n")
#
#
# # test_3
# cc = 0
# dd = 0
# count = 0
# i = 0
# while i < 8:
#     a = int(input("Enter first number from 1 to 20: "))
#     b = int(input("Enter second number from 1 to 20: "))
#     c = random.randrange(1, 21)
#     d = random.randrange(1, 21)
#     if a + b > c + d:
#         count += 1
#     if i == 3:
#         cc += c
#         dd += d
#     i += 1
# print(f"Random number: {7 - count} VS introduced number: {count} \nRandom number in 4 iteration: {cc}, {dd}")
# print("____________________________________\n")


# test_4
# num_count = int(input("Enter quantity numbers: "))
# dig = (input("Enter found digit: "))
# num_string = ''
# count_ = 0
# i = 0
# while i < num_count:
#     num = random.randrange(1, 1000)
#     print(num)
#     count_ += str(num).count(dig)
#     i += 1
# # print(num_string.count(dig))
# # for j in num_string:
# #     if j == dig:
# #         count += 1
# print(count_)
# print("____________________________________\n")


# test_5
# numbers = ''
# string = input("Enter some string: ")
# for i in string:
#     if i.isdigit():
#         numbers += i
#     else:
#         numbers += " "
# print(numbers.split())
# print("____________________________________\n")

# HaaaHJD --> Ha aa HJ D
# test_6
# word = input("Enter word: ")
# i = 0
# vowels_count = 0
# upper_count = 0
# lower_count = 0
# while i < len(word)-1:
#     if word[i].islower() and word[i + 1].islower():
#         lower_count += 1
#         i += 1
#     if word[i].isupper() and word[i + 1].isupper():
#         upper_count += 1
#         i += 1
#     i += 2
# for j in word:
#     if j.lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
#         vowels_count += 1
# consonants_count = len(word) - vowels_count
# print(f"Pairs of letters in uppercase: {upper_count} \nPairs of lowercase letters: {lower_count}"
#       f"\nVowels letter: {vowels_count} \nConsonant letters: {consonants_count} \nWord length: {len(word)}")
list_ = [1, 2, 3, 4, 5][:]
list_2 = list_[:]
print(type(list_2))
