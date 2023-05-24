# cook your dish here
for i in range(int(input())):
    c,d=map(int,input().split(' '))
    for i in range(1,11):
        if(10*(i-1)< c <= 10*i):
            k=i
        if(10*(i-1)< d <= 10*i):
            j=i
    print(max(k,j)-min(k,j))
