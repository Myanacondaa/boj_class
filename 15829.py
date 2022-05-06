import sys
input = sys.stdin.readline

def hash_func(x:str) -> int:
    hash_val = 0
    for i in range(len(x)):
        hash_val += (ord(x[i])-96)*(31**i) #  ASCII of a : 97, so (a-96) is 1.
    return hash_val % 1234567891

if __name__ == "__main__":
    L = int(input())
    x = input()
    print(hash_func(x))

