lst = []
p = []
# number of elements as input
n = int(input("Enter number of elements : "))
print("input:\n")
# iterating till the range
for i in range(0, n):
    ele = int(input())

    lst.append(ele)  # adding the element
f=1
print(lst)
for i in range(0,n):
    for j in range(i+1,n):
        if lst[i]<lst[j]:
            f=0
    if(f==1):
        p.append(lst[i])
p.append(lst[n-1])
print(p)
        
    


        
        