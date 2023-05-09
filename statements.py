# Write a Python program that takes a list of strings as input and outputs
#  the number of times each string appears in the list,
#  using a dictionary and conditional statements.
def list_of_strings(str):
    dict_strings = {}
    for s in str:
        if s in dict_strings:
            dict_strings[s] += 1
        else:
            dict_strings[s] = 1
    return dict_strings
print(list_of_strings(["Kenya","Uganda","Tanzania","Kenya"]))


# Write a Python program that takes a list of numbers as input
#  and outputs the median of the numbers 
def median_numbers(numz):
    numz.sort()
    length = len(numz)
    if length % 2 == 0:
        median = (numz[length//2] + numz[length//2 -1])/2
    else:
        median = numz[length//2]
    return median
print(median_numbers([1,2,3,4,5,6,7,8,9]))

# Write a Python program that takes a list of numbers as input and outputs the second 
# largest number in the list using conditional statements and a for loop.
def second_largest_num(nums):
    largest_num = nums[0]
    second_largest_num = nums[0]
    for n in nums:
        if n > largest_num:
            second_largest_num = largest_num
            largest_num = n
        elif n > second_largest_num:
            second_largest_num = n
        return second_largest_num
print(second_largest_num([1,2,3,4,5,6,7,8,9]))




# Write a Python program that takes a year as input and determines if it is a leap year.
def is_leap_year(year):
    if year % 4== 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("is a leap year")
            else:
                print("is not a leap year")
print(is_leap_year(2023))




# Write a Python program that takes a string as input and checks if it is 
# a palindrome (reads the same forwards and backwards), ignoring spaces and punctuation.
# def is_palindrome(name):
#     name = ''.join(n for n in name if n.isalnum()).lower()
#     return name == name[::-1]
# # name = "noon,dad,boat"
# if is_palindrome(name):
#     print(f"{name} is palindrome")
# else:
#     print(f"{name} is not a palindrome")
# print(is_palindrome("noon"))

time = "noon"
time == time
reversed_time == reversed(time)
if list(time)==list(reversed_time):
    print("is palindrome")
else:
    print("is not palindrome")