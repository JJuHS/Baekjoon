import sys
# sys.stdin = open("C:/Users/ghtjd/Desktop/tmp/python/input.txt", "r")

input = sys.stdin.readline
from collections import deque as dq

# 입력받기 : 빌딩주변을 다 '.'(이동가능) 으로 채워놓는다.
def input_data():
    h, w = map(int, input().split())
    buildings = [['.'] * (w + 2) for _ in range(h + 2)]

    for i in range(1, h + 1):
        building = input()
        buildings[i][1:-1] = building

    key_had = list(input())
    if '0' in key_had:key_had = []
    return h, w, buildings, key_had

direction = [
    (-1, 0),  # 상
    (1, 0),   # 하
    (0, -1),  # 좌
    (0, 1)    # 우
]
def sol(h, w, buildings, key_had):
    closed_door = []
    paper_get = 0
    visit = []
    q = dq()
    q.append((0, 0))
    visit.append(0)
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx in range(h + 2) and ny in range(w + 2):
                # 이미 방문한 경우
                if (nx * (w + 2) + ny) in visit:continue
                visit.append(nx * (w + 2) + ny)
                char = buildings[nx][ny]
                # 벽인 경우
                if char == '*':continue
                # 문인데 키 없는 경우
                if char.isupper() and char.lower() not in key_had:
                    closed_door.append((nx, ny, char))
                    continue
                # 문서인 경우
                if char == '$':
                    paper_get += 1
                    buildings[nx][ny] = '.'
                # 열쇠인 경우
                if char.islower():
                    # 이미 있는 키
                    if char in key_had:
                        buildings[nx][ny] = '.'
                    else:
                        key_had.append(char)
                        buildings[nx][ny] = '.'
                        for cx, cy, alphabet in closed_door:
                            if alphabet.lower() == char:
                                buildings[cx][cy] = '.'
                                q.append((cx, cy))
                # 문이고 키 있는 경우
                if char.isupper():
                    if char.lower() in key_had:
                        buildings[nx][ny] = '.'
                q.append((nx, ny))
    print(paper_get)
    return

T = int(input())

for _ in range(T):
    h, w, buildings, key_had = input_data()
    sol(h, w, buildings, key_had)


