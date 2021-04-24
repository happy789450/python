#coding:utf-8

import wx
import os
# wx基本类是app
# APP，oninit初始化
class Myapp(wx.App): #类的继承
    def OnInit(self): #子类覆盖父类的方法
        frame=wx.Frame(parent=None,title='hello wxpython') # 新建一个框架
        panel=wx.Panel(frame,-1) #生成面板
        label1=wx.StaticText(panel,-1,"user",pos=(20,30))
        text1=wx.TextCtrl(panel,-1,pos=(55,30),size=(150,20),
                          style=wx.TE_MULTILINE)
        label2 = wx.StaticText(panel, -1, "pass", pos=(20, 70))
        text2 = wx.TextCtrl(panel, -1, pos=(55, 70), size=(150, 20),
                            style=wx.TE_PASSWORD)  #隐藏输入

        button1 = wx.Button(panel,-1,"login",pos=(50,120)) # 确定按钮位置
        button2 = wx.Button(panel, -1, "clear", pos=(130, 120))
        self.text1 = text1
        self.text2 = text2
        self.button1 = button1
        self.button2 = button2
        self.Bind(wx.EVT_BUTTON,  #绑定事件
                  self.login, #激发的按钮事件
                  self.button1)   #激发的按钮
        self.Bind(wx.EVT_BUTTON,  # 绑定事件
                  self.clear,  # 激发的按钮事件
                  self.button2)  # 激发的按钮
        frame.Show() # 显示
        return True
    def login(self,event):
        user = self.text1.GetValue().strip()  #抓取用户输入去除空格
        passwd = self.text2.GetValue().strip()
        if user=="rice" and passwd=="123456":
            wx.MessageBox("ok","info",wx.OK|wx.ICON_INFORMATION)
        else:
            wx.MessageBox("no", "info", wx.OK | wx.ICON_INFORMATION)
        pass
    def clear(self,event):
        self.text1.SetValue("")
        self.text2.SetValue("")
        pass
app=Myapp() #启动
app.MainLoop() # 进入消息循环