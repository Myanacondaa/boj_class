import sys
sys.setrecursionlimit(10**6)
n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

white = 0
blue = 0


def cut_paper(arr: list[list[int]]):
    global white, blue
    if len(arr) == 1:     # 자른 종이가 1*1이면
        if arr[0][0] == 1:   # 1이면 파란색
            blue += 1
        else:               # 0이면 하얀색
            white += 1
        return

    tmp = 0
    for p in arr:
        tmp += sum(p)   # 배열의 합

    if tmp == 0:        # 0이면 하얀색
        white += 1
        return

    elif tmp == len(arr)**2:     # 종이의 넓이와 같으면 모두 1임
        blue += 1
        return

    for i in range(4):
        section = []
        if i == 0:
            for j in range(len(arr)//2):    # 1/4 구역 슬라이싱 후 section 리스트에 추가
                section.append(arr[j][:len(arr)//2])
            cut_paper(section)              # 1/4 구역 재귀 호출

        if i == 1:
            for j in range(len(arr) // 2):  # 2/4 구역 슬라이싱 후 section 리스트에 추가
                section.append(arr[j][len(arr) // 2:])
            cut_paper(section)  # 1/4 구역 재귀 호출

        if i == 2:
            for j in range(len(arr) // 2):  # 3/4 구역 슬라이싱 후 section 리스트에 추가
                section.append(arr[(len(arr)//2)+j][:len(arr) // 2])
            cut_paper(section)  # 1/4 구역 재귀 호출

        if i == 3:
            for j in range(len(arr) // 2):  # 4/4 구역 슬라이싱 후 section 리스트에 추가
                section.append(arr[(len(arr)//2)+j][len(arr) // 2:])
            cut_paper(section)  # 1/4 구역 재귀 호출


cut_paper(paper)
print(white)
print(blue)





