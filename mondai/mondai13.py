n=int(input("整数："))

if n % 10 == 0:
    print("１０の倍数")
    
elif n % 5 == 0:
    print("５の倍数")
    
elif n % 2 == 0:
    print("２の倍数")
    
else:
    print("それ以外")