

# 넘나 어렵...
N = int(input())
store = list(map(int, input().split()))
check = [0]*100

check[0] = store[0]
check[1] = max(store[0],store[1])

for i in range(2, N):
    check[i] = max(check[i-1], check[i-2]+store[i])

print(check[N-1])
