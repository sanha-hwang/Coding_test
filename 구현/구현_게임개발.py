#data 입력받기
N, M = map(int, input().split())
x, y, direction = map(int, input().split())

array =[]
for i in range(N):
    array.append(list(map(int, input().split())))

history = [[0] * M for _ in range(N)] # 방문한 위치 저장
history[x][y] = 1 #초기위치 방문처리

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1] 


def turn_left(): # 회전하는 함수
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    #회전하여 그 앞칸 확인해보기
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    #4방향 확인
    if history[nx][ny] == 0 and array[nx][ny] == 0: #아직 방문하지 않았고, 육지라면 이동후 update
        history[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else: # 가보지 않은 칸이 없거나 바다인 경우
        turn_time += 1
    
    if turn_time == 4: # 4방향 다 확인햇는데 이동이 없다
        nx = x - dx[direction]
        ny = y - dy[direction] # 한칸 뒤로 가볼까
        # 뒤로 갈 수 있다면 
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀 있는 경우
        else:
            break # 게임종료 끝
        
        turn_time = 0 # 뒤로가서 다시 시작

print(count)


