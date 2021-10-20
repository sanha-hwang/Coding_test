import time
N = int(input())
start_time = time.time()
h = 0
count = 0
while h <= N:
    if '3' in str(h):
        count += 3600
    else:
        # m에 3이 들어가는 숫자 15개 (03, 13, 23, 30~39, 43,53)-> s 60개,
        # m에 3이 안들어가는 숫자 45개 -> s에 3이 들어가는 것만 카운트
        count += (15 * 60 + 45 * 15)
    h += 1 
end_time = time.time()
print(count)
print(end_time-start_time)
