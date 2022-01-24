# 시각(완전탐색문제)
# 정수 N이 입려고디면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.
# 예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각이다.

# 입력(0<=N<=23)
N = int(input())

count = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 있다면 count+1
            if '3' in str(i)+str(j)+str(k): count += 1
print(count)
