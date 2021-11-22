#위에서 아래로
n = int(input())
input_list = list()

for i in range(n):
  input_list.append(int(input()))

input_list.sort(reverse=True) ## 또는 원본을 남기고 정렬을 하고 싶으면 array = sorted(input_list, reverse=True)

for i in range(len(input_list)):
  print(input_list[i], end=" ")