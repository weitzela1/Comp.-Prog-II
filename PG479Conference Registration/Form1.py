
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
    def __init__(self, parent):
        self.MyParent = parent
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._comboBox1 = System.Windows.Forms.ComboBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._groupBox1.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.Controls.Add(self._checkBox2)
        self._groupBox1.Controls.Add(self._checkBox1)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(12, 12)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(257, 227)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Conference:"
        # 
        # checkBox1
        # 
        self._checkBox1.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._checkBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox1.Location = System.Drawing.Point(6, 28)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(245, 29)
        self._checkBox1.TabIndex = 0
        self._checkBox1.Text = "Conference Registration: $895"
        self._checkBox1.UseVisualStyleBackColor = False
        self._checkBox1.CheckedChanged += self.CheckBox1CheckedChanged
        # 
        # checkBox2
        # 
        self._checkBox2.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._checkBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox2.Location = System.Drawing.Point(6, 63)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(245, 29)
        self._checkBox2.TabIndex = 1
        self._checkBox2.Text = "Opening Night Dinner , Keynote: $30"
        self._checkBox2.UseVisualStyleBackColor = False
        self._checkBox2.CheckedChanged += self.CheckBox2CheckedChanged
        # 
        # groupBox2
        # 
        self._groupBox2.Controls.Add(self._button2)
        self._groupBox2.Controls.Add(self._button1)
        self._groupBox2.Controls.Add(self._comboBox1)
        self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox2.Location = System.Drawing.Point(276, 12)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.Size = System.Drawing.Size(257, 227)
        self._groupBox2.TabIndex = 2
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Preconference Workshops"
        # 
        # comboBox1
        # 
        self._comboBox1.DisplayMember = "test"
        self._comboBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._comboBox1.FormattingEnabled = True
        self._comboBox1.Items.AddRange(System.Array[System.Object](
            ["Intro to E-Commerce",
            "The Future of the Web",
            "Advanced Visual Basic",
            "Network Security"]))
        self._comboBox1.Location = System.Drawing.Point(6, 37)
        self._comboBox1.Name = "comboBox1"
        self._comboBox1.Size = System.Drawing.Size(245, 28)
        self._comboBox1.TabIndex = 0
        self._comboBox1.SelectedIndexChanged += self.ComboBox1SelectedIndexChanged
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ControlDark
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(6, 184)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(116, 37)
        self._button1.TabIndex = 1
        self._button1.Text = "Reset"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ControlDark
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(141, 184)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(116, 37)
        self._button2.TabIndex = 2
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # Form1
        # 
        self.BackColor = System.Drawing.SystemColors.ControlLight
        self.ClientSize = System.Drawing.Size(545, 251)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._groupBox1)
        self.Name = "Form1"
        self.Text = "Form1"
        self._groupBox1.ResumeLayout(False)
        self._groupBox2.ResumeLayout(False)
        self.ResumeLayout(False)


    def Button2Click(self, sender, e):
        self.MyParent.Show()
        self.Hide()

    def Button1Click(self, sender, e):
        pass

    def CheckBox1CheckedChanged(self, sender, e):
        self.MyParent.Conference = 1
        

    def CheckBox2CheckedChanged(self, sender, e):
        self.MyParent.Conference2 = 1

    def ComboBox1SelectedIndexChanged(self, sender, e):
        """
        boom = self._comboBox1.Text
        if boom == "testing":
            self.MyParent.Workshop = 1
        if boom == "why wont this show":
            self.MyParent.Workshop = 2
            """
            