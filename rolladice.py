import random

response="y"
while response=="y":
    no=random.randint(1,6)
    if no==1:
        print("______")
        print("|     |")
        print("|  0  |")
        print("|     |")
        print("|_____|")
    elif no==2:
        print("______")
        print("|0    |")
        print("|     |")
        print("|    0|")
        print("|_____|")
    elif no ==3:
        print("______")
        print("|0    |")
        print("|  0  |")
        print("|    0|")
        print("|_____|")
    elif no==4:
        print("______")
        print("|0   0|")
        print("|     |")
        print("|0   0|")
        print("|_____|")
    elif no==5:
        print("______")
        print("|0   0|")
        print("|  0  |")
        print("|0   0|")
        print("|_____|")
    else:
        print("______")
        print("|0   0|")
        print("|0   0|")
        print("|0   0|")
        print("|_____|")
    response=input("press y to continue or no to stop")