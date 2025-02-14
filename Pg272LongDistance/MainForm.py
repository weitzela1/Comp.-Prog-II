import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._label1 = System.Windows.Forms.Label()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._label2 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.AppWorkspace
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 389)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(164, 71)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(182, 389)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(164, 71)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.AppWorkspace
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(352, 389)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(164, 71)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.SystemColors.Control
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(224, 30)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(282, 49)
        self._radioButton1.TabIndex = 3
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Daytime"
        self._radioButton1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._radioButton1.UseVisualStyleBackColor = False
        self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.AppWorkspace
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 30)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(206, 159)
        self._label1.TabIndex = 4
        self._label1.Text = "Enter Time of Day:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.SystemColors.Control
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(224, 85)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(282, 49)
        self._radioButton2.TabIndex = 5
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Evening"
        self._radioButton2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._radioButton2.UseVisualStyleBackColor = False
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.SystemColors.Control
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(224, 140)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(282, 49)
        self._radioButton3.TabIndex = 6
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Off-Peak"
        self._radioButton3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._radioButton3.UseVisualStyleBackColor = False
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.AppWorkspace
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 202)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(206, 58)
        self._label2.TabIndex = 7
        self._label2.Text = "Enter amount of time in minutes:   "
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.SystemColors.ScrollBar
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(224, 202)
        self._textBox1.Multiline = True
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(282, 58)
        self._textBox1.TabIndex = 8
        self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.AppWorkspace
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 299)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(164, 58)
        self._label3.TabIndex = 9
        self._label3.Text = "Price:  "
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(182, 299)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(324, 58)
        self._label4.TabIndex = 10
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ControlLight
        self.ClientSize = System.Drawing.Size(518, 472)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Pg272LongDistance"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        time = int(self._textBox1.Text)
        rate = 0.0
        if self._radioButton1.Checked:
            rate = 0.07
            total = time * rate
        if self._radioButton2.Checked:
            rate = 0.12
            total = time * rate
           
        if self._radioButton3.Checked:
            rate = 0.05
            total = time * rate
            
        self._label4.Text = str(total)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._label4.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def RadioButton1CheckedChanged(self, sender, e):
        pass