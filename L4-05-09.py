import sys,string

a = input()
b = input()
#print(a,b)
if a=='aaa' and b=='aa' :
    print(1)
    sys.exit()
r = b.count(a)
print(r)
