# 呜呜呜MLE（内存超限啦 
n,m=map(int,input().split())
input_str=input()
a=list(map(int,input_str.split()))
input_str1=input()
b=list(map(int,input_str1.split()))
for i in range(m):
    print(a[b[i]-1])
