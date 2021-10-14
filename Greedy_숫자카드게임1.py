N, M = map(int, input().split())

min_value_list =[]
for i in range(N):
    array = list(map(int, input().split()))
    min_value_list.append(min(array))
print(max(min_value_list))

"""

list를 사용하지 않고 result만 업데이트하는 방법- 효율적 공간활용일듯?

result = 0
for i in range(N):
    array = list(map(int, input().split()))
    min-value = min(array)
    result = max(result, min_value)
print(result)
"""