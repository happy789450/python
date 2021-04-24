#coding:utf-8
import wx
class Myapp(wx.App):
    def OnInit(self):
        frame=wx.Frame(parent=None,title='hello wxpython')
        frame.Show()
        return True
app=Myapp()
app.MainLoop()