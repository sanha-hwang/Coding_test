data = input()
column = data[0] # chr, ord -> ord(a)~ord(h)
row = int(data[1]) # 1~8

dc = [2 , 2, -2, -2, 1, 1, -1, -1]
dr = [1, -1, 1, -1, 2, -2, 2, -2]

count = 0

for i in range(len(dc)):
    c = ord(column) + dc[i]
    r = row + dr[i]
    if (c < ord('a') + 0) or c > (ord('a') + 7) or r < 1 or r > 8:
        continue
    else:
        count += 1
print(count) 


