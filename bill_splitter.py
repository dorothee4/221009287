#nyiransabimana dorothee
#221009287
#Computer Science
import random

d = input("Enter the number of friends joining (including you):\n")
num = int(d)
friends = {}

if num > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(num):
        name = input()
        friends.update({name: 0})
    
print("Enter the total bill value:")
x = input()
bill = int(x)
split = int(bill) / num
for key, value in friends.items():
    friends[key] = round(split, 2)

print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
choice = input()
if choice == "yes":
    lucky_friend = random.choice(list(friends))
    print(lucky_friend, " is the lucky one!")

    for_remaining = bill / (num - 1)

    for key, value in friends.items():
        if key == lucky_friend:
            friends[lucky_friend] = 0
        else:
            friends[key] = round(for_remaining, 2)
else:
    print("No one is going to be lucky")

print(friends)
