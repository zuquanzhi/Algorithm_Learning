n,p=map(int,input().split())
mapping={}
for i in range(p):
    input_str=input()
    input1=list(map(int,input_str.split()))
    if input1[0]==1:
        mapping.update({(input1[1],input1[2]):input1[3]})  #字典添加元素直接dict.update(),没有=
    else:print(mapping[input1[1],input1[2]])
