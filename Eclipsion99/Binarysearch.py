arr = list(map(int, input("Enter elements:").split()))
elem = int(input("Enter element to search:"))

def binary_search(L, x):
    
    l = 0
    r = len(L) - 1
    m = 0
    while l <= r:
	    m = (r + l) // 2
	    if L[m] < x:
		    l = m + 1
	    elif L[m] > x:
	        r = m - 1
	    else:
	        return m
    return -1
	
res = binary_search(arr, elem)
if res == -1:
    print("Element not found")
else:
    print("Element found at index:",res)
