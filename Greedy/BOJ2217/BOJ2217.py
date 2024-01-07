import sys
sys.stdin = open("/Users/dang/Desktop/2024_Algorithm/Greedy/BOJ2217/BOJ2217.txt")

# k 개의 로프를 연결하면 각 로프에 모두 고르게 w/k 만큼의 중량이 걸림
# 로프들을 이용해 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램?
# 로프가 버틸 수 있는 최소 중량
# 전체 로프를 활용해 들어올릴 수 있는 무게
# 일단 전부다 더한 다음에 최소값 * N 보다 빼고 더 큰지 비교하면서 빼나가기

input = sys.stdin.readline

N = int(input())
rope = []
totalWeight = 0

for i in range(N):
    rope.append(int(input()))

rope.sort(reverse=True)

for i in range(N):
    if rope[i] * (i + 1) >= totalWeight:
        totalWeight = rope[i] * (i + 1)
    
print(totalWeight)