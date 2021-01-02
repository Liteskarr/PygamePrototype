from PIL import Image
from PyQt5.QtWidgets import QFileDialog
import pprint
colors = {
	'water':((3, 169, 244), '03A9F4', 0),
	'plains':((76,175,80), '4CAF50', 1),
	'hills':((0,150,136), '009688', 2),
	'mountains':((121,85,72),'795548', 3),
	'plains_river':((255,193,7), 'FFC107', 4),
	'hills_river':((255,152,0), 'FF9800', 5),
	'mntns_river':((255,87,34), 'FF5722', 6)
}

def from_png(path = None):
	img = Image.open(path)
	pixils = img.load()
	x, y = img.size
	mp = [[[] for j in range(y)] for i in range(x)]
	for j in range(x):
		for i in range(y):
		 	for k in colors:
		 		if pixils[i, j] == colors[k][0]:
		 			mp[j][i] = colors[k][2]
		 			break 
	return mp

a = from_png('vis.bmp')
print(a)
# for i in a:
# 	print(str(i))