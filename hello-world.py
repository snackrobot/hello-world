# This program says hello and asks for a person's name. It also
# provides the name length. Lastly, it asks for the person's age and
# provides them with their new age in 1 year.

print('Hello, world!')
print('What is your name, human?')    # ask for their name
myName = input()
print('It is good to meet you, ' + myName + ' , that''s a lovely \
name.')
print('The length of your name is:')
print(len(myName))
print('What is your age, human?')    # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in 1 year. Happy \
early birthday! I hope you get to eat cake.')