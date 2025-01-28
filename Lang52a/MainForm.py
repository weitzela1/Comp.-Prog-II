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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.DimGray
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(36, 26)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(137, 53)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter Length:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.DimGray
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(36, 107)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(137, 53)
        self._label2.TabIndex = 1
        self._label2.Text = "Enter Width:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.SystemColors.ScrollBar
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(199, 26)
        self._textBox1.Multiline = True
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(161, 53)
        self._textBox1.TabIndex = 2
        self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.SystemColors.ScrollBar
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(199, 107)
        self._textBox2.Multiline = True
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(161, 53)
        self._textBox2.TabIndex = 3
        self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.DimGray
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(36, 234)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(137, 53)
        self._label3.TabIndex = 4
        self._label3.Text = "Area:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.DimGray
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(36, 310)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(137, 53)
        self._label4.TabIndex = 5
        self._label4.Text = "Perimeter:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Gray
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(199, 234)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(161, 53)
        self._label5.TabIndex = 6
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.Gray
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(199, 310)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(161, 53)
        self._label6.TabIndex = 7
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ControlLight
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(20, 394)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(140, 71)
        self._button1.TabIndex = 8
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ControlLight
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(199, 393)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(140, 71)
        self._button2.TabIndex = 9
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.ControlLight
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(382, 393)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(140, 71)
        self._button3.TabIndex = 10
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.AppWorkspace
        self.ClientSize = System.Drawing.Size(546, 476)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Lang52a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        """
        Notes:
        Date Types:
            - int (integer): Whole Number
            - float (Float-point Number): Number w decima
            - str (String): Text
            
        Operators: + - * / % (mod) **(power) //(floor divide)
        
        
        
        
        """
        length = int(self._textBox1.Text)
        width = int(self._textBox2.Text)
        
        area = length * width
        per = length * 2 + width * 2
        
        self._label5.Text = str(area)
        self._label6.Text = str(per)
       

    def Button2Click(self, sender, e):
        self._label5.Text = ""
        self._label6.Text = ""
        self._textBox1.Text = ("")
        self._textBox2.Text = ("")

    def Button3Click(self, sender, e):
        Application.Exit()