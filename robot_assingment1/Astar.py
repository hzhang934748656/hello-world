class Array2D:
	def __init__(self,w,h):
		self.w = w
		self.h = h
		self.data = []
		self.data = [[0 for y in range(h)] for x in range(w)]


	def showArray2D(self):
		for y in range(self.h):
			for x in range(self.w):
				print(self.data[x][y], end= "")
				print("")
	def __getitem__(self, item):
		return self.data[item]

class Point:
	#show a point
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __eq__(self, other):
		if self.x == other.x and self.y == other.y:
			return True
		return False
	def __str__(self):
		return "x"+str(self.x)+",y:"+str(self.y)



class A_star:

	class Node:
		def __init__(self, point, endpoint,g = 0):
			self.point = point
			self.father = None
			self.g = g
			self.h = (abs(endpoint.x - point.x) + abs(endpoint.y - point.y)

	def __init__(self, map2d,startpoint, endpoint, passTag = 0):

        # open list
        self.openlist = []
        # close list
        self.closelist = []
        # find map
        self.map2d = map2d
        # start point
        self.startpoint = startpoint
        self.endpoint = endpoint
        self.passTag = passTag

    
    def getMinNode(self):
    	# get the lowest F in openlist
 		# return : Node
 		currentNode = self.openlist[0]
 		for node in self.openlist:
 			if node.g + node.h < currentNode.g + currentNode.h:
 				currentNode = node
 			return currentNode

 	def pointInCloselist(self,point):
 		for node in self.closelist:
 			if node.point == point:
 				return True
 		return False
 	def pointInOpenList(self,point):
 		for node in self.openlist:
 			if node.point == point:
 				return node
 		return Node
 	def endPointInCloseList(self):
 		for node in self.openlist:
 			if node.point == self.endpoint:
 				return node
 			return None
 	def searchNear(self, minF, offsetX, offsetY):
 		 """
        搜索节点周围的点
        :param minF:F值最小的节点
        :param offsetX:坐标偏移量
        :param offsetY:
        :return:
        """
        #越界检测
        if minF.point.x + offsetX < 0 or min.point.x + offsetX > self.map2d.w - 1 or minF.point.y + offsetY < 0 or min.point.y + offsetY > self.map2d.h - 1: 
        	return
        # 如果是障碍，就忽略
        if self.map2d[minF.point.x + offsetX][minF.point.y + offsetY] != self.passTag:
        	return
        #如果在关闭表中，就忽略
        currentPoint = Point(minF.point.x + offsetX, minF.point.y + offsetY)
        if self.pointInCloselist(currentPoint):
        	return

       	# 设置单位花费
        if offsetX == 0 or offsetY == 0:
        	step = 10
       	else:
       		step = 14
       	 # 如果不再openList中，就把它加入openlist
		currentNode = self.pointInOpenList(currentPoint)
		if not currentNode:
			currentNode = A_star.Node(currentPoint, self.endpoint, g=minF.g + step)
			currentNode.father = minF
			self.openlist.append(currentNode)
			return
		# 如果在openList中，判断minF到当前点的G是否更小
		if minF.g + step < currentNode.g:
			currentNode.g = minF + step
			currentNode.father = minF
	def start(self):
		#1.将起点放入开启列表
		startpoint = A_star.Node(self.startpoint, self.endpoint)
		self.openlist.append(startNode)

		# main loop
		while True:
			#找到F值最小的点
			minF = self.getMinNode()
			# 把这个点加入closeList中，并且在openList中删除它
			self.closelist.append(minF)
			self.openlist.remove(minF)
			# 判断这个节点的上下左右节点
			self.searchNear(minF,0, -1)
			self.searchNear(minF,0, 1)
			self.searchNear(minF,-1, 0)
			self.searchNear(minF,1, 0)
			# 判断是否终止
			point = self.endPointInCloseList()
			if point:
				# 如果终点在关闭表中，就返回结果
                # print("关闭表中")
                cPoint = point
                pathList = []
                while  True:
                	if cPoint.father:
                		pathList.append(cPoint.point)
                		cPoint = cPoint.father
                	else:
                		return list(reversed(pathList))
                if len(self.openlist) == 0:
                	return None






if __name__ == '__main__':
    #创建一个10*10的地图
    map2d=Array2D(10,10)
    #设置障碍
    map2d[4][0]= 1
    map2d[4][1] = 1
    map2d[4][2] = 1
    map2d[4][3] = 1
    map2d[4][4] = 1
    map2d[4][5] = 1
    map2d[4][6] = 1
    #显示地图当前样子
    map2d.showArray2D()
    #创建AStar对象,并设置起点为0,0终点为9,0
    aStar=AStar(map2d,Point(0,0),Point(9,0))
    #开始寻路
    pathList=aStar.start()
    #遍历路径点,在map2d上以'8'显示
    for point in pathList:
        map2d[point.x][point.y]=8
        # print(point)
    print("----------------------")
    #再次显示地图
    map2d.showArray2D()
