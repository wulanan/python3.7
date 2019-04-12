#e1.1TempConvert.py
import math
TempStr =eval('input("请输入带有符号的温度值: ")')
if TempStr[-1] in ['F','f']:
    C = math.ceil((eval(TempStr[0:-1]) - 32)/1.8)
    print("转换后的温度是{:d}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = math.ceil(1.8*eval(TempStr[0:-1]) + 32)
    print("转换后的温度是{:d}F".format(F))
else:
    print("输入格式错误")
