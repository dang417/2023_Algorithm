# S = A[0] * B[0] + ... + A[N-1] * B[N-1]
# S의 값을 가장 작게 만들기 위해 A의 수를 재배열 하기
# S의 최솟값을 출력하는 프로그램
# B의 값이 클수록 A의 값중 작은 것을 선택하도록 한다
import sys
sys.stdin = open("/Users/dang/Desktop/2024_Algorithm/Greedy/BOJ1026/BOJ1026.txt")

# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# rlt = 0
# A.sort(reverse=True)
# B.sort()

# for i in range(N):
#     rlt += A[i] * B[i]

# print(rlt)

# B 배열은 재배열 하면 안된다고 했으므로
N = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
rlt = 0

# 정렬된 A의 값을 작은 순으로 추출하고, B 배열중 값이 큰 순으로 추출하여 곱해서 더한다

for x in A:
    y = B.pop(B.index(max(B)))
    rlt += x * y

print(rlt)