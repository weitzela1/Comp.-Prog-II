import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ControlLight
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(6, 12)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(204, 37)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter word1:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ControlLight
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 124)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(198, 42)
        self._label2.TabIndex = 1
        self._label2.Text = "Anagrams?"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(110, 110, 110)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(216, 124)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(205, 42)
        self._label3.TabIndex = 2
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(216, 12)
        self._textBox1.Multiline = True
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(205, 37)
        self._textBox1.TabIndex = 3
        self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        self._textBox1.TextChanged += self.TextBox1TextChanged
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ControlDark
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 203)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(167, 68)
        self._button1.TabIndex = 4
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ControlDark
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(254, 203)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(167, 68)
        self._button2.TabIndex = 5
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(216, 63)
        self._textBox2.Multiline = True
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(205, 37)
        self._textBox2.TabIndex = 7
        self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ControlLight
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(6, 63)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(204, 37)
        self._label4.TabIndex = 6
        self._label4.Text = "Enter word2:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.Control
        self.ClientSize = System.Drawing.Size(433, 329)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "StrInt1"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()

    def Button1Click(self, sender, e):
        self._label3.Text = ""
        word1 = self._textBox1.Text.lower()
        word2 = self._textBox2.Text.lower()
        
        if len(word1) != len(word2):
            self._label3.Text = "False"
        else:
            for lcv in range(len(word1)):
                c = word1[lcv]
                index = word2.find(c)
                if index == -1:
                    self._label3.Text = "False"
                else:
                    word2 = word2[0:index] + word2[index+1:]
        self._label3.Text = str(len(word2) == 0)
        
        
        pass

    def Button2Click(self, sender, e):
        self._label3.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""

    def TextBox1TextChanged(self, sender, e):
        pass

    def MainFormLoad(self, sender, e):
        pass