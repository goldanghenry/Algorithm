# 바닥 공사_1초,128MB, 20분
# 가로의 길이가 N, 세로의 길이가 2인 직사각형 형태의 얇은 바닥이 있다. 테일이는 이 얇은 바닥을
# 1x2의 덮개, 2x1의 덮개, 2x2의 덮개를 이용해 채우고자 한다.
# 이 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 작성하시오.

# 입력
n = int(input())

# DP 테이블 초기화
d = [0] * 1001

# 다이나믹 프로그래밍
d[1] = 1
d[2] = 3

for i in range(3,n+1):
    d[i] = (d[i-1]+d[i-2]*2) % 796796

# 출력
print(n)
