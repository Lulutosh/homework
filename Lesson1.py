name1 = input('hi user 1, please enter your name: ')
age1 = int(input(f'{name1} please enter your age: '))
height1 = float(input(f' {name1} please enter your height: '))
print(f"you are {name1}, your are {age1} years old, your height is {height1}")

name2 = input('please enter your name: ')
age2 = int(input(f'{name2} please enter your age: '))
height2 = float(input(f'{name2} please enter your height: '))
print(f"you are {name2}, your are {age2} years old, your height is {height2}")

height_combined = height1 + height2
print(f' combined height of {name1} and {name2} is {height_combined}')



