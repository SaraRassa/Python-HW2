import math

for i in range(100):

    N=int(input("Enter second(s): "))
    H=math.floor(N/3600)
    M=math.floor((N-H*3600)/60)
    S= N- H*3600 - M*60

    print("Time= ", H,":", M,":",S)

