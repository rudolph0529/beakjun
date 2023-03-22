total_price = int(input())
total_item = int(input())

sum_price=0

for i in range(total_item):
    item_price, item_count = map(int, input().split())
    sum_price += item_price*item_count

if total_price == sum_price:
    print('Yes')
else :
    print('No')