n = int(input())
m = int(input())
s = input()
# 문자열 브루스 포스 하면 시간 오버
# s에 IOI가 몇 번 있는지 확인

cnt, ans, idx = 0, 0, 0

while idx+3 < m:
    if s[idx:idx+3] == "IOI":
        cnt += 1
        idx += 2      # 인덱스 두 번 이동해서 끝의 I부터 다시 시작
        if cnt == n:  # IOI가 반복되는 횟수가 n과 같으면 s 한 개를 찾은 것과 같으므로
            ans += 1  # s의 개수 추가
            cnt -= 1

    else:
        idx += 1    # 한 번만 이동
        cnt = 0

print(ans)