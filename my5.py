
import os
import pdb
# help(os)


'''
    @author 战神Z
    @date 2016年9月12日
    @title Gobang
    @modified 
      
'''




checkerboard = []


def ini():
	
	for i in range(10):
		checkerboard.append([])
		for j in range(10):
			checkerboard[i].append(0)
	start()


def start():
	who = False
	os.system('cls')
	printcb()
	while  True:
		t=input('Plese input (x,y),now is'+('乂' if who else '口')+':')
		t =t.split(',')
		if len(t)==2:
			x=int(t[0])
			y=int(t[1])
			if checkerboard[x][y]==0:
				checkerboard[x][y]=1 if who else 2
				os.system('cls')
				printcb()

				# pdb.set_trace()

				win=whowin(x,y)
				if win:
					print(('乂' if who else '口')+'win' )
					break
				who = not who
	os.system('pasuse')


def whowin(px,py):
	t=checkerboard[px][py]

	#|
	count = 0
	x=px
	y=py
	while (x>=0 and t == checkerboard[x][y]):
		count += 1
		x -= 1
	x=px
	while (x<10 and t == checkerboard[x][y]):
		count += 1
		x += 1
	if (count>5):
		return True

	#-
	count = 0
	x=px
	y=py
	while (y>=0 and t == checkerboard[x][y]):
		count += 1
		y -= 1
	y=py
	while (y<10 and t == checkerboard[x][y]):
		count += 1
		y += 1
	if (count>5):
		return True

	#/
	count = 0
	x=px
	y=py
	while (x<10 and y>=0 and t == checkerboard[x][y]):
		count += 1
		x += 1
		y -= 1
	x=px
	y=py
	while (x>=0 and y<10 and t == checkerboard[x][y]):
		count += 1
		x -= 1
		y += 1
	if (count>5):
		return True

	#\
	count = 0
	x=px
	y=py
	while (x>=0 and y>=0 and t == checkerboard[x][y]):
		count += 1
		x -= 1
		y -= 1
	x=px
	y=py
	while (x<10 and y<10 and t == checkerboard[x][y]):
		count += 1
		x += 1
		y += 1
	if (count>5):
		return True

	



def printcb():
	print (' 零一二三四五六七八九')
	for i in range(10):
		print(i,end='')
		for j in range(10):
			if checkerboard[i][j]==0:
				print('十',end='')
			elif checkerboard[i][j]==1:
				print('乂',end='')
			elif checkerboard[i][j]==2:
				print('口',end='')
		print('\n')


ini()
