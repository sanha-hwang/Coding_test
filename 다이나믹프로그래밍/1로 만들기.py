
N = int(input())

d = [0] * 30001 # 버퍼 초기화  index가 주어진 숫자, value는 index 1로 가는 방법 수 즉, counting

# bottom up 방식 => 넘 어렵...
for i in range(2, N+1) :
    d[i] = d[i-1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+ 1)
    
    if i % 3 == 0:
        d[i] = min(d[i], d[i //3] + 1)
    
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5]+ 1)

print(d[N])