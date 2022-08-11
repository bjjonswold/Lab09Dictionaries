# Lab09Dictionaries
Dictionaries Warmup Lab

# Step 1 -- Self Explanation
Please take a look at the collegeAddress dictionary and answer the following questions. 

1. What are the keys listed in the dictionary named collegeAddress? You can verify the keys by printing them out in the program using the dict.keys() method.
2. What happens if you try to add a second 'State' key into the schoolAddress dictionary? Answer as a comment within your program.
3. Can you add in a key that is a number instead of a string? If you can, add a key that is an int or float type to the dictionary. 
4. Can you change the value of the Building Name key in the dictionary? If so, change it to the dorm you lived in Freshman year. However, don't manually change the value within the dictionary rather change the value by adding a new line of code.
5. What is the length of the dictionary? You can verify the length by printing it out using the len(dict) method. 

# Step 2 -- Creating a Dictionary Containing Dictionaries
First, fill in the two dictionaries provided right under the comment STEP 2 using the exact same 5 key names provided in collegeAddress dictionary at the beginning of this lab. These may be real buildings or buildings with fake values. 

After you have filled in the two additional dictionaries, you are going to fill in a dictionary that contains the three dictionaries you have already dealt with in this program. The name of the keys and the first value have been provided for you. Please fill out the remaining you values. 

# Submitting the Assignment
Make sure to submit the assignment for grading! If you haven't clicked through the canvas link in a while, we would suggest clicking through it again before submitting.

# Reminder on Dictionaries
Dictionaries in Python, sometimes referred to as maps in other languages, are a data-structure used to store data as key:value pairs. A dictionary is changeable and does not allow for duplicate keys. Dictionaries are written using curly brackets with each key/value pair is seperated by a semicolon and different pairs are seperated by a comma. An example dictionary is shown below.

```python
dictionary = {
'key':'value',
'sport': 'pickleball',
'color': 'red',
'mascot': 'zebra',
'fans': 4
}
```

I can change a value by reassigning the key to something else. For example, I can change the value assigned to the 'color' key like this:
```python
dictionary['color'] = 'blue'
```
The dictionary would now contain the key/value pair 'color':'blue'.

As stated above, keys are not allowed to be duplicated. If I try to duplicate a key in a dictionary, the second key/value pair will overwrite the first key/value pair. For example,
```python
cheeseTouch = {
'wowza': 'Zoo Wee Mama',
'wowza': 'Greg Heffley'
}
print(cheeseTouch)
```
will print {'wowza': 'Greg Heffley'} and nothing else. 

The length of a dictionary is determined by adding all the key/value pairs. You can use the len() function to print this out.
```python
presidentsThisCentury = {
'firstDemocrat': 'Bill Clinton',
'firstRepublican': 'George W. Bush',
'secondDemocrat': 'Barack Obama',
'secondRepublican': 'Donald J. Trump',
'thirdDemocrat': 'Joseph R. Biden'
}
print(len(presidentsThisCentury))

#Output: 5
```

Numbers, strings, and variable names can be used as keys or values. Dictionaries can even be used as as values within a dictionary, but a dictionary cannot serve as a key within another dictionary.
So this would work:
```python
var1 = 'left'
var2 = 'right'
dict1 = {'key':'value'}

thisDict = {
1: 'two',
'three': 4,
var1: var2,
'nested dictionary': dict1
}
```

But this wouldn't:

```python
var1 = 'left'
var2 = 'right'
dict1 = {'key':'value'}

thisDict = {
1: 'two',
'three': 4,
var1: var2,
dict1: 'invalid'
}
```
