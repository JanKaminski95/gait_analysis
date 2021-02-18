import wx
from Video_analyser import *
from coordination.constants import *
from coordination.profiler import *
from coordination.plotter import *

class loaded_S_C_profiler(wx.Panel):
    def __init__(self, parent, gui_size):
        # self.proj_path = proj_path
        self.parent = parent
        self.gui_size = gui_size
        h = self.gui_size[0]
        w = self.gui_size[1]
        wx.Panel.__init__(self, parent, -1, style=wx.SUNKEN_BORDER, size=(w, h))

        # top_sizer = wx.BoxSizer(wx.VERTICAL)
        #
        # self.intro_txt = wx.StaticText(self,
        #                                label='Perform speed, acceleration and coordination analysis.')
        # top_sizer.Add(self.intro_txt, 0, wx.ALL, 5)

        sizer = wx.GridBagSizer(10,7)
        # sizer.Add(top_sizer,pos=(0,0))

        # line = wx.StaticLine(self)
        # sizer.Add(line, pos=(0, 0), span=(0, w), flag=wx.EXPAND | wx.BOTTOM, border=5)

        txt1 = wx.StaticText(self,label = 'Part1: Create speed profiles.')
        font = txt1.GetFont()
        font.PointSize += 0.5
        font = font.Bold()
        txt1.SetFont(font)
        sizer.Add(txt1,pos=(0,0),flag=wx.EXPAND)


        # self.save_np = wx.RadioBox(
        #     self,
        #     label='Want to save results as numpy table?',
        #     choices=['No','Yes'],
        #     majorDimension=1,
        #     style = wx.RA_SPECIFY_COLS,
        # )
        # sizer.Add(self.save_np,pos=(3,0),flag=wx.EXPAND)

        self.load_dir_txt = wx.StaticText(self,label='Select directory with labels:')
        sizer.Add(self.load_dir_txt,pos=(2,0),flag=wx.ALIGN_RIGHT)


        self.load_dir = wx.DirPickerCtrl(
            self,
            path='',
            style=wx.DIRP_USE_TEXTCTRL | wx.DIRP_DIR_MUST_EXIST,
            message='Choose the working directory'
        )
        sizer.Add(self.load_dir, pos=(2, 1), span=wx.DefaultSpan, flag=wx.BOTTOM | wx.EXPAND, border=5)

        # self.proj_path = self.load_dir.GetPath()

        self.save_plot = wx.RadioBox(
            self,
            label='Want to save speed profile plot?',
            choices=['No','Yes'],
            majorDimension=1,
            style = wx.RA_SPECIFY_COLS,
        )
        sizer.Add(self.save_plot,pos=(3,0),flag=wx.EXPAND)

        self.save_log = wx.RadioBox(
            self,
            label='Want to save results as csv(Excel) table?',
            choices=['No','Yes'],
            majorDimension=1,
            style = wx.RA_SPECIFY_COLS,
        )
        sizer.Add(self.save_log,pos=(3,1),flag=wx.EXPAND)


        self.check = wx.Button(self,label='Run speed analysis!')
        sizer.Add(self.check,pos=(4,2),flag=wx.EXPAND)
        self.check.Bind(wx.EVT_BUTTON,self.locomotion)


        line1 = wx.StaticLine(self)
        sizer.Add(line1, pos=(5, 0), span=(1, w), flag=wx.EXPAND | wx.BOTTOM, border=5)




        txt2 = wx.StaticText(self,label='Part2: Create cadence plots and circular plot.')
        font = txt2.GetFont()
        font.PointSize += 0.5
        font = font.Bold()
        txt2.SetFont(font)
        sizer.Add(txt2,pos=(6,0),flag=wx.TOP)



        cadence_txt = wx.Button(self,label='Run coordination analysis')
        sizer.Add(cadence_txt,pos=(7,2),flag=wx.EXPAND)
        cadence_txt.Bind(wx.EVT_BUTTON,self.cadence)

        line2 = wx.StaticLine(self)
        sizer.Add(line2, pos=(8, 0), span=(1, w), flag=wx.EXPAND | wx.BOTTOM, border=5)

        txt3 = wx.StaticText(self,label='Part3: Create acceleration plots with drag and recovery events')
        font = txt3.GetFont()
        font.PointSize += 0.5
        font = font.Bold()
        txt3.SetFont(font)
        sizer.Add(txt3,pos=(9,0))

        tThresh_txt = wx.StaticText(self,label='Specify duration to count a drag/recovery event:')
        sizer.Add(tThresh_txt,pos=(10,0),flag=wx.TOP)


        self.tThresh = wx.SpinCtrlDouble(self,value='',min=0,max=1,initial=0.25,inc=0.05)
        sizer.Add(self.tThresh,pos=(11,0),flag=wx.TOP)

        self.accel = wx.Button(self,label='Run acceleration analysis')
        sizer.Add(self.accel,pos=(11,2),flag=wx.EXPAND)



        self.SetSizer(sizer)
        sizer.Fit(self)


    def locomotion(self,event):

        plotFlag=False
        log=False

        if self.save_plot.GetStringSelection() == 'Yes':
            plotFlag=True
        if self.save_log.GetStringSelection() == 'Yes':
            log=True
        # print('working'+self.load_dir.GetPath())
        locomotionProfiler(data_path=self.load_dir.GetPath(),saveFlag=True, plotFlag=plotFlag, log=log)

    def cadence(self,event):
        combinedPlot(data_path=self.load_dir.GetPath(),saveFlag=False,paperPlot=True)