#coding:utf-8

import wx
# wx基本类是app
# APP，oninit初始化
class Myapp(wx.App): #类的继承
    def OnInit(self): #子类覆盖父类的方法
        frame=wx.Frame(parent=None,title='hello wxpython') # 新建一个框架
        panel=wx.Panel(frame,-1) #生成面板
        button=wx.Button(panel,-1,"hello",pos=(50,50)) # 确定按钮位置

        frame.Show() # 显示
        return True

app=Myapp() #启动
app.MainLoop() # 进入消息循环