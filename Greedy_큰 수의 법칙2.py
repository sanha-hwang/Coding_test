"""    
효율적 아이디어 
while문을 통해 m이 1씩 감소하는데, M이 몹시 클 때는 시간 초과판정을 받을 수 있다.
"""
import time

N, M, K = map(int, input().split()) # 배열의 크기 N, 숫자가 더해지는 횟수 M,연속해서 더할 수 있는 횟수 K
array = list(map(int, input().split()))

start_time = time.time()

first_number = sorted(array, reverse = True)[0]
second_number = sorted(array, reverse = True)[1]

X = [first_number] * K +[second_number] # K+1 개 

result = (M // (K + 1)) * sum(X) + (M % (K + 1)) * first_number
end_time = time.time()
print(result)
print("time:",end_time-start_time)
