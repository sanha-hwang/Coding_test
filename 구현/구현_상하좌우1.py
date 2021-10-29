N = int(input())
data_array = input().split()

x = 1
y = 1

for data in data_array:
    
    if data == 'R' and (y < 5):
        y += 1
    elif data == 'L' and (y > 1):
        y -= 1
    elif data == 'D' and (x < 5):
        x += 1
    elif data =="U" and (x > 1):
        x -= 1
    else:
        continue
print("{} {}".format(x,y))