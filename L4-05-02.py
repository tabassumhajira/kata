import sys,string


def maxOfSegmentMins(a, b, c):
    if c == 1:
        return min(a)
    if c == 2 :
        return max(a[0], a[b - 1])
    return max(a)

b,c = input().split()
b,c = int(b),int(c)
a = [ int(x) for x in input().split()]
b = len(a)
ans = maxOfSegmentMins(a, b, c)
print(ans)
