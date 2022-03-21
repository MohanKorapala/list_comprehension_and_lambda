# numbrs 1 thru 9
# no commas between the 3 sections(expression,iteration, and condiditon)
x =[i for i in range(10)]
print(x)

# adding an expression - square of each number
squares = [i**2 for i in range(10)]
print(squares)

# multiply each element by 3
list1 = [3,4,5]
multiplied = [i*3 for i in list1]
print(multiplied)

# word manipulation
listofwords = ['this','is','a','list','of','words']
fletter = [word[0] for word in listofwords]
print(fletter)

# lowercase the letters
list1 = ['A','B','C']
list2 = [x.lower() for x in list1]
print(list2)

# adding in an IF condiditon
# all even numbers from 0-4 (sqarued)
new_range = [i*i for i in range (5) if i%2 ==0]
print(new_range)

string = "Hello 12345 World"
numbers = [x for x in string if x.isdigit()]
letters = [x for x in string if x.isalpha()]
print(numbers)
print(letters)

#old way
numbers = []
for x in string:
    if x.isdigit():
        numbers.append(x)

# using a file
myfile = open('test.txt','r')
result = [i.rstrip('\n') for i in myfile if 'line 3' in i]
print(result)

# using functions
def double(x):
    return x*2

print(double(10))

mynumbers = [double(x) for x in range(10)]
print(mynumbers)

#for even numbers only
mynumbers = [double(x) for x in range(10) if x%2==0]
print(mynumbers)

# you can add more aruguments
result = [x+y for x in [10,30,50] for y in [20,40,60]]
print(result)