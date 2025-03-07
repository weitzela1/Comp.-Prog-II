
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
    def __init__(self, parent):
        self.Myparent = parent
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._groupBox1.SuspendLayout()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(229, 27)
        self._label1.TabIndex = 0
        self._label1.Text = "How many Tickets?"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 47)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(229, 27)
        self._label2.TabIndex = 1
        self._label2.Text = "# of Tickets:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label2.Click += self.Label2Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(247, 47)
        self._textBox1.Multiline = True
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(140, 27)
        self._textBox1.TabIndex = 2
        self._textBox1.TextChanged += self.TextBox1TextChanged
        # 
        # groupBox1
        # 
        self._groupBox1.Controls.Add(self._radioButton3)
        self._groupBox1.Controls.Add(self._radioButton2)
        self._groupBox1.Controls.Add(self._radioButton1)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(12, 101)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(186, 229)
        self._groupBox1.TabIndex = 3
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Section"
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.SystemColors.ControlDark
        self._radioButton1.Location = System.Drawing.Point(6, 35)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(179, 30)
        self._radioButton1.TabIndex = 0
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Section A"
        self._radioButton1.UseVisualStyleBackColor = False
        self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.SystemColors.ControlDark
        self._radioButton2.Location = System.Drawing.Point(4, 99)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(179, 30)
        self._radioButton2.TabIndex = 1
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Section B"
        self._radioButton2.UseVisualStyleBackColor = False
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.SystemColors.ControlDark
        self._radioButton3.Location = System.Drawing.Point(4, 163)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(179, 30)
        self._radioButton3.TabIndex = 2
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Section C"
        self._radioButton3.UseVisualStyleBackColor = False
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(204, 136)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(183, 27)
        self._label3.TabIndex = 4
        self._label3.Text = "Total Costs:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label3.Click += self.Label3Click
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(204, 179)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(91, 27)
        self._label4.TabIndex = 5
        self._label4.Text = "Tickets"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(204, 225)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(91, 27)
        self._label5.TabIndex = 6
        self._label5.Text = "Tax"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(204, 267)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(91, 27)
        self._label6.TabIndex = 7
        self._label6.Text = "Total"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.SystemColors.Control
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(301, 179)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(86, 27)
        self._label7.TabIndex = 8
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.SystemColors.Control
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(301, 225)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(86, 30)
        self._label8.TabIndex = 9
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.SystemColors.Control
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(301, 267)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(86, 27)
        self._label9.TabIndex = 10
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ButtonFace
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 430)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(131, 28)
        self._button1.TabIndex = 11
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ButtonFace
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(256, 430)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(131, 28)
        self._button2.TabIndex = 12
        self._button2.Text = "Close"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # Form1
        # 
        self.BackColor = System.Drawing.SystemColors.AppWorkspace
        self.ClientSize = System.Drawing.Size(399, 470)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._groupBox1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "Form1"
        self.Text = "Form1"
        self.Load += self.Form1Load
        self._groupBox1.ResumeLayout(False)
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label2Click(self, sender, e):
        pass

    def Label3Click(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        self.Myparent.Show()
        self.Close()

    def Form1Load(self, sender, e):
        pass

    def TextBox1TextChanged(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        tickets = (int(self._textBox1.Text))
        price = 0

        if self._radioButton1.Checked == True:
            price = 50
        if self._radioButton2.Checked == True:
            price = 30
        if self._radioButton3.Checked == True:
            price = 20
        wotax = tickets * price
        tax = wotax * 1.06 - wotax
        total = wotax * 1.06
        self._label7.Text = str(wotax)
        self._label8.Text = str(tax)
        self._label9.Text = str(total)

    def RadioButton1CheckedChanged(self, sender, e):
        pass