H, M = map(int,input().split())

if H < 0 or H > 23 or M < 0 or M > 59 :
    print('입력 오류입니다.')
elif H == 0 and M < 45 :
    print('%d %d'%(23, M+60-45))
elif H != 0 and M < 45 :
    print('%d %d'%(H-1, M+60-45))
else:
    print('%d %d'%(H, M-45))