import random

S=input("Enter S to start the game ")
while True:
        d=random.randint(1,6)
        print(d)
        if d==6:
            print("Great!you can roll again")
            S=input("Enter S to roll ")
                
        else:
            break