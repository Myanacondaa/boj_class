import sys
input = sys.stdin.readline

def is_palindrome(t: str) -> str:
    for i in range(len(t)//2):
        if t[0+i] != t[-1-i]:
            return 'no'

    return 'yes'


if __name__ == "__main__":
    while True:
        text = int(input())
        if text ==0:
            break
        print(is_palindrome(str(text)))
