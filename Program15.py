n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

only_english = english.difference(french)

print(len(only_english))