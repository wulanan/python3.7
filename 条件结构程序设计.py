#求学生分数的平均值
flag="y"
sum=0.0
counter=0
while flag=="y":
    x=int(input("请输入学生的分数："))
    sum=sum+x
    counter=counter+1
    flag=input("输入y还是n：")
print ("#求学生分数的平均值为：",sum/counter)
