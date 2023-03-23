N = int(input())
a = input().split()
li = list()

for i in a:
    li.append(int(i))

cnt = int(input())

print(li.count(cnt))