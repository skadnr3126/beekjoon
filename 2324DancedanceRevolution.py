ddr_sequence = list(map(int, input().split()))

max = 400001
n = len(ddr_sequence)-1 #0 제외
dp  = [[400001]*n for _ in range(5)]

dp[0][0] = 2

def cal_power(frm ,to  ) -> int : 
    if frm == 0 :
        return 2
    if frm == to :
        return 1
    if abs(frm - to) == 1 or abs(frm - to) == 3 :
        return 3
    if abs(frm - to) == 2 :
        return 4


for i in range(n-1) :
    for j in range(5):
        if dp[j][i] != max :

            
            current_x = ddr_sequence[i]
            current_y = j
            next_x = ddr_sequence[i+1]


            #current_x 가 이동했을때
            val = cal_power(current_x , next_x)
            next_y = current_y

            dp[next_y][i+1] = min(dp[next_y][i+1] , dp[j][i] + val)

            #current_y 가 이동했을때
            val = cal_power(current_y , next_x)
            next_y = current_x

            dp[next_y][i+1] = min(dp[next_y][i+1] , dp[j][i] + val)


print(min(dp[i][n-1] for i in range(5)))




