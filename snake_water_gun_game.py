# This code is written by Ravi Singh Kharayat
import random

n = ["s", "w", "g"]

user = []
computer = []
i = 1

while i <= 10:
    cpu = random.choice(n)
    input1 = input("Enter the choice:\n"
                   "s for snake\n"
                   "w for water\n"
                   "g for gun\n")
    if (input1 == "s") and (cpu == "w"):
        user.append("1")
        computer.append("0")
    elif (input1 == "w") and (cpu == "g"):
        user.append("1")
        computer.append("0")
    elif (input1 == "s") and (cpu == "g"):
        user.append("0")
        computer.append("1")
    elif input1 == cpu:
        user.append("0")
        computer.append("0")
    i += 1

if user.count("1") > computer.count("1"):
    print(user, "/n", computer)
    print("user WINS!!")
elif user.count("1") < computer.count("1"):
    print(user, "/n", computer)
    print("computer WINS!!")

# This code is written by Ravi Singh Kharayat
