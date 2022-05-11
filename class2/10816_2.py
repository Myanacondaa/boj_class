import sys
from collections import Counter
input = sys.stdin.readline

def number_of_card(x:list[int], y:list[int]): # print number of cards that right
    dic = Counter(x)
    for ele in y:
        if ele in dic:
            print(dic[ele], end=' ')
        else:
            print(0, end=' ')



if __name__ == "__main__":
    N = int(input()) # input number of card
    card = list(map(int, input().split())) # input card number
    M = int(input()) # input number of guesses
    num = list(map(int, input().split())) # input guess card
    number_of_card(card, num)
