n=int(input())
a=[]
for i in range(n):
    h=int(input())
    a.append(h)
for i in range(n-1):
    for j in range(0,n-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print("Sorted array is:")
for i in range(len(a)):
    print("% d" % a[i], end=" ")