array_1 = []
# number of elements as input
m = int(input("Enter number of elements : "))
print("input:\n")
# iterating till the range
for i in range(0, m):
    ele = int(input())
    array_1.append(ele)  # adding the element


array_2=[]
# number of elements as input
n = int(input("Enter number of elements : "))
print("input:\n")
# iterating till the range
for i in range(0, n):
    ele = int(input())
    array_2.append(ele)  # adding the element

array_3=[]
# number of elements as input
o = int(input("Enter number of elements : "))
print("input:\n")
# iterating till the range
for i in range(0, o):
    ele = int(input())
    array_3.append(ele)  # adding the element
p = []
f=0
for i in range(0,m):
    for j in range(0,n):
        if array_1[i]==array_2[j]:           
            for k in range(0,o):
                if array_2[j]==array_3[k]:
                    p.append(array_3[k])
print(p)
