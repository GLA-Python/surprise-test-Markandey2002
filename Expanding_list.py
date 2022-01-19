def num(n):
    lst=[]
    for i in range(len(n)-1):
        lst.append(abs(n[i+1]-n[i]))
    j=sorted(lst)
    print(j)
    if j == lst:
       return True
    else:
       return False


n=list(map(int, input().split()))
out=num(n)
print(out)
