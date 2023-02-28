

#STEP 1
collegeAddress = {
'Building Name': 'Ammons Hall', 
'Street': '711 Oval Dr',
'City': 'Fort Collins',
'State': 'Colorado',
'Zip Code': 80523,
'State': 'Minnesota', #Added a second State key
float(5): 'Float Test' #Testing adding a float
}

collegeAddress['Building Name'] = 'Academic Village'

print(collegeAddress)
# Answer to Question 1 below
# Keys: Building Name, Street, City, State, and Zip Code
# Answer to Question 2 below
# See above (It will overide the original State Key)
# Answer to Question 3 below
# Yes, see above
# Answer to Question 4 below
# See above
# Answer to Question 5 below
# Length of the dictionary is 6


#STEP 2
building2Address = {
'Building Name': 'Newsome', 
'Street': '1313 Square St',
'City': 'Denver',
'State': 'Colorado',
'Zip Code': 80446
}
building3Address = {
'Building Name': 'Skylight', 
'Street': '1220 Penn Circle',
'City': 'Birmingham',
'State': 'Alabama',
'Zip Code': 44762
}

dictionaryOfAddresses = {
'College Address': collegeAddress,
'Building 2 Address': building2Address,
'Building 3 Address': building3Address}


# for you to test your dictionary of dictionaries
print(dictionaryOfAddresses)

# should output Fort Collins, feel free to change for testing purposes
print(dictionaryOfAddresses['College Address']['City'])


