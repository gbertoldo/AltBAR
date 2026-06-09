import wx
###########################################################################
## Class ReportFrame
###########################################################################

class ReportFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer14 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer15 = wx.BoxSizer( wx.VERTICAL )

        self.txtCtrlLog = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
        bSizer15.Add( self.txtCtrlLog, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

        self.btnCancel = wx.Button( self.m_panel5, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer16.Add( self.btnCancel, 0, wx.ALL, 5 )

        self.btnSave = wx.Button( self.m_panel5, wx.ID_ANY, u"Salvar", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer16.Add( self.btnSave, 0, wx.ALL, 5 )


        bSizer15.Add( bSizer16, 0, wx.ALIGN_RIGHT, 5 )


        self.m_panel5.SetSizer( bSizer15 )
        self.m_panel5.Layout()
        bSizer15.Fit( self.m_panel5 )
        bSizer14.Add( self.m_panel5, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer14 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.btnCancel.Bind( wx.EVT_BUTTON, self.onBtnCancel )
        self.btnSave.Bind( wx.EVT_BUTTON, self.onBtnSave )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onBtnCancel( self, event ):
        event.Skip()

    def onBtnSave( self, event ):
        event.Skip()

