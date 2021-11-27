def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None


N = int(input())
product = list(map(int,input().split()))

M = int(input())
need = list(map(int, input().split()))

''' sanha

for i in range(M):
    if need[i] in product:
        print('yes', end=' ')
    else:
        print('no', end=' ')
'''

for i in need:
    result = binary_search(product, i, 0, N-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')