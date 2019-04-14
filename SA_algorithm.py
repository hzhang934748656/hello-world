def initialize_chess(N):
  Board =np.zeros(N*N).reshape(N,N)
  
  for i in range(0,N):
    rand_number = random.randint(0,N-1)
    Board[i][rand_number] = 1
  return Board
def get_place(Board):### get the chess place###
	Col_index = []
	#get the index of col which is 1
	for i in range(0,N):
		for j in range(0,N):
	 		 if Board[i][j] == 1:
	   			 Col_index.append(j)
	return Col_index
def move(Board,N,Col_index):
  while(1):
    rn1 = random.randint(0,N-1)
    rn2 = random.randint(0,N-1)
    if rn2 != rn1:
      break
  Board[rn1][Col_index[rn1]] = 0
  Board[rn1][rn2] = 1
  Col_index[rn1]=rn2
  return(Board,Col_index)
def Calculate_score(Board,N,Col_index):
  cost = 0
  i_index = 1
  for j in range(0,N):
  #check each col
    for i in range(i_index,N):
      if Board[i][Col_index[j]] == 1:
        cost = cost + 1
    i_index = i_index + 1
  
 #check each left_dig
  for u in range(0,N):

    if Col_index[u] == 0:
      continue
    for k in range(1,N):
      if Col_index[u]-k < 0:
        continue
      if u+k > N-1:
        break
      if Board[u+k][Col_index[u]-k] == 1:
        cost = cost + 1
  #check each right_dig
  for u in range(0,N):

    if Col_index[u] == N-1:
      continue
    for k in range(1,N):
      if Col_index[u]+k > N-1:
        continue
      if u+k > N-1:
        break
      if Board[u+k][Col_index[u]+k] == 1:
        cost = cost + 1

  return cost
def SA_algorithm(Board_old,Col_index_old,T,N):
  cost_old = Calculate_score(Board_old,N,Col_index_old)
  Board_new,Col_index_new=move(Board_old,N,Col_index_old)
  cost_new = Calculate_score(Board_new,N,Col_index_new)
  if cost_new ==0:
    return Board_new,Col_index_new,cost_new
  Delta = cost_new - cost_old
  if (1001-T>3000):
    if (Delta>0):
      if(random.random()>=math.exp(-Delta/(10001-T))):
         #reject bad move
        return Board_old,Col_index_old,cost_old
      else:
        return Board_new,Col_index_new,cost_new
    else:#good move accept
      return Board_new,Col_index_new,cost_new
  else:
    if(Delta>0):
      return Board_old,Col_index_old,cost_old
    else:
      return Board_new,Col_index_new,cost_new
#hyper
print("Please input a number N")

N=input()
print("---------------------------------------")
N = int(N)
##########
import numpy as np
import random
import math
#initialize the board
Board = initialize_chess(N)
print("Initial state:")
print(Board)
Col_index=get_place(Board)
count = 0
for T in range(1,10000):

  count = count + 1
  Board_new,Col_index_new,cost = SA_algorithm(Board,Col_index,T,N)
  if cost == 0:
    break
print("---------------------------------------")
print("Result:")

print(Board_new)
if(count ==9999):
  print("Sorry, I fail to find the good solution")
else:
  print("The total time for try is ",count)
print("---------------------------------------")