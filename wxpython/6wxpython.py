#coding:utf-8

import wx
import os
# wx基本类是app
# APP，oninit初始化
class Myapp(wx.App): #类的继承
    def OnInit(self): #子类覆盖父类的方法
        frame=wx.Frame(parent=None,title='hello wxpython') # 新建一个框架
        panel=wx.Panel(frame,-1) #生成面板
        label1=wx.StaticText(panel,-1,"MutilLine",pos=(20,30))
        text1=wx.TextCtrl(panel,-1,pos=(100,100),size=(150,20),
                          style=wx.TE_MULTILINE)



        button=wx.Button(panel,-1,"run",pos=(100,50)) # 确定按钮位置
        self.text1=text1

        # self.button1=button
        # self.Bind(wx.EVT_BUTTON,  #绑定事件
        #           self.Onbutton1, #激发的按钮事件
        #           self.button1)   #激发的按钮
        frame.Show() # 显示
        return True
    # def Onbutton1(self,event):
    #     self.button1.SetLabel("nimei")
    #     os.system(self.text1.GetValue())
app=Myapp() #启动
app.MainLoop() # 进入消息循环