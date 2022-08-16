x=[500,100,50,20,10,5,2,1]
t=int(input("enter total amount:"))
i=0
print("the total number of notes:\n")
while t>0:
    if t>=x[i]:
        c=int(t/x[i])
        print(x[i],":",c)
    t=t%x[i]
    i+=1



