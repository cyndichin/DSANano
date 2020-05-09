# EFFICIENCY: how well you are using computer resources to get a certain job done
# We said earlier that this Nanodegree program is about how to write code to solve problems and to do so efficiently.
# In the last section, we looked at some basic aspects of solving problems—but we didn't really think too much about whether our solutions were efficient.
# Space and time
# When we refer to the efficiency of a program, we aren't just thinking about its speed—we're considering both the time it will take to run the program and the amount of space the program will require in the computer's memory. Often there will be a trade-off between the two, where you can design a program that runs faster by selecting a data structure that takes up more space—or vice versa.

# Algorithms

# An algorithm is essentially a series of steps for solving a problem. Usually, an algorithm takes some kind of input (such as an unsorted list) and then produces the desired output (such as a sorted list).
# For any given problem, there are usually many different algorithms that will get you to exactly the same end result. But some will be much more efficient than others. To be an effective problem solver, you'll need to develop the ability to look at a problem and identify different algorithms that could be used—and then contrast those algorithms to consider which will be more or less efficient.
# But computers are so fast!
# Sometimes it seems like computers run programs so quickly that efficiency shouldn't really matter. And in some cases, this is true—one version of a program may take 10 times longer than another, but they both still run so quickly that it has no real impact.
# But in other cases, a small difference in how your code is written—or a tiny change in the type of data structure you use—can mean the difference between a program that runs in a fraction of a millisecond and a program that takes hours (or even years!) to run.

# Quantifying Efficiency
# Counting lines of code is not a perfect way to quantify efficiency, and we'll see that there's a lot more to it as we go through the program. But in this case, it's an easy way for us to approximate the difference in efficiency between the two solutions. We can see that if Python has to perform an addition operation 100 times, this will certainly take longer than if it only has to perform an addition operation twice!
## ====================================================================================z
# Input Size and Efficiency
# As the input to an algorithm increases, the time required to run the algorithm may also increase —and different algorithms may increase at different rates.
# Notice that we said may increase. 
# As we saw with the above examples, input size sometimes affects the run-time of the program and sometimes doesn't—it depends on the program.

# The rate of increase
# - Linear relationship (constant rate)
# - Quadratic rate of increase
# and more
# order or rate of increase in the run-time of an algorithm is an essential concept when designing algorithms.

# # Order
# We should note that when people refer to the rate of increase of an algorithm, they will sometimes instead use the term order. Or to put that another way:

# The rate of increase of an algorithm is also referred to as the order of the algorithm.

# For example, instead of saying "this relationship has a linear rate of increase", we could instead say, "the order of this relationship is linear".

# On the next page, we'll introduce something called Big O Notation, and you'll see that the "O" in the name refers to the order of the rate of increase.
## ====================================================================================z
# Big O Notation
# Big O Notation
# When describing the efficiency of an algorithm, we could say something like "the run-time of the algorithm increases linearly with the input size". This can get wordy and it also lacks precision. So as an alternative, mathematicians developed a form of notation called big O notation.

# The "O" in the name refers to the order of the function or algorithm in question. And that makes sense, because big O notation is used to describe the order—or rate of increase—in the run-time of an algorithm, in terms of the input size (n).

# In this next video, Brynn will show some different examples of what the notation would actually look like in practice. This likely won't "click" for you right away, but don't worry—once you've gotten some experience applying it to real problems, it will be much more concrete.
def decode(input):
    create output string
    for each letter in input:
        get new_letter from letter's location in cipher
        add new_letter to output
    return output

# Brynn estimated the efficiency as O(2n + 2). Suppose the input string is "jzqh". What is n in this case? 4
# In the examples we've looked at here, we've been approximating efficiency by counting the number of lines of code that get executed. 
# But when we are thinking about the run-time of a program, what we really care about is how fast the computer's processor is, and how many operations we're asking the processor to perform. 
# Different lines of code may demand very different numbers of operations from the computer's processor. 
# For now, counting lines will work OK as an approximation, but as we go through the course you'll see that there's a lot more going on under the surface.

## ====================================================================================z
# Worst Case and Approximation
# Suppose that we analyze an algorithm and decide that it has the following relationship between the input size, n, and the number of operations needed to carry out the algorithm:

# N = n^2 +5
# Where nn is the input size and NN is the number of operations required.
# For example, if we gave this algorithm an input of 22, the number of required operations would be 2^2 +5 simply 9.

