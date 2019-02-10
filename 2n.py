s= int(input())
a=0
for i in range(1,s):
  for j in range(i,s+1):
    if(i!=j):
      a+=1
print(a)
