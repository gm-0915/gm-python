#例題1
#1 １つ目の整数：15
x=input("１つ目の整数：")
x=int(x)

#2 ２つ目の整数：4
y=input("２つ目の整数：")
y=int(y)

#3 15+4=19
print("{}+{}={}".format(x,y,x+y))

#4 15-4=11
print("{}-{}={}".format(x,y,x-y))

#5 15×4=60
print("{}*{}={}".format(x,y,x*y))

#6 15÷4=3 余り3
print("{}//{}={}余り{}".format(x,y,x//y,x%y))