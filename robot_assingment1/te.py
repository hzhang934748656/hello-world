#wall = [[400, 0], [400, 100], [400, 200], [400, 300], [400, 800], [400, 700], [400, 600], [400, 500], [600, 400], [700, 400], [800, 400], [0, 300], [100, 300], [200, 300], [200, 400], [200, 500], [200, 600], [100, 600]]
'''
x_list = []
y_list = []
for a in wall:
	x_list.append(a[0])
	y_list.append(a[1])
print(x_list)
print(y_list)'''
wall = [(400, 0), (400, 100), (400, 200), (400, 300), (400, 800), (400, 700), (400, 600), (400, 500), (600, 400), (700, 400), (800, 400), (0, 300), (100, 300), (200, 300), (200, 400), (200, 500), (200, 600), (100, 600)]
for x,y in wall:
	if (x,y) == (700,400):
		break
	print("duck")