lst = []
p = []
# number of elements as input
n = int(input("Enter number of elements : "))
print("input:\n")
# iterating till the range
for i in range(0, n):
    ele = int(input())

    lst.append(ele)  # adding the element

print(lst)
for i in range(1,n-1):
    if lst[i] > lst[i+1] and lst[i] > lst[i-1]:
        p.append(lst[i])
print(p)
