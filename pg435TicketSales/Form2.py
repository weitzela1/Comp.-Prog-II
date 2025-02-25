
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form2(Form):
    def __init__(self, parent):
        self.Myparent = parent
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._label8 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._groupBox2.SuspendLayout()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(188, 26)
        self._label1.TabIndex = 1
        self._label1.Text = "How many Tickets?"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 60)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(125, 26)
        self._label2.TabIndex = 2
        self._label2.Text = "Number of Tickets:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(143, 60)
        self._textBox1.Multiline = True
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(56, 26)
        self._textBox1.TabIndex = 3
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 114)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(187, 55)
        self._label3.TabIndex = 4
        self._label3.Text = "Student Tickets are for student seating in the student section only."
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # groupBox2
        # 
        self._groupBox2.Controls.Add(self._label8)
        self._groupBox2.Controls.Add(self._label7)
        self._groupBox2.Controls.Add(self._label6)
        self._groupBox2.Controls.Add(self._label5)
        self._groupBox2.Controls.Add(self._label9)
        self._groupBox2.Controls.Add(self._label10)
        self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox2.Location = System.Drawing.Point(205, 45)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.Size = System.Drawing.Size(180, 124)
        self._groupBox2.TabIndex = 6
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Total Costs"
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.SystemColors.Menu
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(108, 78)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(66, 22)
        self._label8.TabIndex = 5
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.SystemColors.Menu
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(108, 49)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(66, 22)
        self._label7.TabIndex = 4
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.Menu
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(108, 19)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(66, 22)
        self._label6.TabIndex = 3
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.Control
        self._label5.Location = System.Drawing.Point(6, 77)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(96, 23)
        self._label5.TabIndex = 2
        self._label5.Text = "Total:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.SystemColors.Control
        self._label9.Location = System.Drawing.Point(6, 48)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(96, 23)
        self._label9.TabIndex = 1
        self._label9.Text = "Tax:"
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.SystemColors.Control
        self._label10.Location = System.Drawing.Point(6, 19)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(96, 23)
        self._label10.TabIndex = 0
        self._label10.Text = "Tickets:"
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ButtonFace
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(69, 200)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(131, 28)
        self._button1.TabIndex = 7
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ButtonFace
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(206, 200)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(131, 28)
        self._button2.TabIndex = 8
        self._button2.Text = "Close"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # Form2
        # 
        self.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self.ClientSize = System.Drawing.Size(395, 252)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "Form2"
        self.Text = "Form2"
        self.Load += self.Form2Load
        self._groupBox2.ResumeLayout(False)
        self.ResumeLayout(False)
        self.PerformLayout()


    def Form2Load(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        ticketstu = (int(self._textBox1.Text))
        total = ticketstu * 20
        tax = total * 1.06 - total
        ttotal = total * 1.06
        self._label6.Text = str(total)
        self._label7.Text = str(tax)
        self._label8.Text = str(ttotal)

    def Button2Click(self, sender, e):
        self.Myparent.Show()
        
        self.Close()