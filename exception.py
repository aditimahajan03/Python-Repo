# how to handle errors in python
# try accept blocks to handle exceptions that are raised in our programs
# as a good programmer you should always anticipate
# these kind of exceptions and handle them properly.
try:
    age = int(input('Age: '))
    income = 4000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("invalid value ")
except ValueError:
    print("invalid value")