# The thing to notice in the above exercise, is this: In n^2 + 5, the 5 has very little impact on the total efficiency—especially as the input size gets larger and larger. 
# Asking the computer to do 10,005 operations vs. 10,000 operations makes little difference. Thus, it is the n^2n that we really care about the most, and the +5 makes little difference.
# Most of the time, when analyzing the efficiency of an algorithm, the most important thing to know is the order. 
# In other words, we care a lot whether the algorithm's time-complexity has a linear order or a quadratic order (or some other order). 
# This means that very often (in fact, most of the time) when you are asked to analyze an algorithm, you can do so by making an approximation that significantly simplifies things. 
# In this next video, Brynn will discuss this concept and show how it's used with Big O Notation.

## ====================================================================================z
# Efficiency Practice

# Quadratic Example
# O(n^2)

def Quad_Example(our_list):
    for first_loop_item in our_list:
        for second_loop_item in our_list:
            print ("Items: {}, {}".format(first_loop_item,second_loop_item))
            
Quad_Example([1,2,3,4])

# Log Linear Example
# O(nlogn)

# Don't worry about how this algorithm works, we will cover it later in the course!

def Log_Linear_Example(our_list):
    
    if len(our_list) < 2:
        return our_list
    
    else:
        mid = len(our_list)//2
        left = our_list[:mid]
        right = our_list[mid:]

        Log_Linear_Example(left)
        Log_Linear_Example(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                our_list[k]=left[i]
                i+=1
            else:
                our_list[k]=right[j]
                j+=1
            k+=1

        while i < len(left):
            our_list[k]=left[i]
            i+=1
            k+=1

        while j < len(right):
            our_list[k]=right[j]
            j+=1
            k+=1
        
        return our_list

Log_Linear_Example([56,23,11,90,65,4,35,65,84,12,4,0])

# Linear Example
# O(n)
def Linear_Example(our_list):
    for item in our_list:
        print ("Item: {}".format(item))

Linear_Example([1,2,3,4])

# Logarithmic Example
# O(logn)
def Logarithmic_Example(number):
    if number == 0: 
        return 0
    
    elif number == 1: 
        return 1
    
    else: 
        return Logarithmic_Example(number-1)+Logarithmic_Example(number-2)
    
Logarithmic_Example(29)

# Constant Example
# O(1)
def Constant_Example(our_list):
    return our_list.pop()

Constant_Example([1,2,3,4])

# https://www.bigocheatsheet.com/
# https://wiki.python.org/moin/TimeComplexity

## ====================================================================================z
# Space Complexity
# Space Complexity Examples
# When we refer to space complexity, we are talking about how efficient our algorithm is in terms of memory usage. 
# This comes down to the datatypes of the variables we are using and their allocated space requirements. 
# In Python, it's less clear how to do this due to the underlying data structures using more memory for house keeping functions (as the language is actually written in C).
# For example, in C/C++, an integer type takes up 4 bytes of memory to store the value, 
# but in Python 3 an integer takes 14 bytes of space. Again, this extra space is used for housekeeping functions in the Python language.
# For the examples of this lesson we will avoid this complexity and assume the following sizes:
# Type	Storage size
# char	1 byte
# bool	1 byte
# int	4 bytes
# float	4 bytes
# double	8 bytes
# It is also important to note that we will be focusing on just the data space being used and not any of the environment or instructional space.

# Example 1

def our_constant_function():

    x = 3 # Type int
    y = 345 # Type int
    z = 11 # Type int

    answer = x+y+z

    return answer

# So in this example we have four integers (x, y, z and answer) and therefore our space complexity will be 4*4 = 16 bytes. This is an example of constant space complexity, since the amount of space used does not change with input size.

# Example 2

def our_linear_function(n):

    n = n # Type int
    counter = 0 # Type int
    list_ = [] # Assume that the list is empty (i.e., ignore the fact that there is actually meta data stored with Python lists)

    while counter < n:
        list_.append(counter)
        counter = counter + 1

    return list_

# So in this example we have two integers (n and counter) and an expanding list, 
# and therefore our space complexity will be 4*n + 8 since we have an expanding integer 
# list and two integer data types. This is an example of linear space complexity.

# https://commons.wikimedia.org/wiki/File:Comparison_computational_complexity.svg