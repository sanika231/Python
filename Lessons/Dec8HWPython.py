##L=["Sanika Thatte","Alviya Sayyed","Aashvi Gupta","Tanishi Srivastava","Diya Prakash"]
##for i in range(0,len(L),1):
##    print(L[i])

##N=[]
##W=[]
##index=0
##while True:
##    name=input("enter name: ")
##    if name=="stop":
##        N.pop()
##        W.pop()
##        break
##    weight=int(input("enter current weight(in pounds)"))
##    if weight=="stop":
##        N.pop()
##        W.pop()
##        break
##    N.append(name)
##    W.append(weight)
##    W[index]=W[index]+10
##    print(N)
##    print(W)
##    index=index+1
    
animals=["dog","cat","rat","bat","crab","peacock"]
animals.append("parrot")
animals.append("crow")
for i in range(len(animals)-1,0,-1):
        if "c" == animals[i][0]:
            k=animals.pop(i)

print(animals)



