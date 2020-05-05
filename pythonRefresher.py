## CONTROL STRUCTURES REVIEW

## Iteration with Loops
## For Loop, For-Each Loop, While 

# Examples of iteration with for loops.

my_list = [0, 1, 2, 3, 4, 5]

# Print each value in my_list. Note you can use the "in" keyword to iterate over a list.
for item in my_list:
    print('The value of item is: ' + str(item))

# Print each index and value pair.
for i, value in enumerate(my_list):
    print('The index value is: ' + str(i) + '. The value at i is: ' + str(value))

# Print each number from 0 to 9 using a while loop.
i = 0
while(i < 10):
    print(i)
    i += 1

# Print each key and dictionary value. Note that you can use the "in" keyword 
# to iterate over dictionary keys.
my_dict = {'a': 'jill', 'b': 'tom', 'c': 'tim'}
for key in my_dict:
    print(key + ', ' + my_dict[key])

# Remember that Python requires correct indentation for code blocks to be interpreted correctly. 
# Indentation for a block is usually four spaces, or one tab length.

## Conditional Statements: bool logic to help guide decision process (true or false)
## Statements are structured using comparison operators: greater than (>), less than (<), and equal to (==).
## IF, ELSE, ELIF
num = 5
if num < 5:
    print('The number is smaller than 5.')
elif num == 5:
    print('The number equals 5.')
else:
    print('The number is greater than 5.')

## The number equals 5.

### EXERCISE 1
def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    smallest_pos = None
    for num in in_list:
        if num > 0:
            # Note: we use a logical "or" in this solution to form 
            # the conditional statement, although this was
            # not introduced above. 
            if smallest_pos == None or num < smallest_pos:
                smallest_pos = num
    return smallest_pos

# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

print(smallest_positive([-6, -9, -7]))
# Correct output: None

print(smallest_positive([]))
# Correct output: None

### EXERCISE 2
# This exercise uses a data structure that stores Udacity course information.
# The data structure format is:

#    { <semester>: { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }
courses = {
    'spring2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'fall2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'spring2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                        'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }


def when_offered(courses, course):
    # TODO: Fill out the function here.
    semesters = []
    for semester in courses:
        if course in courses[semester]:
            semesters.append(semester)
    # TODO: Return list of semesters here.
    return semesters

print(when_offered(courses, 'cs101'))
# Correct result: 
# ['fall2020', 'spring2020']

print(when_offered(courses, 'bio893'))
# Correct result: 
# []

## ====================================================================================z
## FUNCTIONS + GENERATORS
## Python Functions
#  Python involves a function declaration def that takes one or more values, 
#  and a return that returns one or more values.
# Note: In Python every function returns a value. In case you do not specify a return value explicitly, Python will return None from that function.

# Example function 1: return the sum of two numbers.
def sum(a, b):
    return a+b

# Example function 2: return the size of list, and modify the list to now be sorted.
def list_sort(my_list):
    my_list.sort()
    return len(my_list),  my_list

## ====================================================================================z
## Python Generators
# A generator in Python is similar to a function except instead of returning a value and exiting a process, 
# a generator will pause the process, saving its state for next time. 
# The biggest difference between a function and generator from a code perspective is one word: 
# return is changed to yield.


# Useful when dealing with very large collections of data that you don’t want to store in memory all at once. 
# It’s also very useful for dealing with extremely large or even infinite series.
# Below is an example of how to use a generator to print even numbers. 
# Printing all even numbers at once would take an infinite amount of time, but the generator allows the process to pause, and go back to creating even numbers when needed.
# To create the next successive even number simply call next() on the generator object, and it will yield the next iteration. After yield is called, everything in the state of the generator function freezes, and the value is returned. When the generator is called again with next(), 
# it picks back up right where it stopped at yield from before.

# Definition of the generator to produce even numbers.
def all_even():
    n = 0
    while True:
        yield n
        n += 2

my_gen = all_even()

# Generate the first 5 even numbers.
for i in range(5):
    print(next(my_gen))

# Now go and do some other processing.
do_something = 4
do_something += 3
print(do_something)

# Now go back to generating more even numbers.
for i in range(100):
    print(next(my_gen))

### EXERCISE 1
# In the following exercise, you will create a generator fact_gen() that generates factorials. 
# For a number n, n factorial is denoted by n!, and it is the product of all positive integers less than or equal to n.
def prod(a,b):
    # TODO change output to the product of a and b
    return a*b

def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        # TODO: update i and n
        # Hint: i is a successive integer and n is the previous product
        i += 1
        n = output


# Test block
my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))

# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120

