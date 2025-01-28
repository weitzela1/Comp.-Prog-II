import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 18)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(166, 58)
        self._label1.TabIndex = 0
        self._label1.Text = "Please put in 3 digit #'s"
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(194, 18)
        self._textBox1.Multiline = True
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(152, 58)
        self._textBox1.TabIndex = 1
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(374, 18)
        self._textBox2.Multiline = True
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(152, 58)
        self._textBox2.TabIndex = 2
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(194, 82)
        self._textBox3.Multiline = True
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(152, 58)
        self._textBox3.TabIndex = 3
        # 
        # textBox4
        # 
        self._textBox4.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(374, 82)
        self._textBox4.Multiline = True
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(152, 58)
        self._textBox4.TabIndex = 4
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 186)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(166, 58)
        self._label2.TabIndex = 5
        self._label2.Text = "Sum:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 266)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(166, 58)
        self._label3.TabIndex = 6
        self._label3.Text = "Average:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.AliceBlue
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(194, 186)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(332, 58)
        self._label4.TabIndex = 7
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(194, 266)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(332, 58)
        self._label5.TabIndex = 8
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.DeepSkyBlue
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 373)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(153, 94)
        self._button1.TabIndex = 9
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.DeepSkyBlue
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(205, 373)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(153, 94)
        self._button2.TabIndex = 10
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DeepSkyBlue
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(392, 373)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(153, 94)
        self._button3.TabIndex = 11
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.SteelBlue
        self.ClientSize = System.Drawing.Size(557, 479)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog54a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        first = int(self._textBox1.Text)
        second = int(self._textBox2.Text)
        third = int(self._textBox3.Text)
        fourth = int(self._textBox4.Text)
        
        sum = first + second + third + fourth
        average = (first + second + third + fourth) / 4
        
        self._label4.Text = str(sum)
        self._label5.Text = str(average)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox4.Text = ""
        self._label4.Text = ""
        self._label5.Text = ""