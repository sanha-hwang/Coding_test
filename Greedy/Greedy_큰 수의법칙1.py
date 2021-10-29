##최초 아이디어
import time

N, M, K = map(int, input().split()) # 배열의 크기 N, 숫자가 더해지는 횟수 M,연속해서 더할 수 있는 횟수 K
array = list(map(int, input().split()))

start_time = time.time()

first_number = sorted(array, reverse = True)[0]
second_number = sorted(array, reverse = True)[1]
sum = 0
count = 0 # 연속해서 더하는 횟수 카운트

while M > 0:
    if count < K: # K번만큼 제일 큰 수 더하기 
        sum += first_number
        count += 1
    else: #연속끊어주기
        sum += second_number
        count = 0 # count reset
    M -= 1
end_time = time.time()
print(sum)
print("time:",end_time-start_time)


