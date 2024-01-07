import sys
sys.stdin = open("/Users/dang/Desktop/2024_Algorithm/Greedy/BOJ1789/BOJ1789.txt")
input = sys.stdin.readline

# 1부터 더해가다가 S보다 같을 때 또는 커졌을 때 1부터 하나씩 빼보면서 맞추면 됨
# 즉 커졌을 때 더해진 수의 갯수 - 1 이 최대 갯수

S = int(input())
rlt = 0
N = 1

while True:
    rlt += N
    if rlt == S:
        print(N)
        break
    elif rlt > S:
        print(N - 1)
        break
    else:
        N += 1