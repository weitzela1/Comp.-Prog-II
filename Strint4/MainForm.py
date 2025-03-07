import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(109, 45)
        self._textBox1.Multiline = True
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(200, 75)
        self._textBox1.TabIndex = 0
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(91, 148)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(167, 72)
        self._label1.TabIndex = 1
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(22, 262)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(108, 65)
        self._button1.TabIndex = 2
        self._button1.Text = "button1"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(389, 367)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Strint4"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        wrd = self._textBox1.Text
        reverse = ((wrd::-1))
        
        self._label1.Text = reverse