N = int(input())
data_array = input().split()

x = 1
y = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

for data in data_array:
    
    for i in range(len(move_types)):
        if data == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x, y =nx, ny # update 
print(x,y)