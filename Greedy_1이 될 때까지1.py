import time


N, K = map(int, input().split())
start_time = time.time()

count = 0
while N != 1:
    if N % K == 0:
        N /= K
       
    else:
        N -= 1
    count += 1
end_time = time.time()
        
print(count)
print("time:",end_time-start_time)
