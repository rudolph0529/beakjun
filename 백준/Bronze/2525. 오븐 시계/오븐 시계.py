H, M = map(int, input().split())
smoke_time = int(input())

if H+(M+smoke_time)//60 > 23 :
    print('%d %d'%((H+(M+smoke_time)//60)-24, (M+smoke_time)%60))
else :
    print('%d %d'%(H+(M+smoke_time)//60, (M+smoke_time)%60))