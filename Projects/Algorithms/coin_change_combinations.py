def combinationsFor(N, using):
    table = [[0 for i in range(N)] for i in range(N)]
    res  = [0] *(N+1)
    res[0]=1
    for i in range(1,N+1):
        for j in using:
            if(j<=i):
                res[i]+=res[i-j]
    return res[N]

print("This program prints the total number of combinations to obtain change for a given denomination")
print("Enter the changes to use (space separated) - ", end = '')
changes = list(map(int, input().split()))
print("Enter the value you want to find change combinations for - ", end = '')
val = int(input())
print(f'No. of change combinations for {val} using changes {changes} is {combinationsFor(val, changes)}')