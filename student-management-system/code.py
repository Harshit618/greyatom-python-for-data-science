# --------------
# Code starts here
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']

# Create the lists 
new_class=class_1+class_2
# Concatenate both the strings

print(new_class)
# Append the list
new_class.append('Peter Warden')
# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print(new_class)


# Create the Dictionary
courses={"Math":65,"English":70,"History":80,"French":70,"Science":60}

print(courses)
# Slice the dict and stores  the all subjects marks in variable
total=courses.values()
print(total)
# Store the all the subject in one variable `Total`
total=sum(total)
# Print the total
print(total)
# Insert percentage formula
x=len (courses)
print(x)
percentage=total/(x*100)*100
# Print the percentage
print(percentage)





# Create the Dictionary
mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,"Peter Warden":75}
topper= max(mathematics,key =mathematics.get)
print (topper)

# Given string


# Create variable first_name 
split=topper.split()
# Create variable Last_name and store last two element in the list
first_name=split[0]
last_name=split[1]
# Concatenate the string
full_name=last_name+" "+first_name
# print the full_name
print(full_name)
# print the name in upper case
certificate_name=full_name.upper()
print(certificate_name)
# Code ends here


