# 성적이 낮은 순서로 학생 출력하기, dict 활용 => tuple을 활용해도 괜찮음

n= int(input())
score_list = dict()
for i in range(n):
  name, score = input().split()
  score_list[int(score)] = name

for score_key in sorted(score_list.keys()):
  print(score_list[score_key], end=' ')