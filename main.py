import wx
import UIAltimeter
import bitmaptools

if __name__ == '__main__':   
  app = wx.App()
  mainFrame = UIAltimeter.MainFrame(parent=None)
  mainFrame.SetIcon(wx.Icon(bitmaptools.resource_path("./fig/bar.png")))
  mainFrame.Show()
  mainFrame.Maximize(True)
  app.MainLoop()