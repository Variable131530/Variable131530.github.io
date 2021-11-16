n = int(input('Nhập vào số cột/hàng: '))

x, y = 0, 0
dx, dy = 0, 1

mat = [[None]*n for j in range(n)]
print(mat)

for i in range(n**2):
	mat[x][y] = i
	nx, ny = x+dx, y+dy
	if 0 <= nx < n and 0 <= ny < n and mat[nx][ny] == None:
		x, y = nx, ny
	else:
		dx, dy = dy, -dx
		x, y = x+dx, y+dy

for x in range(n):
	for y in range(n):
		print('%02d' %(mat[x][y]), end = ' ')
	print()




