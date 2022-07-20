# number1= int(input('inter number 1:'))
# number2= int(input('inter number 2:'))
# number3= int(input('inter number 3:'))
# print('sum of {},{} and {} is: {}'.\
# format(number1,number1,number1,(number1\
#                               +number2+number3)))

# name="shema ERIC"

# for n in range(2,15,2):
#   print(n)
# else:
#   print('done !!!!')


"""
# 1.

userName = input("inter you name:")
for n in userName:
    print(n, '*', end='')
"""

"""
# 2 sum  of 10 number

mySum = 0
for i in range(1,11):
    mySum = mySum + i
else:
   print("the sum of first 10 number is:{}".format(mySum))
"""

"""
# 3 odd / even
print('odd numbers:', end='\t')
for i in range(1, 100):
    print(i, end=',')
"""

"""
#4 divisible by 7 and multiple of 5 btn 500-1400

count = 0
for i in range(499,1401):
    if i % 7 == 0 or i % 5 == 0:
        count = count+1
print(count) 
"""

"""
#5 not divisible by 5

for i in range(1,101):
    if i % 5 == 0:
        continue
    else:
        print(i, end=",")
"""

# print("\"he said that \"Kigali is Beautiful\"\"")

"""
word1 = list(input('Enter the word:'))
word2 = word1.copy()
word2.reverse()
if str(word1).lower() == str(word2).lower():
    print('parindrom')
else:
    print('not parindrom')
"""
""" 
num_list = [10, 20, 30, 40, 99, 7, 33, 88, 66, 100, 101]
odd = []
even = []
for i in num_list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("source list:{}".format(num_list))
print("even list:{}".format(even))
print('odd list:{}'.format(odd))

"""

"""
num_list = [10, 20, 30, 40, 99, 7, 33, 88, 66, 100, 101]
odd = [i for i in num_list if i%2 != 0 ]
even = [i for i in num_list if i%2 == 0]
double = [i*2 for i in num_list]
print("even list:{}".format(even))
print('odd list:{}'.format(odd))
print('double list:{}'.format(double))
"""

"""
city = ['k', 'i', 'g', 'a', 'l', 'i']
city_cap = [i.upper() for i in city]

print(city_cap)
"""

"""
sum1 = 0
numbers =[1,2,3,4,5,6,7,'e','shema']
for i in numbers:
    if type(i) == int:
        sum1 += i
print('the sum is:{}'.format(sum1))
"""

# 1 sum of all items in  list

list1 = [1, 2, 3]
total = 0
for n in list1:
    total += n
# print(total)


# 2 largest in list
list2 = [1, 2, 3, 6, 8, 9, 10]
largest = list2[0]
for n in list2:
    if largest < n:
        largest = n
# print(largest)

# 3 find average in list

list3 = [1, 2, 3]
total = 0
for n in list1:
    total += n
# print(total/len(list3))

# 4 total number of integer in list

list4 = [1.5, 2, 3, 3.4, 1]
totalInt = 0
for n in list4:
    if type(n) == int:
        totalInt += 1
# print(totalInt)

# 5 find odd/ enven using

list5 = [1.5, 2, 3, 3.4, 1]

oddNumber = [n for n in list5 if n % 2 != 0]
evenNumber = [n for n in list5 if n % 2 == 0]
# print('odd:{}'.format(oddNumber))
# print('even:{}'.format(evenNumber))

# 6 reverse list using slicing

list6 = [1.5, 2, 3, 3.4, 1]

# print(list6[-1: :-1])

# 7 remove duplicate in a list

list7 = [10, 10, 10, 20, 20, 30, 40, 40, 50, 70, 90]
result = set(list7)
# print(result)

# 8 print midle word or two middle words

"""
sentence = input("inter the sentence you want:")
sentenceList = sentence.split(" ")
length = len(sentenceList)
if length % 2 == 0:
    print(sentenceList[int(length/2)-1] + " " + sentenceList[int(length/2)])
else:
    print(sentenceList[int(length / 2)])
"""

# unpacking a list of a tuple
list9 = [10, 10, 10, 20, 20, 30, 40, 40, 50, 70, 90]
# [...a,b]=list9
*a, b = list9

# print(b)

dct = {'name': 'shema', 'age': 12}
value = 'name'

# print(dct.get(value))


# dictionary
# print(range(0,0.0))
# command line argument

"""
in terminal we use  python main.py 10 20
import sys

print(sys.argv[1])
print(sys.argv[0]) to display script name
"""

"""
import sys as sys1

print(sys1.argv[1])
print(sys1.argv[0])
"""

# 1 guess game


import random

reward = {
    '1': 10000,
    '2': 5000,
    '3': 3000,
    '4': 2000,
    '5': 1000
}
count = 6
for i in count:
    userNumber = int(input('guess number between 1 and 10:'))
    rand = random.randrange(1,10)
    print('system number is:{}'.format(rand[i]))
    if userNumber == rand:
        print('congratulation you win {} !!!!'.format(reward[count]))
        break
    else:
        print('Oops ! you fail')
        continue


# 2 calculating area of circle and volume of cone and sylinder

"""
circle = π · r2
volume of cylinder = π · r2 · h
volume of cone = (1/3) · π · r2 · h
"""

import math

#radius = int(input('inter radius:'))
#height = int(input('inter height:'))


def circle_area(radius):
    print('circle area is:{}'.format(math.pi * (radius ** 2)))


def cylinder_volume(radius, height):
    print('cylinder volume is:{}'.format(math.pi * (radius ** 2) * height))


def cone_volume(radius, height):
    print('cone volume is:{}'.format((1 / 3) * math.pi * (radius ** 2) * height))

"""
circle_area(radius)
cylinder_volume(radius, height)
cone_volume(radius, height)
"""


#3 state name as input

distr_dic = {
    'gasabo': {
        'CNname': 'gasabo cn',
        'capital': 'capit1',
        'population': 1003500
    },
    'kicukiro': {
            'CN_name': 'kicukiro cn',
            'capital': 'kicukiro_capital',
            'population': 1004500
        },
    'nyarugenge': {
                'CN_name': 'nyarugenge cn',
                'capital': 'nyarugenge_capital',
                'population': 10023456
            },
}

dist_name = input('enter district name:')

def find_details(dist_name):
    print(distr_dic[dist_name])

find_details(dist_name)

#4 compare time of execution between factorial of 899 and recursion

