n = int(input () ) 
k = int(input () )
l = int(input () ) 
m = int(input () )
a = [0] * n 
b = [0] * l 
for i in range (n):
    a [i] = i+1
for i in range (l):
    b [i] = i+1
print (a[0:n:k-1],b[0:l:m-1])

#далее пыталась добавить варианты для случаев,
#когда последний эл-т не равен 1
for i in range (n//2):
    t=a[i]
    a[i]=a[n-i-1]
    a[n-i-1]=t
print(a)
for i in range ( (n-k) // 2):
    t=a[i]
    a[i]=a[(n-k)-i-1]
    a[ (n-k)-i-1 ] =t
print(a) 
for i in range ( (n-k),(n-k+n-1)//2+1 ):
    t=a[i]
    a[i]=a[(n-k)-i-1]
    a[ (n-k)-i-1 ] =t
print(a) 