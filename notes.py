a = int(input("input amount\n"))
n_500 = 0
n_100 = 0
n_50 = 0
n_20 = 0
n_10 = 0
n_5 = 0
n_2 = 0
n_1 = 0
if a >= 500:
    n_500 = int(a/500)
    a = a-(n_500*500)
if a >= 100:
    n_100 = int(a/100)
    a = a-(n_100*100)
if a >= 50:
    n_50 = int(a/50)
    a = a-(n_50*50)
if a >= 20:
    n_20 = int(a/20)
    a = a-(n_20*20)
if a >= 10:
    n_10 = int(a/10)
    a = a-(n_10*10)
if a >= 5:
    n_5 = int(a/5)
    a = a-(n_5*5)
if a >= 2:
    n_2 = int(a/2)
    a = a-(n_2*2)
if a >= 1:
    n_1 = int(a/1)
   
else:
    print("input not valid")
print("Total number of notes:\n 500:"+str(n_500) + "\n 100:" + str(n_100) + "\n 50:" + str(n_50) +
      "\n 20:" + str(n_20) + "\n 10:" + str(n_10) + "\n 5:" + str(n_5) + "\n 2:" + str(n_2) + "\n 1:" + str(n_1))
