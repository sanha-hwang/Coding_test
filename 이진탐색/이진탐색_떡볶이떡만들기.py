
N, M = map(int, input().split())
dduck_length = list(map(int, input().split()))

#초기 절단길이 mid 구하기
start = min(dduck_length)
end = max(dduck_length)
mid = (start + end ) // 2 

while True:
    sum_thing = 0 # 제공하는 길이
    for i in range(N):
        if dduck_length[i]- mid > 0 :
            sum_thing += (dduck_length[i]- mid)
        else:
            continue
        
    if sum_thing > M:
        start = mid
        mid = (start + end ) // 2
    elif sum_thing == M :
        print(mid)
        break
    else:
        end = mid
        mid = (start + end ) // 2

