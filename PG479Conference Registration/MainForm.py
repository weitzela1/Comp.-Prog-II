import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        self.Conference = 0
        self.Conference2 = 0
        self.Workshop = 0
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._textBox5 = System.Windows.Forms.TextBox()
        self._textBox6 = System.Windows.Forms.TextBox()
        self._label7 = System.Windows.Forms.Label()
        self._textBox7 = System.Windows.Forms.TextBox()
        self._label8 = System.Windows.Forms.Label()
        self._textBox8 = System.Windows.Forms.TextBox()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._groupBox1.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.Controls.Add(self._textBox8)
        self._groupBox1.Controls.Add(self._label8)
        self._groupBox1.Controls.Add(self._textBox7)
        self._groupBox1.Controls.Add(self._label7)
        self._groupBox1.Controls.Add(self._textBox6)
        self._groupBox1.Controls.Add(self._textBox5)
        self._groupBox1.Controls.Add(self._label6)
        self._groupBox1.Controls.Add(self._label5)
        self._groupBox1.Controls.Add(self._textBox4)
        self._groupBox1.Controls.Add(self._textBox3)
        self._groupBox1.Controls.Add(self._textBox2)
        self._groupBox1.Controls.Add(self._textBox1)
        self._groupBox1.Controls.Add(self._label4)
        self._groupBox1.Controls.Add(self._label3)
        self._groupBox1.Controls.Add(self._label2)
        self._groupBox1.Controls.Add(self._label1)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(12, 12)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(611, 238)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Registrant"
        self._groupBox1.Enter += self.GroupBox1Enter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(6, 76)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(110, 32)
        self._label2.TabIndex = 1
        self._label2.Text = "Company:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(6, 117)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(110, 32)
        self._label3.TabIndex = 2
        self._label3.Text = "Adress:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(6, 159)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(110, 32)
        self._label4.TabIndex = 3
        self._label4.Text = "City:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(122, 159)
        self._textBox1.Multiline = True
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(112, 32)
        self._textBox1.TabIndex = 4
        self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(122, 35)
        self._textBox2.Multiline = True
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(112, 32)
        self._textBox2.TabIndex = 5
        self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        self._textBox2.TextChanged += self.TextBox2TextChanged
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(122, 76)
        self._textBox3.Multiline = True
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(112, 32)
        self._textBox3.TabIndex = 6
        self._textBox3.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # textBox4
        # 
        self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(122, 117)
        self._textBox4.Multiline = True
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(112, 32)
        self._textBox4.TabIndex = 7
        self._textBox4.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(6, 35)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(110, 32)
        self._label1.TabIndex = 0
        self._label1.Text = "Name:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(338, 35)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(110, 32)
        self._label5.TabIndex = 8
        self._label5.Text = "Phone:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(338, 76)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(110, 32)
        self._label6.TabIndex = 9
        self._label6.Text = "Email:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # textBox5
        # 
        self._textBox5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox5.Location = System.Drawing.Point(454, 38)
        self._textBox5.Multiline = True
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(112, 32)
        self._textBox5.TabIndex = 10
        self._textBox5.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # textBox6
        # 
        self._textBox6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox6.Location = System.Drawing.Point(454, 79)
        self._textBox6.Multiline = True
        self._textBox6.Name = "textBox6"
        self._textBox6.Size = System.Drawing.Size(112, 32)
        self._textBox6.TabIndex = 11
        self._textBox6.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(240, 159)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(110, 32)
        self._label7.TabIndex = 12
        self._label7.Text = "State:"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # textBox7
        # 
        self._textBox7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox7.Location = System.Drawing.Point(356, 159)
        self._textBox7.Multiline = True
        self._textBox7.Name = "textBox7"
        self._textBox7.Size = System.Drawing.Size(92, 32)
        self._textBox7.TabIndex = 13
        self._textBox7.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(454, 159)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(46, 32)
        self._label8.TabIndex = 14
        self._label8.Text = "ZIP:"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # textBox8
        # 
        self._textBox8.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox8.Location = System.Drawing.Point(506, 159)
        self._textBox8.Multiline = True
        self._textBox8.Name = "textBox8"
        self._textBox8.Size = System.Drawing.Size(99, 32)
        self._textBox8.TabIndex = 15
        self._textBox8.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(252, 253)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(208, 29)
        self._label9.TabIndex = 1
        self._label9.Text = "Total Cost:"
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.SystemColors.ControlLightLight
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(472, 253)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(144, 28)
        self._label10.TabIndex = 2
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.AppWorkspace
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(18, 304)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(172, 48)
        self._button1.TabIndex = 3
        self._button1.Text = "Select Conference Options:"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.AppWorkspace
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(234, 373)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(172, 74)
        self._button2.TabIndex = 4
        self._button2.Text = "Reset"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.AppWorkspace
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(451, 373)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(172, 74)
        self._button3.TabIndex = 5
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.BackColor = System.Drawing.SystemColors.AppWorkspace
        self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(18, 373)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(172, 74)
        self._button4.TabIndex = 6
        self._button4.Text = "Calculate"
        self._button4.UseVisualStyleBackColor = False
        self._button4.Click += self.Button4Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ControlLight
        self.ClientSize = System.Drawing.Size(635, 459)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._groupBox1)
        self.Name = "MainForm"
        self.Text = "PG479Conference Registration"
        self._groupBox1.ResumeLayout(False)
        self._groupBox1.PerformLayout()
        self.ResumeLayout(False)


    def GroupBox1Enter(self, sender, e):
        pass

    def TextBox2TextChanged(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        from Form1 import *
        form1 = Form1(self)
        form1.Show()
        self.Hide()

    def Button2Click(self, sender, e):
        self._label10.Text = ""
        self._textBox1.Text = ("")
        self._textBox2.Text = ("")
        self._textBox3.Text = ("")
        self._textBox4.Text = ("")
        self._textBox5.Text = ("")
        self._textBox6.Text = ("")
        self._textBox7.Text = ("")
        self._textBox8.Text = ("")

    def Button4Click(self, sender, e):
        regis = 0
        extra = 0
        if self.Conference == 1:
            regis = 895
        else:
            regis = 0
        if self.Conference2 == 1:
            extra = 30
        else:
            extra = 0
        total = regis + extra
        self._label10.Text = str(total)
 
        

    def Button3Click(self, sender, e):
        Application.Exit()