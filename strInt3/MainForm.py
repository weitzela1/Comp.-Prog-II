import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button2 = System.Windows.Forms.Button()
        self._button1 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ControlDark
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(204, 224)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(167, 68)
        self._button2.TabIndex = 13
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ControlDark
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 224)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(167, 68)
        self._button1.TabIndex = 12
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(222, 23)
        self._textBox1.Multiline = True
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(347, 56)
        self._textBox1.TabIndex = 11
        self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(110, 110, 110)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(222, 105)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(341, 55)
        self._label3.TabIndex = 10
        self._label3.Click += self.Label3Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ControlLight
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 105)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(198, 55)
        self._label2.TabIndex = 9
        self._label2.Text = "First nonrepeated letter:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ControlLight
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 23)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(198, 59)
        self._label1.TabIndex = 8
        self._label1.Text = "Enter word:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.ControlDark
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(402, 224)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(167, 68)
        self._button3.TabIndex = 14
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ButtonFace
        self.ClientSize = System.Drawing.Size(581, 305)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "strInt3"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label3Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        self._label3.Text = ""
        wrd = self._textBox1.Text.lower()
        n = len(wrd)
        for lcv in range(wrd):
            if lcv[0] 
            
        

            

            
        

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._label3.Text = ""