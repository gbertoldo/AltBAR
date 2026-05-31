import wx
import wx.adv
import numpy as np
import threading
import UIAltimeterTemplate
import wxMultiPlotPanel
import Altimeter
import UIReportFrame

class MainFrame(UIAltimeterTemplate.MainFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.altimeter = Altimeter.Altimeter(self)
       
        # Plot panel
        self.plotPanel = wxMultiPlotPanel.wxMultiPlotPanel( self.panelBase, ["-*"], 10,100, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.plotPanel.setXLabel("t (s)")
        self.plotPanel.setYLabel("Altura (m)")
        self.plotPanel.setTitle("")
        self.plotPanel.setGrid()
        self.plotPanel.addToolbar()

    def onButtonSetPlotTitleClick( self, event ):
        txt = self.textCtrlPlotTitle.GetValue()
        self.plotPanel.setTitle(txt)
        event.Skip()

    def onButtonExtractDataClick( self, event ):
        self.extractData()
        event.Skip()

    def onButtonReportClick( self, event ):
        self.getReport()
        event.Skip()

    def onButtonClearMemoryClick( self, event ):
        self.clearMemory()
        event.Skip()

    def onMenuItemClose( self, event ):
        self.Destroy()
        event.Skip()

    def onMenuItemExtractData( self, event ):
        self.extractData()
        event.Skip()

    def onMenuItemReport( self, event ):
        self.getReport()
        event.Skip()

    def onMenuItemClearMemory( self, event ):
        self.clearMemory()
        event.Skip()

    def onMenuItemWriteFirmware( self, event ):
        self.writeFirmware()
        event.Skip()

    def onMenuItemAbout( self, event ):
        info = wx.adv.AboutDialogInfo()
        info.SetName("AltBAR - UI")
        info.SetVersion("1.0.0")
        info.SetDescription("Interface gráfica para altímetro AltBAR")
        info.SetCopyright("(C) 2026 Comissão de eletrônicos da BAR")
        info.AddDeveloper("Guilherme Bertoldo")
        info.SetWebSite("https://abmf.bar.org.br/home")

        wx.adv.AboutBox(info, parent=self)
        event.Skip()

    def notify(self, msg):
        wx.CallAfter(self.textCtrlTerminal.AppendText, msg)

    def clear(self):
        self.textCtrlTerminal.Clear()
        x = np.array([0])
        y = np.array([0])
        self.plotPanel.draw([[x,y]])
        self.altimeter.clear()
    
    def extractData(self):
        self.clear()
        thread = threading.Thread(target=self.extractDataBG)
        thread.start()

    def extractDataBG(self):
        self.altimeter.extractData()
        data = self.altimeter.getData()
        if (len(data[0])>0):
            self.plotPanel.draw([data])
        else:
            self.notify("\nMemória vazia!")

    def getReport(self):
        txt = self.altimeter.getReport()   
        reportFrm = UIReportFrame.ReportFrame(self)
        reportFrm.setText(txt)
        reportFrm.Show()

    def clearMemory(self):
        dlg = wx.MessageDialog(
            parent=None, 
            message="Deseja limpar a memória de voo do altímetro?",
            caption="Limpar memória", 
            style=wx.YES_NO | wx.ICON_QUESTION # Use Yes and No buttons with a question icon
        )

        result = dlg.ShowModal()

        if result == wx.ID_YES:
            self.clear()
            thread = threading.Thread(target=self.altimeter.clearEEPROM)
            thread.start()


    def writeFirmware(self):
        dlg = wx.MessageDialog(
            parent=None, 
            message="Deseja gravar o firmware no altímetro? Isto apagará a memória atual.",
            caption="Gravar firmware", 
            style=wx.YES_NO | wx.ICON_QUESTION # Use Yes and No buttons with a question icon
        )

        result = dlg.ShowModal()

        if result == wx.ID_YES:
            self.clear()
            thread = threading.Thread(target=self.altimeter.writeFirmware)
            thread.start()
