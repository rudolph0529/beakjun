A, B, C = map(int, input().split())

if A == B and B == C:
    print('%d'%(A*1000+10000))
elif A == B :
    print('%d'%(A*100+1000))
elif B == C :
    print('%d'%(B*100+1000))
elif A == C :
    print('%d'%(A*100+1000))
else :
    print('%d'%(max(A,B,C)*100))