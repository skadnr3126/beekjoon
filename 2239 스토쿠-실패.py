from collections import deque
sudoku = []
one_number_sell_queue = deque()
tracking_sell = []

def find_possible_nums(y,x) :
    if sudoku[y][x] != 0 :
        return 0
    possible_nums = [i for i in range(10)]
    for i in range(9) :
        if sudoku[y][i] in possible_nums :
            possible_nums.remove(sudoku[y][i])
        if sudoku[i][x] in possible_nums :
            possible_nums.remove(sudoku[i][x])
    start_x = (x//3)*3
    start_y = (y//3)*3
    for i in range(3) :
        for j in range(3) :
            if sudoku[start_y+i][start_x+j] in possible_nums :
                possible_nums.remove(sudoku[start_y+i][start_x+j])
    
    #print(possible_nums)
    if len(possible_nums) == 1 :
        sudoku[y][x] = possible_nums[0]
        one_number_sell_queue.append((y,x))
    else :
        sudoku[y][x] = possible_nums

    #print(sudoku[y][x])

def delete_possible_num(y,x,num) :
    for i in range(9):
        if type(sudoku[y][i]) == list and num in sudoku[y][i] :
            sudoku[y][i].remove(num)
            if len(sudoku[y][i]) == 1 :
                sudoku[y][i] = sudoku[y][i][0]
                one_number_sell_queue.append((y,i))
        if type(sudoku[i][x]) == list and num in sudoku[i][x] :
            sudoku[i][x].remove(num)
            if len(sudoku[i][x]) == 1 :
                sudoku[i][x] = sudoku[i][x][0]
                one_number_sell_queue.append((i,x))
    start_x = (x//3)*3
    start_y = (y//3)*3
    for i in range(3) :
        for j in range(3) :
            if type(sudoku[start_y+i][start_x+j]) == list and num in sudoku[start_y+i][start_x+j] :
                sudoku[start_y+i][start_x+j].remove(num)
                if len(sudoku[start_y+i][start_x+j]) == 1 :
                    sudoku[start_y+i][start_x+j] = sudoku[start_y+i][start_x+j][0]
                    one_number_sell_queue.append((start_y+i,start_x+j))

def possible(y,x,num) :
    for idx in range(9) :
        if type(sudoku[y][idx]) == int :
            if sudoku[y][idx] == num :
                return False
        if type(sudoku[idx][x]) == int :
            if sudoku[idx][x] == num :
                return False
    start_x = (x//3)*3
    start_y = (y//3)*3
    for i in range(3) :
        for j in range(3) :
            if type(sudoku[start_y+i][start_x+j]) == int :
                if sudoku[start_y+i][start_x+j] == num :
                    return False
    return True
    

def dfs(idx) :
    if idx == len(tracking_sell):
        for i in range(9) :
            for j in range(9) :
                print(sudoku[i][j], end = '')
            print()
        exit(0)
    
    x,y = tracking_sell[idx]
    possible_nums = sudoku[y][x]
    for num in possible_nums :
        if possible(y,x,num) :
            sudoku[y][x] = num
            dfs(idx+1)
            sudoku[y][x] = possible_nums#원상복구
        


#입력받기
for _ in range(9):
    input_list = list(input())
    input_list = list(map(int ,input_list))
    sudoku.append(input_list)

#가능한 숫자 받기
for y in range(9) :
    for x in range(9):
        find_possible_nums(y,x)

#하나인 숫자 처리하기
while one_number_sell_queue :
    y,x = one_number_sell_queue.popleft()
    num = sudoku[y][x]
    delete_possible_num(y,x,num)

#2개이상인 것들 추가하기

for i in range(9) :
    for j in range(9) :
        if type(sudoku[i][j]) == list :
            tracking_sell.append((j,i))

dfs(0)


#print sudoku


