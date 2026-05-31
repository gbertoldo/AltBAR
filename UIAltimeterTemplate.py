# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"AltBAR - UI"), pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.AddGrowableCol( 0 )
        fgSizer1.AddGrowableRow( 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, _(u"Título:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer5.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.textCtrlPlotTitle = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.textCtrlPlotTitle, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.buttonSetPlotTitle = wx.Button( self.m_panel1, wx.ID_ANY, _(u"Alterar"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.buttonSetPlotTitle, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer3.Add( bSizer5, 0, wx.EXPAND, 5 )

        self.panelBase = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3.Add( self.panelBase, 1, wx.EXPAND |wx.ALL, 5 )

        self.textCtrlTerminal = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
        self.textCtrlTerminal.SetForegroundColour( wx.Colour( 0, 196, 0 ) )
        self.textCtrlTerminal.SetBackgroundColour( wx.Colour( 32, 32, 32 ) )
        self.textCtrlTerminal.SetMinSize( wx.Size( -1,150 ) )

        bSizer3.Add( self.textCtrlTerminal, 0, wx.ALL|wx.EXPAND, 5 )


        fgSizer1.Add( bSizer3, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.buttonExtractData = wx.Button( self.m_panel1, wx.ID_ANY, _(u"Extrair dados"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.buttonExtractData.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.buttonExtractData.SetMinSize( wx.Size( -1,60 ) )

        bSizer4.Add( self.buttonExtractData, 0, wx.ALL|wx.EXPAND, 5 )

        self.buttonReport = wx.Button( self.m_panel1, wx.ID_ANY, _(u"Relatório"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.buttonReport.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.buttonReport.SetMinSize( wx.Size( -1,60 ) )

        bSizer4.Add( self.buttonReport, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticline1 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer4.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

        self.buttonClearMemory = wx.Button( self.m_panel1, wx.ID_ANY, _(u"Limpar memória"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.buttonClearMemory.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        self.buttonClearMemory.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
        self.buttonClearMemory.SetBackgroundColour( wx.Colour( 255, 149, 149 ) )
        self.buttonClearMemory.SetMinSize( wx.Size( -1,60 ) )

        bSizer4.Add( self.buttonClearMemory, 0, wx.ALL|wx.EXPAND, 5 )


        fgSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )


        self.m_panel1.SetSizer( fgSizer1 )
        self.m_panel1.Layout()
        fgSizer1.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()
        self.m_menubar1 = wx.MenuBar( 0 )
        self.menuFile = wx.Menu()
        self.menuItemClose = wx.MenuItem( self.menuFile, wx.ID_ANY, _(u"Fechar"), wx.EmptyString, wx.ITEM_NORMAL )
        self.menuFile.Append( self.menuItemClose )

        self.m_menubar1.Append( self.menuFile, _(u"Arquivo") )

        self.menuOperations = wx.Menu()
        self.menuItemExtractData = wx.MenuItem( self.menuOperations, wx.ID_ANY, _(u"Extrair dados"), wx.EmptyString, wx.ITEM_NORMAL )
        self.menuOperations.Append( self.menuItemExtractData )

        self.menuItemReport = wx.MenuItem( self.menuOperations, wx.ID_ANY, _(u"Relatório"), wx.EmptyString, wx.ITEM_NORMAL )
        self.menuOperations.Append( self.menuItemReport )

        self.menuOperations.AppendSeparator()

        self.menuItemClearMemory = wx.MenuItem( self.menuOperations, wx.ID_ANY, _(u"Limpar memória"), wx.EmptyString, wx.ITEM_NORMAL )
        self.menuOperations.Append( self.menuItemClearMemory )

        self.menuOperations.AppendSeparator()

        self.menuItemWriteFirmware = wx.MenuItem( self.menuOperations, wx.ID_ANY, _(u"Gravar firmware"), wx.EmptyString, wx.ITEM_NORMAL )
        self.menuOperations.Append( self.menuItemWriteFirmware )

        self.m_menubar1.Append( self.menuOperations, _(u"Operações") )

        self.menuHelp = wx.Menu()
        self.menuItemAbout = wx.MenuItem( self.menuHelp, wx.ID_ANY, _(u"Sobre"), wx.EmptyString, wx.ITEM_NORMAL )
        self.menuHelp.Append( self.menuItemAbout )

        self.m_menubar1.Append( self.menuHelp, _(u"Ajuda") )

        self.SetMenuBar( self.m_menubar1 )


        self.Centre( wx.BOTH )

        # Connect Events
        self.buttonSetPlotTitle.Bind( wx.EVT_BUTTON, self.onButtonSetPlotTitleClick )
        self.buttonExtractData.Bind( wx.EVT_BUTTON, self.onButtonExtractDataClick )
        self.buttonReport.Bind( wx.EVT_BUTTON, self.onButtonReportClick )
        self.buttonClearMemory.Bind( wx.EVT_BUTTON, self.onButtonClearMemoryClick )
        self.Bind( wx.EVT_MENU, self.onMenuItemClose, id = self.menuItemClose.GetId() )
        self.Bind( wx.EVT_MENU, self.onMenuItemExtractData, id = self.menuItemExtractData.GetId() )
        self.Bind( wx.EVT_MENU, self.onMenuItemReport, id = self.menuItemReport.GetId() )
        self.Bind( wx.EVT_MENU, self.onMenuItemClearMemory, id = self.menuItemClearMemory.GetId() )
        self.Bind( wx.EVT_MENU, self.onMenuItemWriteFirmware, id = self.menuItemWriteFirmware.GetId() )
        self.Bind( wx.EVT_MENU, self.onMenuItemAbout, id = self.menuItemAbout.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onButtonSetPlotTitleClick( self, event ):
        event.Skip()

    def onButtonExtractDataClick( self, event ):
        event.Skip()

    def onButtonReportClick( self, event ):
        event.Skip()

    def onButtonClearMemoryClick( self, event ):
        event.Skip()

    def onMenuItemClose( self, event ):
        event.Skip()

    def onMenuItemExtractData( self, event ):
        event.Skip()

    def onMenuItemReport( self, event ):
        event.Skip()

    def onMenuItemClearMemory( self, event ):
        event.Skip()

    def onMenuItemWriteFirmware( self, event ):
        event.Skip()

    def onMenuItemAbout( self, event ):
        event.Skip()


