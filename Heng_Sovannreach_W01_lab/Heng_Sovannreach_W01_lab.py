'''
------------------
    Exercise 1
------------------
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a+b)
print("Difference: ", a-b)
print("Product: ", a*b)
print("Quotient: ", float(a / b))


'''
------------------
    Exercise 2
------------------
'''

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))
if first_number > second_number and first_number > third_number:
    print(f"The largest number is {first_number}")
elif second_number > first_number and second_number > third_number:
    print(f"The largest number is {second_number}")
elif third_number > first_number and third_number > second_number:
    print(f"The largest number is {third_number}")
else:
    print("All equal") 



'''
------------------
    Exercise 3
------------------
'''

for i in range(1,101):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)


'''
------------------
    Exercise 4
------------------
'''


def factorial(num):
    sum = 1
    for i in range(1,num+1):
        sum *= i
    return sum


num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")

'''
------------------
    Exercise 5
------------------
'''

string = input("Enter a string: ")
is_palindrome = True
for i in range( 0, len(string) ):
      if string[i] != string[len(string) - i - 1]:
                 is_palindrome = False

if is_palindrome :
    print(f"{string} is a palindrome")
else :
    print(f"{string} is not a palindrome")
