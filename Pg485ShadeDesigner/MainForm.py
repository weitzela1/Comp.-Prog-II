import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button2 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._radioButton4 = System.Windows.Forms.RadioButton()
        self._radioButton5 = System.Windows.Forms.RadioButton()
        self._radioButton6 = System.Windows.Forms.RadioButton()
        self._radioButton7 = System.Windows.Forms.RadioButton()
        self._groupBox3 = System.Windows.Forms.GroupBox()
        self._radioButton8 = System.Windows.Forms.RadioButton()
        self._radioButton9 = System.Windows.Forms.RadioButton()
        self._radioButton10 = System.Windows.Forms.RadioButton()
        self._radioButton11 = System.Windows.Forms.RadioButton()
        self._radioButton12 = System.Windows.Forms.RadioButton()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._groupBox1.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self._groupBox3.SuspendLayout()
        self.SuspendLayout()
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.DarkSeaGreen
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(247, 400)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(167, 100)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.MediumSeaGreen
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(146, 31)
        self._label1.TabIndex = 3
        self._label1.Text = "Styles"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.Color.SeaGreen
        self._groupBox1.Controls.Add(self._radioButton3)
        self._groupBox1.Controls.Add(self._radioButton2)
        self._groupBox1.Controls.Add(self._radioButton1)
        self._groupBox1.Location = System.Drawing.Point(12, 53)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(145, 144)
        self._groupBox1.TabIndex = 4
        self._groupBox1.TabStop = False
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.MediumSeaGreen
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(247, 9)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(146, 31)
        self._label2.TabIndex = 5
        self._label2.Text = "Sizes"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.MediumSeaGreen
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(491, 9)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(146, 31)
        self._label3.TabIndex = 6
        self._label3.Text = "Colors"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # radioButton1
        # 
        self._radioButton1.Location = System.Drawing.Point(6, 18)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(138, 18)
        self._radioButton1.TabIndex = 0
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Regular Shades"
        self._radioButton1.UseVisualStyleBackColor = True
        # 
        # radioButton2
        # 
        self._radioButton2.Location = System.Drawing.Point(6, 42)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(138, 18)
        self._radioButton2.TabIndex = 1
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Folding Shades"
        self._radioButton2.UseVisualStyleBackColor = True
        # 
        # radioButton3
        # 
        self._radioButton3.Location = System.Drawing.Point(6, 66)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(138, 18)
        self._radioButton3.TabIndex = 2
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Roman Shades"
        self._radioButton3.UseVisualStyleBackColor = True
        # 
        # groupBox2
        # 
        self._groupBox2.BackColor = System.Drawing.Color.SeaGreen
        self._groupBox2.Controls.Add(self._radioButton7)
        self._groupBox2.Controls.Add(self._radioButton4)
        self._groupBox2.Controls.Add(self._radioButton5)
        self._groupBox2.Controls.Add(self._radioButton6)
        self._groupBox2.Location = System.Drawing.Point(247, 53)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.Size = System.Drawing.Size(145, 144)
        self._groupBox2.TabIndex = 5
        self._groupBox2.TabStop = False
        # 
        # radioButton4
        # 
        self._radioButton4.Location = System.Drawing.Point(6, 66)
        self._radioButton4.Name = "radioButton4"
        self._radioButton4.Size = System.Drawing.Size(138, 18)
        self._radioButton4.TabIndex = 2
        self._radioButton4.TabStop = True
        self._radioButton4.Text = "32 inches wide"
        self._radioButton4.UseVisualStyleBackColor = True
        # 
        # radioButton5
        # 
        self._radioButton5.Location = System.Drawing.Point(6, 42)
        self._radioButton5.Name = "radioButton5"
        self._radioButton5.Size = System.Drawing.Size(138, 18)
        self._radioButton5.TabIndex = 1
        self._radioButton5.TabStop = True
        self._radioButton5.Text = "27 inches wide"
        self._radioButton5.UseVisualStyleBackColor = True
        # 
        # radioButton6
        # 
        self._radioButton6.Location = System.Drawing.Point(6, 18)
        self._radioButton6.Name = "radioButton6"
        self._radioButton6.Size = System.Drawing.Size(138, 18)
        self._radioButton6.TabIndex = 0
        self._radioButton6.TabStop = True
        self._radioButton6.Text = "25 inches wide"
        self._radioButton6.UseVisualStyleBackColor = True
        # 
        # radioButton7
        # 
        self._radioButton7.Location = System.Drawing.Point(6, 90)
        self._radioButton7.Name = "radioButton7"
        self._radioButton7.Size = System.Drawing.Size(138, 18)
        self._radioButton7.TabIndex = 3
        self._radioButton7.TabStop = True
        self._radioButton7.Text = "40 inches wide"
        self._radioButton7.UseVisualStyleBackColor = True
        # 
        # groupBox3
        # 
        self._groupBox3.BackColor = System.Drawing.Color.SeaGreen
        self._groupBox3.Controls.Add(self._radioButton12)
        self._groupBox3.Controls.Add(self._radioButton8)
        self._groupBox3.Controls.Add(self._radioButton9)
        self._groupBox3.Controls.Add(self._radioButton10)
        self._groupBox3.Controls.Add(self._radioButton11)
        self._groupBox3.Location = System.Drawing.Point(491, 53)
        self._groupBox3.Name = "groupBox3"
        self._groupBox3.Size = System.Drawing.Size(145, 144)
        self._groupBox3.TabIndex = 6
        self._groupBox3.TabStop = False
        # 
        # radioButton8
        # 
        self._radioButton8.Location = System.Drawing.Point(6, 90)
        self._radioButton8.Name = "radioButton8"
        self._radioButton8.Size = System.Drawing.Size(138, 18)
        self._radioButton8.TabIndex = 3
        self._radioButton8.TabStop = True
        self._radioButton8.Text = "Red"
        self._radioButton8.UseVisualStyleBackColor = True
        # 
        # radioButton9
        # 
        self._radioButton9.Location = System.Drawing.Point(6, 66)
        self._radioButton9.Name = "radioButton9"
        self._radioButton9.Size = System.Drawing.Size(138, 18)
        self._radioButton9.TabIndex = 2
        self._radioButton9.TabStop = True
        self._radioButton9.Text = "Teal"
        self._radioButton9.UseVisualStyleBackColor = True
        # 
        # radioButton10
        # 
        self._radioButton10.Location = System.Drawing.Point(6, 42)
        self._radioButton10.Name = "radioButton10"
        self._radioButton10.Size = System.Drawing.Size(138, 18)
        self._radioButton10.TabIndex = 1
        self._radioButton10.TabStop = True
        self._radioButton10.Text = "Blue"
        self._radioButton10.UseVisualStyleBackColor = True
        # 
        # radioButton11
        # 
        self._radioButton11.Location = System.Drawing.Point(6, 18)
        self._radioButton11.Name = "radioButton11"
        self._radioButton11.Size = System.Drawing.Size(138, 18)
        self._radioButton11.TabIndex = 0
        self._radioButton11.TabStop = True
        self._radioButton11.Text = "Natural"
        self._radioButton11.UseVisualStyleBackColor = True
        # 
        # radioButton12
        # 
        self._radioButton12.Location = System.Drawing.Point(6, 114)
        self._radioButton12.Name = "radioButton12"
        self._radioButton12.Size = System.Drawing.Size(138, 18)
        self._radioButton12.TabIndex = 4
        self._radioButton12.TabStop = True
        self._radioButton12.Text = "Green"
        self._radioButton12.UseVisualStyleBackColor = True
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.MediumSeaGreen
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 208)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(625, 52)
        self._label4.TabIndex = 7
        self._label4.Text = "PLEASE BE AWARE THAT THERE IS A 50 DOLLAR BASE FEE"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.MediumSeaGreen
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(12, 282)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(378, 52)
        self._label5.TabIndex = 8
        self._label5.Text = "Total:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.LimeGreen
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(396, 282)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(247, 52)
        self._label6.TabIndex = 9
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.DarkSeaGreen
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(18, 400)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(167, 100)
        self._button1.TabIndex = 10
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DarkSeaGreen
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(476, 400)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(167, 100)
        self._button3.TabIndex = 11
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.ForestGreen
        self.ClientSize = System.Drawing.Size(655, 512)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._groupBox3)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._groupBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button2)
        self.Name = "MainForm"
        self.Text = "Pg485ShadeDesigner"
        self._groupBox1.ResumeLayout(False)
        self._groupBox2.ResumeLayout(False)
        self._groupBox3.ResumeLayout(False)
        self.ResumeLayout(False)


    def ComboBox1SelectedIndexChanged(self, sender, e):
        Style = 0
        Size = 0
        Color = 0
        if self._radioButton1.Checked == True:
            Style = 0
        if self._radioButton2.Checked == True:
            Style = 10
        if self._radioButton3.Checked == True:
            Style = 15
        if self._radioButton6.Checked == True:
            Size = 0
        if self._radioButton5.Checked == True:
            Size = 2
        if self._radioButton4.Checked == True:
            Size = 4
        if self._radioButton7.Checked == True:
            Size = 6
        if self._radioButton11.Checked == True:
            Color = 5
        else:
            Color = 0
            
            
            
        total = 50 + Style + Size + Color
        self._label6.Text = str(total)
        
        

    def Button1Click(self, sender, e):
        Style = 0
        Size = 0
        Color = 0
        if self._radioButton1.Checked == True:
            Style = 0
        if self._radioButton2.Checked == True:
            Style = 10
        if self._radioButton3.Checked == True:
            Style = 15
        if self._radioButton6.Checked == True:
            Size = 0
        if self._radioButton5.Checked == True:
            Size = 2
        if self._radioButton4.Checked == True:
            Size = 4
        if self._radioButton7.Checked == True:
            Size = 6
        if self._radioButton11.Checked == True:
            Color = 5
        else:
            Color = 0
            
            
            
        total = 50 + Style + Size + Color
        self._label6.Text = str(total)
 

    def Button2Click(self, sender, e):
        self._label6.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()