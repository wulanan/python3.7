#e2.1DrawPython.py
import turtle
turtle.setup(650, 350, 200, 200)
'''
turtle.setup(width=0.5,height=0.75,startx=None,starty=None)，
参数：width,height:输入宽和高为整数时,表示像素;为小数时,表示占据电脑屏幕的比例，
(startx,starty):这一坐标表示矩形窗口左上角顶点的位置,如果为空,则窗口位于屏幕中心。
'''
turtle.penup()  #提起笔移动，不绘制图形，用于另起一个地方绘制
turtle.fd(-250) #turtle.forward(distance）向当前画笔方向移动distance像素长度
turtle.pendown() #移动时绘制图形，缺省时也为绘制
turtle.pensize(25) #设置画笔的宽度
turtle.pencolor("purple") #没有参数传入，返回当前画笔颜色，传入参数设置画笔颜色
turtle.seth(-40) #逆时针旋转angle度,seth()只改变方向但不行进
for i in range(4):
    turtle.circle(40, 80) #turtle.circle(r, extent=None),根据半径r绘制extent角度的弧形 
    turtle.circle(-40, 80) #r默认圆心在海龟左侧r距离的位置, extent: 绘制角度，默认是360度整圆
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
