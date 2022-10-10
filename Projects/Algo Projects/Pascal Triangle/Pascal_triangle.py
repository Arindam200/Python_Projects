from math import factorial
from itertools import islice


# input n
def solve(n):
    list1=[]
    list2=[]
    for i in  range(1,n+1):
        list2.append(i)

    for i in range(n):
        for j in range(i + 1):
            # nCr = n!/((n-r)!*r!)
            k=factorial(i) // (factorial(j) * factorial(i - j))
            list1.append(k)


    Inputt = iter(list1)
    Output = [list(islice(Inputt, elem))for elem in list2]
    print(Output)
if __name__ == '__main__':
    n=int(input("Enter n:"))
    solve(n)