### EXERCISE 2
# In the next exercise, you will write a function that checks sudoku squares for correctness.
# Sudoku is a logic puzzle where a game is defined by a partially filled 9 x 9 square of digits where each square contains one of the digits 1, 2, 3, 4, 5, 6, 7, 8, 9. For this question we will generalize and simplify the game.
# Define a procedure, check_sudoku, that takes as input a square list of lists representing an n x n sudoku puzzle solution and returns the boolean True if the input is a valid sudoku square and returns the boolean False otherwise.
# A valid sudoku square satisfies these two properties:
# Each column of the square contains each of the whole numbers from 1 to n exactly once.
# Each row of the square contains each of the whole numbers from 1 to n exactly once.
# You may assume that the input is square and contains at least one row and column.

# An example solution for the check_sudoku() function
def check_sudoku(square):
    for row in square:
        # Create a list with the integers 1, 2, ..., n.
        # We will check that each number in the row is in the list
        # and remove the numbers from the list once they are verified
        # to ensure that each number only occurs once in the row.
        check_list = list(range(1, len(square[0]) + 1))
        for i in row:
            if i not in check_list:
                return False
            check_list.remove(i)
    for n in range(len(square[0])):
        # We do the same here for each column in the square.
        check_list = list(range(1, len(square[0]) + 1))
        for row in square:
            if row[n] not in check_list:
                return False
            check_list.remove(row[n])
    return True

#print(check_sudoku(incorrect))
#>>> False

#print(check_sudoku(correct))
#>>> True

#print(check_sudoku(incorrect2))
#>>> False

#print(check_sudoku(incorrect3))
#>>> False

#print(check_sudoku(incorrect4))
#>>> False

#print(check_sudoku(incorrect5))
#>>> False

## ====================================================================================z
## CLASSES REVIEW
## A class is a structure in object-oriented programming that allows functions and related data to be grouped together.
# In a Python class, an important concept is self, which is used to reference a class instance's own variables and functions from within the class definition. 
# Another important and commonly used function definition is the class initializer, def __init__(self). The body of the initializer is where instance variable definitions should be added, and the initializer initializes all the variables once an instance of the class is created.
#  Also, any input variables that a class needs to have, such as a name for the person can be passed into initializer function.

# Examples of Python Classes
# Below is an example of a basic Person class. 
# The class has two variables for name and age, along with three functions for initializing the class, incrementing the person’s age, and getting the person’s name.

class Person:
    def __init__(self, name, age):
        self.person_name = name
        self.person_age = age

    def birthday(self):
        self.person_age += 1

    def getName(self):
        return self.person_name

# create an instance of the Person class and access Person's name
bob = Person('Bob', 32)
print(bob.getName())
# prints Bob

# Currently, we have one function for getting the class’s variable. This is called an Accessor. 
# The other function that the class has is actually modifying one of the class’ variables, and that is called a Mutator. 
# We can make our Person older by calling birthday()

bob.birthday()
print(bob.person_age)
# prints 33

# The birthday function call successfully increments the age of our Person. 
# Also note that we can directly get the age of bob without using a function call. 
# This is because the Person class variables are defined as public, so we can directly access them without a function call. 
# If instead we wanted the Person’s age variable to be private to the class, in Python 3 we could put double underscores in front of the variable: __person_age. 
# Then we would have to use a function call in order to retrieve it.

### EXERCISE 1
# Now let's assume that the current month is April, and you want to use a Person class to help make use of information about the friends in your contacts list. In particular, you'd like to increment the age of all of your friends with birthdays in April. You would also like to know who they are, along with their current ages, so you can send them birthday cards. Finally, you would also like to figure out which month has the most friends with birthdays, so you can budget for all of the birthday cards you will need to buy.

# In the following exercise, the Person class will be provided for you, and you will be working with a list of instances of the class, representing friends in your contacts. This list is stored in the variable people.

# To complete the exercise, you will need to do two things:

# Complete the function get_april_birthdays(people). This function should return a dictionary with each name of your friend with an April birthday as a key, and their updated age as the value.
# Complete the function get_most_common_month(people). This function should return the name of the month with the most number of birthdays among your friends.
# There is some testing code provided in test(), and there are more specific TODO instructions in each of the two functions mentioned.

class Person:
    def __init__(self, name, age, month):
        self.name = name
        self.age = age
        self.birthday_month = month
        
    def birthday(self):
        self.age += 1

def create_person_objects(names, ages, months):
    my_data = zip(names, ages, months)
    person_objects = []
    for item in my_data:
        person_objects.append(Person(*item))
    return person_objects

def get_april_birthdays(people):
    # TODO:
    # Increment "age" for all people with birthdays in April.
    # Return a dictionary "april_birthdays" with the names of
    # all people with April birthdays as keys, and their updated ages 
    # as values. See the test below for an example expected output.
    april_birthdays = {}
    for person in people:
        if person.birthday_month == 'April':
            person.age += 1
            april_birthdays[person.name] = person.age
            
    return april_birthdays

