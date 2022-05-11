import sys
input = sys.stdin.readline

def gcd(x:int, y:int) -> int:
    if x < y:
        x,y = y, x

    if x%y ==0:
        return y

    else:
        return gcd(y, x%y)


def lcm(x:int, y:int, greatest_common_factor) -> int:
    return int(x*y/greatest_common_factor)


if __name__ == "__main__":
    N, M = map(int, input().split())
    greatest_common_factor = gcd(N, M)
    print(greatest_common_factor)
    print(lcm(N, M, greatest_common_factor))