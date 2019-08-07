#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

'''

import time
import sys


def noOfLetters():
    first_nums = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
            "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["ten", "twenty", "thirty","forty","fifty", "sixty","seventy","eighty","ninety"]

    count = 0
    for num in range(1,1001):
        if num < 20:
            count += len(first_nums[num])

        elif num < 100 and num % 10 == 0:
            count += len(tens[int(num/10 - 1)])

        elif num < 1000 and num % 100 == 0:
            count += len(first_nums[int(num/100)] + "hundred")

        elif num == 1000:
            count += len("onethousand")

        elif num < 100 and num % 10 != 0:
            count += len(tens[int(num//10 - 1)] + first_nums[int(num%10)])

        elif num < 1000:
            if num%100 < 20:
                count += len(first_nums[int(num//100)] + "hundredand" + first_nums[num%100])

            else:
                count += len(first_nums[int(num//100)] + "hundredand" + tens[int(num%100//10 - 1)] +  first_nums[int(num%10)])

    return count

start_time = time.time()
print noOfLetters()
print("--- %s seconds ---" % (time.time() - start_time))
