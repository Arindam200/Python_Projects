#find the smallest and the biggest number
print("After finished enter values please enter stop")

list1=[]
while(True):
        
        num=input("enter value: ")
        list1.append(num)
        if num=="stop":
            break

list1.remove("stop")


n_list=[]
for n in range(0,len(list1)):
               list1[n]==int(list1[n])
               n_list.append(int(list1[n]))
print(n_list)


print("Smallest number: ",min(n_list))
print("Biggest number: ",max(n_list))
