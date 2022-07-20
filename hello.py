#number1= int(input('inter number 1:'))
#number2= int(input('inter number 2:'))
#number3= int(input('inter number 3:'))
#print('sum of {},{} and {} is: {}'.\
     # format(number1,number1,number1,(number1\
       #                               +number2+number3)))

#name="shema ERIC"

#for n in range(2,15,2):
 #   print(n)
#else:
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



#print("\"he said that \"Kigali is Beautiful\"\"")

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

#1 sum of all items in  list

list1 = [1, 2, 3]
total = 0
for n in list1:
    total += n
#print(total)


#2 largest in list
list2 = [1, 2,3,6,8,9,10]
largest = list2[0]
for n in list2:
    if largest < n:
        largest = n
#print(largest)

#3 find average in list

list3 = [1, 2, 3]
total = 0
for n in list1:
    total += n
 #print(total/len(list3))

#4 total number of integer in list

list4 = [1.5, 2, 3, 3.4, 1]
totalInt = 0
for n in list4:
    if type(n) == int:
        totalInt += 1
#print(totalInt)

#5 find odd/ enven using

list5 = [1.5, 2, 3, 3.4, 1]

oddNumber = [n for n in list5 if n % 2 != 0]
evenNumber = [n for n in list5 if n % 2 == 0]
#print('odd:{}'.format(oddNumber))
#print('even:{}'.format(evenNumber))

#6 reverse list using slicing

list6 = [1.5, 2, 3, 3.4, 1]

#print(list6[-1: :-1])

#7 remove duplicate in a list

list7 = [10,10,10,20,20,30,40,40,50,70,90]
result = set(list7)
#print(result)

#8 print midle word or two middle words

sentence = input("inter the sentence you want:")
sentenceList = sentence.split(" ")
length = len(sentenceList)
if length % 2 == 0:
    print(sentenceList[int(length/2)-1] + " " + sentenceList[int(length/2)])
else:
    print(sentenceList[int(length / 2)])






