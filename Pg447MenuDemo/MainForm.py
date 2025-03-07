import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._menuStrip1 = System.Windows.Forms.MenuStrip()
        self._exitToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._colorToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._helpToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._exitCtrlQToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._rEToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._ctrlQToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._greenToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._blueToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._blackToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._visibleToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._aboutToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._invisibleToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._menuStrip1.SuspendLayout()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 314)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(478, 42)
        self._label1.TabIndex = 0
        self._label1.Text = "Hello World!"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # menuStrip1
        # 
        self._menuStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
            [self._exitToolStripMenuItem,
            self._colorToolStripMenuItem,
            self._helpToolStripMenuItem]))
        self._menuStrip1.Location = System.Drawing.Point(0, 0)
        self._menuStrip1.Name = "menuStrip1"
        self._menuStrip1.Size = System.Drawing.Size(502, 24)
        self._menuStrip1.TabIndex = 1
        self._menuStrip1.Text = "menuStrip1"
        # 
        # exitToolStripMenuItem
        # 
        self._exitToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
            [self._exitCtrlQToolStripMenuItem]))
        self._exitToolStripMenuItem.Name = "exitToolStripMenuItem"
        self._exitToolStripMenuItem.Size = System.Drawing.Size(37, 20)
        self._exitToolStripMenuItem.Text = "File"
        # 
        # colorToolStripMenuItem
        # 
        self._colorToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
            [self._rEToolStripMenuItem,
            self._greenToolStripMenuItem,
            self._blueToolStripMenuItem,
            self._blackToolStripMenuItem,
            self._visibleToolStripMenuItem]))
        self._colorToolStripMenuItem.Name = "colorToolStripMenuItem"
        self._colorToolStripMenuItem.Size = System.Drawing.Size(48, 20)
        self._colorToolStripMenuItem.Text = "Color"
        # 
        # helpToolStripMenuItem
        # 
        self._helpToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
            [self._aboutToolStripMenuItem]))
        self._helpToolStripMenuItem.Name = "helpToolStripMenuItem"
        self._helpToolStripMenuItem.Size = System.Drawing.Size(44, 20)
        self._helpToolStripMenuItem.Text = "Help"
        # 
        # exitCtrlQToolStripMenuItem
        # 
        self._exitCtrlQToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
            [self._ctrlQToolStripMenuItem]))
        self._exitCtrlQToolStripMenuItem.Name = "exitCtrlQToolStripMenuItem"
        self._exitCtrlQToolStripMenuItem.Size = System.Drawing.Size(92, 22)
        self._exitCtrlQToolStripMenuItem.Text = "Exit"
        self._exitCtrlQToolStripMenuItem.Click += self.ExitCtrlQToolStripMenuItemClick
        # 
        # rEToolStripMenuItem
        # 
        self._rEToolStripMenuItem.Name = "rEToolStripMenuItem"
        self._rEToolStripMenuItem.Size = System.Drawing.Size(105, 22)
        self._rEToolStripMenuItem.Text = "Red"
        self._rEToolStripMenuItem.Click += self.REToolStripMenuItemClick
        # 
        # ctrlQToolStripMenuItem
        # 
        self._ctrlQToolStripMenuItem.Name = "ctrlQToolStripMenuItem"
        self._ctrlQToolStripMenuItem.Size = System.Drawing.Size(116, 22)
        self._ctrlQToolStripMenuItem.Text = "Ctrl + Q"
        # 
        # greenToolStripMenuItem
        # 
        self._greenToolStripMenuItem.Name = "greenToolStripMenuItem"
        self._greenToolStripMenuItem.Size = System.Drawing.Size(105, 22)
        self._greenToolStripMenuItem.Text = "Green"
        self._greenToolStripMenuItem.Click += self.GreenToolStripMenuItemClick
        # 
        # blueToolStripMenuItem
        # 
        self._blueToolStripMenuItem.Name = "blueToolStripMenuItem"
        self._blueToolStripMenuItem.Size = System.Drawing.Size(105, 22)
        self._blueToolStripMenuItem.Text = "Blue"
        self._blueToolStripMenuItem.Click += self.BlueToolStripMenuItemClick
        # 
        # blackToolStripMenuItem
        # 
        self._blackToolStripMenuItem.Name = "blackToolStripMenuItem"
        self._blackToolStripMenuItem.Size = System.Drawing.Size(105, 22)
        self._blackToolStripMenuItem.Text = "Black"
        self._blackToolStripMenuItem.Click += self.BlackToolStripMenuItemClick
        # 
        # visibleToolStripMenuItem
        # 
        self._visibleToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
            [self._invisibleToolStripMenuItem]))
        self._visibleToolStripMenuItem.Name = "visibleToolStripMenuItem"
        self._visibleToolStripMenuItem.ShowShortcutKeys = False
        self._visibleToolStripMenuItem.Size = System.Drawing.Size(105, 22)
        self._visibleToolStripMenuItem.Text = "Visible"
        self._visibleToolStripMenuItem.Click += self.VisibleToolStripMenuItemClick
        # 
        # aboutToolStripMenuItem
        # 
        self._aboutToolStripMenuItem.Name = "aboutToolStripMenuItem"
        self._aboutToolStripMenuItem.Size = System.Drawing.Size(152, 22)
        self._aboutToolStripMenuItem.Text = "About"
        self._aboutToolStripMenuItem.Click += self.AboutToolStripMenuItemClick
        # 
        # invisibleToolStripMenuItem
        # 
        self._invisibleToolStripMenuItem.Name = "invisibleToolStripMenuItem"
        self._invisibleToolStripMenuItem.Size = System.Drawing.Size(117, 22)
        self._invisibleToolStripMenuItem.Text = "Invisible"
        self._invisibleToolStripMenuItem.Click += self.InvisibleToolStripMenuItemClick
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(502, 365)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._menuStrip1)
        self.MainMenuStrip = self._menuStrip1
        self.Name = "MainForm"
        self.Text = "Pg447MenuDemo"
        self.Load += self.MainFormLoad
        self._menuStrip1.ResumeLayout(False)
        self._menuStrip1.PerformLayout()
        self.ResumeLayout(False)
        self.PerformLayout()


    def REToolStripMenuItemClick(self, sender, e):
        self._label1.ForeColor = Color.Red

    def BlueToolStripMenuItemClick(self, sender, e):
        self._label1.ForeColor = Color.Blue

    def BlackToolStripMenuItemClick(self, sender, e):
        self._label1.ForeColor = Color.Black

    def MainFormLoad(self, sender, e):
        pass

    def GreenToolStripMenuItemClick(self, sender, e):
        self._label1.ForeColor = Color.Green

    def ExitCtrlQToolStripMenuItemClick(self, sender, e):
        Application.Exit()

    def VisibleToolStripMenuItemClick(self, sender, e):
        self._label1.Text = "Hello World!"

    def InvisibleToolStripMenuItemClick(self, sender, e):
        self._label1.Text = ""

    def AboutToolStripMenuItemClick(self, sender, e):
        MessageBox.Show("Menu System Demo\n"  "Designed for Starting out\n" "with Windows Form Applications" )