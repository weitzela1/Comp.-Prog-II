import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._menuStrip1 = System.Windows.Forms.MenuStrip()
        self._planetsToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._mercuryToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._venusToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._earthToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._marsToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._jupiterToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._saturnToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._uToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._neptuneToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._button1 = System.Windows.Forms.Button()
        self._otherInfoToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._aUToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._plutoToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._menuStrip1.SuspendLayout()
        self.SuspendLayout()
        # 
        # menuStrip1
        # 
        self._menuStrip1.BackColor = System.Drawing.Color.Navy
        self._menuStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
            [self._planetsToolStripMenuItem,
            self._otherInfoToolStripMenuItem]))
        self._menuStrip1.Location = System.Drawing.Point(0, 0)
        self._menuStrip1.Name = "menuStrip1"
        self._menuStrip1.Size = System.Drawing.Size(410, 24)
        self._menuStrip1.TabIndex = 0
        self._menuStrip1.Text = "menuStrip1"
        # 
        # planetsToolStripMenuItem
        # 
        self._planetsToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
            [self._mercuryToolStripMenuItem,
            self._venusToolStripMenuItem,
            self._earthToolStripMenuItem,
            self._marsToolStripMenuItem,
            self._jupiterToolStripMenuItem,
            self._saturnToolStripMenuItem,
            self._uToolStripMenuItem,
            self._neptuneToolStripMenuItem,
            self._plutoToolStripMenuItem]))
        self._planetsToolStripMenuItem.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._planetsToolStripMenuItem.Name = "planetsToolStripMenuItem"
        self._planetsToolStripMenuItem.Size = System.Drawing.Size(98, 20)
        self._planetsToolStripMenuItem.Text = "Select a Planet:"
        self._planetsToolStripMenuItem.Click += self.PlanetsToolStripMenuItemClick
        # 
        # mercuryToolStripMenuItem
        # 
        self._mercuryToolStripMenuItem.Name = "mercuryToolStripMenuItem"
        self._mercuryToolStripMenuItem.Size = System.Drawing.Size(120, 22)
        self._mercuryToolStripMenuItem.Text = "Mercury"
        self._mercuryToolStripMenuItem.Click += self.MercuryToolStripMenuItemClick
        # 
        # venusToolStripMenuItem
        # 
        self._venusToolStripMenuItem.Name = "venusToolStripMenuItem"
        self._venusToolStripMenuItem.Size = System.Drawing.Size(120, 22)
        self._venusToolStripMenuItem.Text = "Venus"
        self._venusToolStripMenuItem.Click += self.VenusToolStripMenuItemClick
        # 
        # earthToolStripMenuItem
        # 
        self._earthToolStripMenuItem.Name = "earthToolStripMenuItem"
        self._earthToolStripMenuItem.Size = System.Drawing.Size(120, 22)
        self._earthToolStripMenuItem.Text = "Earth"
        self._earthToolStripMenuItem.Click += self.EarthToolStripMenuItemClick
        # 
        # marsToolStripMenuItem
        # 
        self._marsToolStripMenuItem.Name = "marsToolStripMenuItem"
        self._marsToolStripMenuItem.Size = System.Drawing.Size(120, 22)
        self._marsToolStripMenuItem.Text = "Mars"
        self._marsToolStripMenuItem.Click += self.MarsToolStripMenuItemClick
        # 
        # jupiterToolStripMenuItem
        # 
        self._jupiterToolStripMenuItem.Name = "jupiterToolStripMenuItem"
        self._jupiterToolStripMenuItem.Size = System.Drawing.Size(120, 22)
        self._jupiterToolStripMenuItem.Text = "Jupiter"
        self._jupiterToolStripMenuItem.Click += self.JupiterToolStripMenuItemClick
        # 
        # saturnToolStripMenuItem
        # 
        self._saturnToolStripMenuItem.Name = "saturnToolStripMenuItem"
        self._saturnToolStripMenuItem.Size = System.Drawing.Size(120, 22)
        self._saturnToolStripMenuItem.Text = "Saturn"
        self._saturnToolStripMenuItem.Click += self.SaturnToolStripMenuItemClick
        # 
        # uToolStripMenuItem
        # 
        self._uToolStripMenuItem.Name = "uToolStripMenuItem"
        self._uToolStripMenuItem.Size = System.Drawing.Size(120, 22)
        self._uToolStripMenuItem.Text = "Uranus"
        self._uToolStripMenuItem.Click += self.UToolStripMenuItemClick
        # 
        # neptuneToolStripMenuItem
        # 
        self._neptuneToolStripMenuItem.Name = "neptuneToolStripMenuItem"
        self._neptuneToolStripMenuItem.Size = System.Drawing.Size(120, 22)
        self._neptuneToolStripMenuItem.Text = "Neptune"
        self._neptuneToolStripMenuItem.Click += self.NeptuneToolStripMenuItemClick
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Lavender
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(276, 348)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(122, 47)
        self._button1.TabIndex = 1
        self._button1.Text = "EXIT"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # otherInfoToolStripMenuItem
        # 
        self._otherInfoToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
            [self._aUToolStripMenuItem]))
        self._otherInfoToolStripMenuItem.ForeColor = System.Drawing.SystemColors.ActiveCaption
        self._otherInfoToolStripMenuItem.Name = "otherInfoToolStripMenuItem"
        self._otherInfoToolStripMenuItem.Size = System.Drawing.Size(76, 20)
        self._otherInfoToolStripMenuItem.Text = "Other Info:"
        # 
        # aUToolStripMenuItem
        # 
        self._aUToolStripMenuItem.Name = "aUToolStripMenuItem"
        self._aUToolStripMenuItem.Size = System.Drawing.Size(196, 22)
        self._aUToolStripMenuItem.Text = "1 AU = 93 million miles"
        # 
        # plutoToolStripMenuItem
        # 
        self._plutoToolStripMenuItem.Name = "plutoToolStripMenuItem"
        self._plutoToolStripMenuItem.Size = System.Drawing.Size(120, 22)
        self._plutoToolStripMenuItem.Text = "Pluto"
        self._plutoToolStripMenuItem.Click += self.PlutoToolStripMenuItemClick
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkBlue
        self.ClientSize = System.Drawing.Size(410, 407)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._menuStrip1)
        self.MainMenuStrip = self._menuStrip1
        self.Name = "MainForm"
        self.Text = "Pg486Astronomy"
        self.Load += self.MainFormLoad
        self._menuStrip1.ResumeLayout(False)
        self._menuStrip1.PerformLayout()
        self.ResumeLayout(False)
        self.PerformLayout()


    def PlanetsToolStripMenuItemClick(self, sender, e):
        pass

    def MainFormLoad(self, sender, e):
        pass

    def MercuryToolStripMenuItemClick(self, sender, e):
        from Form1 import *
        form1 = Form1(self)
        form1.Show()
        self.Hide()
  

    def Button1Click(self, sender, e):
        Application.Exit()

    def VenusToolStripMenuItemClick(self, sender, e):
        from Form2 import *
        form2 = Form2(self)
        form2.Show()
        self.Hide()

    def EarthToolStripMenuItemClick(self, sender, e):
        from Form3 import *
        form3 = Form3(self)
        form3.Show()
        self.Hide()        

    def MarsToolStripMenuItemClick(self, sender, e):
        from Form4 import *
        form4 = Form4(self)
        form4.Show()
        self.Hide()       

    def JupiterToolStripMenuItemClick(self, sender, e):
        from Form5 import *
        form5 = Form5(self)
        form5.Show()
        self.Hide()      

    def SaturnToolStripMenuItemClick(self, sender, e):
        from Form6 import *
        form6 = Form6(self)
        form6.Show()
        self.Hide()  

    def NeptuneToolStripMenuItemClick(self, sender, e):
        from Form8 import *
        form8 = Form8(self)
        form8.Show()
        self.Hide()                
        

    def UToolStripMenuItemClick(self, sender, e):
        from Form7 import *
        form7 = Form7(self)
        form7.Show()
        self.Hide()

    def PlutoToolStripMenuItemClick(self, sender, e):
        from Form9 import *
        form9 = Form9(self)
        form9.Show()
        self.Hide()