def get_most_common_month(people):
    # TODO: Use the "months" dictionary to record counts of 
    # birthday months for persons in the "people" data.
    # Return the month with the largest number of birthdays.
    months = {'January':0, 'February':0, 'March':0, 'April':0, 'May':0, 
              'June':0, 'July':0, 'August':0, 'September':0, 'October':0,
              'November':0, 'December':0}

    for person in people:
        months[person.birthday_month] += 1

    max_month = None
    max_value = 0
    for key in months.keys():
        if months[key] > max_value:
            max_value = months[key]
            max_month = key

    return max_month

def test():
    # Here is the data for the test. Assume there is a single most common month.
    names = ['Howard', 'Richard', 'Jules', 'Trula', 'Michael', 'Elizabeth', 'Richard', 'Shirley', 'Mark', 'Brianna', 'Kenneth', 'Gwen', 'William', 'Rosa', 'Denver', 'Shelly', 'Sammy', 'Maryann', 'Kathleen', 'Andrew', 'Joseph', 'Kathleen', 'Lisa', 'Viola', 'George', 'Bonnie', 'Robert', 'William', 'Sabrina', 'John', 'Robert', 'Gil', 'Calvin', 'Robert', 'Dusty', 'Dario', 'Joeann', 'Terry', 'Alan', 'Rosa', 'Jeane', 'James', 'Rachel', 'Tu', 'Chelsea', 'Andrea', 'Ernest', 'Erica', 'Priscilla', 'Carol', 'Michael', 'Dale', 'Arthur', 'Helen', 'James', 'Donna', 'Patricia', 'Betty', 'Patricia', 'Mollie', 'Nicole', 'Ernest', 'Wendy', 'Graciela', 'Teresa', 'Nicole', 'Trang', 'Caleb', 'Robert', 'Paul', 'Nieves', 'Arleen', 'Milton', 'James', 'Lawrence', 'Edward', 'Susan', 'Patricia', 'Tana', 'Jessica', 'Suzanne', 'Darren', 'Arthur', 'Holly', 'Mary', 'Randal', 'John', 'Laura', 'Betty', 'Chelsea', 'Margaret', 'Angel', 'Jeffrey', 'Mary', 'Donald', 'David', 'Roger', 'Evan', 'Danny', 'William']
    ages  = [17, 58, 79, 8, 10, 57, 4, 98, 19, 47, 81, 68, 48, 13, 39, 21, 98, 51, 49, 12, 24, 78, 36, 59, 3, 87, 94, 85, 43, 69, 15, 52, 57, 36, 52, 5, 52, 5, 33, 10, 71, 28, 70, 9, 25, 28, 76, 71, 22, 35, 35, 100, 9, 95, 69, 52, 66, 91, 39, 84, 65, 29, 20, 98, 30, 83, 30, 15, 88, 89, 24, 98, 62, 94, 86, 63, 34, 23, 23, 19, 10, 80, 88, 67, 17, 91, 85, 97, 29, 7, 34, 38, 92, 29, 14, 52, 94, 62, 70, 22]
    months = ['January', 'March', 'January', 'October', 'April', 'February', 'August', 'January', 'June', 'August', 'February', 'May', 'March', 'June', 'February', 'August', 'June', 'March', 'August', 'April', 'April', 'June', 'April', 'June', 'February', 'September', 'March', 'July', 'September', 'December', 'June', 'June', 'August', 'November', 'April', 'November', 'August', 'June', 'January', 'August', 'May', 'March', 'March', 'March', 'May', 'September', 'August', 'April', 'February', 'April', 'May', 'March', 'March', 'January', 'August', 'October', 'February', 'November', 'August', 'June', 'September', 'September', 'January', 'September', 'July', 'July', 'December', 'June', 'April', 'February', 'August', 'September', 'August', 'February', 'April', 'July', 'May', 'November', 'December', 'February', 'August', 'August', 'September', 'December', 'February', 'March', 'June', 'December', 'February', 'May', 'April', 'July', 'March', 'June', 'December', 'March', 'July', 'May', 'September', 'November']
    people = create_person_objects(names, ages, months)

    # Calls to the two functions you have completed.
    print(get_april_birthdays(people))
    print(get_most_common_month(people))

test()
# Expected result:
# {'Michael': 11, 'Erica': 72, 'Carol': 36, 'Lisa': 37, 'Lawrence': 87, 'Joseph': 25, 'Margaret': 35, 'Andrew': 13, 'Dusty': 53, 'Robert': 89}
# August
