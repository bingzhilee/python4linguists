# -*- coding: utf-8 -*-
"""TP3_data-structure_for.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fbzP4tvzkK4q4OaF1Os6bHujkFVjTdBe

# **TP3 Data Structure and `for` loop**

**0.1** Print all the numbers in the list `age` using `for` loop.
"""

age = [12,30,45,60,70,90]

for x in age:
  print(x)

"""**0.2** Two ways to print all the names in the list `friends` using `for` loop. """

friends = ["Alice","Lily","Lucy","Max","Harry","Jerry"]
# in clause
for friend in friends:
  print(friend) 
# range() method
for i in range(len(friends)):
  print(friends[i])

"""**0.3** Print all the letters in the string `s` using `for` loop. (same as 0.2)

"""

s = "abracadabra"
for letter in s:
  print(letter)

"""## $\color{blue}{\text{Exercise 1 - The Smallest Value }}$
How would we change this to make it find the smallest value in the list?

"""

lst = [9, 41, 12, 3, 74, 15]
largest_so_far = -999
print('Before', largest_so_far)
for the_num in lst :
   if the_num > largest_so_far :
      largest_so_far = the_num
   print(largest_so_far, the_num)

print('After', largest_so_far)

lst = [9, 41, 12, 3, 74, 15]
smallest_so_far = 999
print('Before', smallest_so_far)
for the_num in lst :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
   print(smallest_so_far, the_num)

print('After', smallest_so_far)

"""## $\color{blue}{\text{Exercise 2 - Filtering in a Loop }}$
Display all the words of length at most 4 in the `str_lst`
"""

# example from lecture 3 for catching all the values greater than 20 in the following list
for value in [9, 41, 12, 3, 74, 15] :
    if value > 20:
 	    print('Large number',value)

str_lst = ['We', 'use', 'an', 'if', 'statement', 'in', 'the', 'loop', 'to', 'catch',
           'the', 'values', 'we', 'are', 'looking', 'for']
for word in str_lst:
  if len(word)<5:
    print(word)

"""## $\color{blue}{\text{Exercise 3 - Counting in a loop }}$
**3.1** Ask users to enter an English word then count and display the vowels in that word.(Using `for` loop)

Expected output:
```
Please enter an English word: Loop
There are 2 vowels in the string "Loop".
```


"""

# 1.define a list of vowels
vowels = ["a","e","i","o","u"]
# 2.get user's input word
word = input('PLease enter an English word: ')
# 3.introduce a count variable, use `for` loop to add one to it each time we have a vowel
nb_vowels = 0
for letter in word: 
  if letter in vowels:
    nb_vowels+=1
print("There are {0} vowels in the string '{1}'.".format(nb_vowels,word))

"""**3.2** Using `dictionnary` to count the occurrence of each letter in a given word.

expected output:
```
Please enter a string: abracadabra
{'a': 5, 'b': 1, 'r': 2, 'c': 1, 'd': 1}
```

**Hint:** we use `in` statement to check if the item `'a'` is a key in a dictionary `d`:

+ if `'a'` is a key in the dictinary `d`, we can update its value by `d['a'] = d['a'] + 1 `

+ if not, we assign a new key with value `1` : `d['a'] =1`
"""

word = input("Please enter a word: ")
d = dict()
for letter in word:
  if letter in d:
    d[letter]+=1
  else:
    d[letter]=1
print(d)