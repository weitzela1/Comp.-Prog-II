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
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(210, 50)
        self._label1.TabIndex = 0
        self._label1.Text = "The radius of the circle:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 148)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(210, 50)
        self._label2.TabIndex = 2
        self._label2.Text = "Area:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 208)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(210, 50)
        self._label3.TabIndex = 3
        self._label3.Text = "Perimeter:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(244, 148)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(255, 49)
        self._label4.TabIndex = 4
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(244, 209)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(255, 49)
        self._label5.TabIndex = 5
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ButtonFace
        self._button1.Cursor = System.Windows.Forms.Cursors.Hand
        self._button1.FlatStyle = System.Windows.Forms.FlatStyle.System
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 387)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(138, 96)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ButtonFace
        self._button2.Cursor = System.Windows.Forms.Cursors.Hand
        self._button2.FlatStyle = System.Windows.Forms.FlatStyle.System
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(215, 387)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(138, 96)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.ButtonFace
        self._button3.Cursor = System.Windows.Forms.Cursors.Hand
        self._button3.FlatStyle = System.Windows.Forms.FlatStyle.System
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(425, 387)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(138, 96)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(241, 12)
        self._textBox1.Multiline = True
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(322, 47)
        self._textBox1.TabIndex = 1
        self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ControlDark
        self.ClientSize = System.Drawing.Size(575, 495)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Lang54c"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        rad = int(self._textBox1.Text)
        area = (rad**2) * 3.14159
        perim = rad * 2 * 3.14159
        
        self._label4.Text = str(round(area, 2))
        self._label5.Text = str(round(perim, 2))

    def Button2Click(self, sender, e):
        self._label4.Text = ""
        self._label5.Text = ""
        self._textBox1.Text = ("")

    def Button3Click(self, sender, e):
        Application.Exit()