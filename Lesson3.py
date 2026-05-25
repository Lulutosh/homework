user1 = {
    "name": input("Enter your name: "),
    "age": input("Enter your age: "),
    "height": int(input("Enter your height (cm): "))
}

user2 = {
    "name": input("Enter your name: "),
    "age": input("Enter your age: "),
    "height": int(input("Enter your height (cm): "))
}

user_list = [user1, user2]
for user in user_list:
    print(user)

def calculate_height(users):
    total = 0
    for user in users:
        total += user["height"]
    return total
print(f"users height combined is")


total_height = calculate_height(user_list)
print(f"Total combined height of both users is {total_height} cm")