for i in range(100):

    H=int(input("Enter hour(s): "))
    M=int(input("Enter minute(s): "))
    S=int(input("Enter second(s): "))
    Total_Time= H*3600 + M*60 + S
    print("Total Time= ", Total_Time," seconds")