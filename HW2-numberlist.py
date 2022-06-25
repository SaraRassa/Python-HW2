sum= 0

while True:
    n=input("enter a number or enter E to exit: ")
    if n=="E":
        break
    sum= sum + int(n)
print(sum)