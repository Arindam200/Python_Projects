from math import log,ceil
def makeSegment(index, l, r, arr, tree):
    if(l==r):
        tree[index] = arr[l]
    else:
        mid = (l+r)//2
        makeSegment(2*index+1, l, mid, arr, tree)
        makeSegment(2*index+2,mid+1, r, arr, tree)
        tree[index] = min(tree[2*index+1], tree[2*index+2])

def createSegmentTree(arr):
    n = len(arr)
    treeSize = 2**(ceil(log(n,2)))*2 - 1
    tree = [None]*treeSize
    makeSegment(0, 0, n-1, arr, tree)
    return tree

arr = list(map(int, input().split()))
tree = createSegmentTree(arr)
print(tree)