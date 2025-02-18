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
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._radioButton6 = System.Windows.Forms.RadioButton()
        self._radioButton7 = System.Windows.Forms.RadioButton()
        self._radioButton8 = System.Windows.Forms.RadioButton()
        self._groupBox3 = System.Windows.Forms.GroupBox()
        self._radioButton9 = System.Windows.Forms.RadioButton()
        self._radioButton10 = System.Windows.Forms.RadioButton()
        self._radioButton11 = System.Windows.Forms.RadioButton()
        self._radioButton12 = System.Windows.Forms.RadioButton()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._checkBox3 = System.Windows.Forms.CheckBox()
        self._checkBox4 = System.Windows.Forms.CheckBox()
        self._checkBox5 = System.Windows.Forms.CheckBox()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._groupBox1.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self._groupBox3.SuspendLayout()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.CadetBlue
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(139, 28)
        self._label1.TabIndex = 0
        self._label1.Text = "Decks:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.CadetBlue
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 179)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(139, 28)
        self._label2.TabIndex = 1
        self._label2.Text = "Wheel Sets:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.CadetBlue
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(269, 9)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(139, 28)
        self._label3.TabIndex = 2
        self._label3.Text = "Truck Assemblies:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.CadetBlue
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(269, 179)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(139, 28)
        self._label4.TabIndex = 3
        self._label4.Text = "Additional/Misc:"
        # 
        # radioButton1
        # 
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.ForeColor = System.Drawing.Color.White
        self._radioButton1.Location = System.Drawing.Point(6, 27)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(139, 24)
        self._radioButton1.TabIndex = 4
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "The Master Thrasher"
        self._radioButton1.UseVisualStyleBackColor = True
        self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
        # 
        # radioButton2
        # 
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.ForeColor = System.Drawing.Color.White
        self._radioButton2.Location = System.Drawing.Point(6, 57)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(139, 24)
        self._radioButton2.TabIndex = 5
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "The Dictator of Grind"
        self._radioButton2.UseVisualStyleBackColor = True
        # 
        # radioButton3
        # 
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.ForeColor = System.Drawing.Color.White
        self._radioButton3.Location = System.Drawing.Point(6, 87)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(139, 24)
        self._radioButton3.TabIndex = 6
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "The Street King"
        self._radioButton3.UseVisualStyleBackColor = True
        # 
        # groupBox1
        # 
        self._groupBox1.Controls.Add(self._radioButton1)
        self._groupBox1.Controls.Add(self._radioButton2)
        self._groupBox1.Controls.Add(self._radioButton3)
        self._groupBox1.Location = System.Drawing.Point(12, 49)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(200, 117)
        self._groupBox1.TabIndex = 9
        self._groupBox1.TabStop = False
        # 
        # groupBox2
        # 
        self._groupBox2.Controls.Add(self._radioButton6)
        self._groupBox2.Controls.Add(self._radioButton7)
        self._groupBox2.Controls.Add(self._radioButton8)
        self._groupBox2.Location = System.Drawing.Point(269, 49)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.Size = System.Drawing.Size(200, 117)
        self._groupBox2.TabIndex = 10
        self._groupBox2.TabStop = False
        # 
        # radioButton6
        # 
        self._radioButton6.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton6.ForeColor = System.Drawing.Color.White
        self._radioButton6.Location = System.Drawing.Point(6, 27)
        self._radioButton6.Name = "radioButton6"
        self._radioButton6.Size = System.Drawing.Size(139, 24)
        self._radioButton6.TabIndex = 4
        self._radioButton6.TabStop = True
        self._radioButton6.Text = "7.75 Axle"
        self._radioButton6.UseVisualStyleBackColor = True
        # 
        # radioButton7
        # 
        self._radioButton7.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton7.ForeColor = System.Drawing.Color.White
        self._radioButton7.Location = System.Drawing.Point(6, 57)
        self._radioButton7.Name = "radioButton7"
        self._radioButton7.Size = System.Drawing.Size(139, 24)
        self._radioButton7.TabIndex = 5
        self._radioButton7.TabStop = True
        self._radioButton7.Text = "8 Axle"
        self._radioButton7.UseVisualStyleBackColor = True
        # 
        # radioButton8
        # 
        self._radioButton8.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton8.ForeColor = System.Drawing.Color.White
        self._radioButton8.Location = System.Drawing.Point(6, 87)
        self._radioButton8.Name = "radioButton8"
        self._radioButton8.Size = System.Drawing.Size(139, 24)
        self._radioButton8.TabIndex = 6
        self._radioButton8.TabStop = True
        self._radioButton8.Text = "8.5 Axle"
        self._radioButton8.UseVisualStyleBackColor = True
        # 
        # groupBox3
        # 
        self._groupBox3.Controls.Add(self._radioButton12)
        self._groupBox3.Controls.Add(self._radioButton9)
        self._groupBox3.Controls.Add(self._radioButton10)
        self._groupBox3.Controls.Add(self._radioButton11)
        self._groupBox3.Location = System.Drawing.Point(12, 221)
        self._groupBox3.Name = "groupBox3"
        self._groupBox3.Size = System.Drawing.Size(200, 146)
        self._groupBox3.TabIndex = 11
        self._groupBox3.TabStop = False
        # 
        # radioButton9
        # 
        self._radioButton9.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton9.ForeColor = System.Drawing.Color.White
        self._radioButton9.Location = System.Drawing.Point(6, 27)
        self._radioButton9.Name = "radioButton9"
        self._radioButton9.Size = System.Drawing.Size(139, 24)
        self._radioButton9.TabIndex = 4
        self._radioButton9.TabStop = True
        self._radioButton9.Text = "51mm"
        self._radioButton9.UseVisualStyleBackColor = True
        # 
        # radioButton10
        # 
        self._radioButton10.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton10.ForeColor = System.Drawing.Color.White
        self._radioButton10.Location = System.Drawing.Point(6, 57)
        self._radioButton10.Name = "radioButton10"
        self._radioButton10.Size = System.Drawing.Size(139, 24)
        self._radioButton10.TabIndex = 5
        self._radioButton10.TabStop = True
        self._radioButton10.Text = "55mm"
        self._radioButton10.UseVisualStyleBackColor = True
        # 
        # radioButton11
        # 
        self._radioButton11.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton11.ForeColor = System.Drawing.Color.White
        self._radioButton11.Location = System.Drawing.Point(6, 87)
        self._radioButton11.Name = "radioButton11"
        self._radioButton11.Size = System.Drawing.Size(139, 24)
        self._radioButton11.TabIndex = 6
        self._radioButton11.TabStop = True
        self._radioButton11.Text = "58mm"
        self._radioButton11.UseVisualStyleBackColor = True
        # 
        # radioButton12
        # 
        self._radioButton12.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton12.ForeColor = System.Drawing.Color.White
        self._radioButton12.Location = System.Drawing.Point(6, 116)
        self._radioButton12.Name = "radioButton12"
        self._radioButton12.Size = System.Drawing.Size(139, 24)
        self._radioButton12.TabIndex = 7
        self._radioButton12.TabStop = True
        self._radioButton12.Text = "61mm"
        self._radioButton12.UseVisualStyleBackColor = True
        # 
        # checkBox1
        # 
        self._checkBox1.BackColor = System.Drawing.Color.CadetBlue
        self._checkBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._checkBox1.Location = System.Drawing.Point(269, 231)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(193, 22)
        self._checkBox1.TabIndex = 12
        self._checkBox1.Text = "Grip Tape"
        self._checkBox1.UseVisualStyleBackColor = False
        # 
        # checkBox2
        # 
        self._checkBox2.BackColor = System.Drawing.Color.CadetBlue
        self._checkBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._checkBox2.Location = System.Drawing.Point(269, 259)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(193, 22)
        self._checkBox2.TabIndex = 13
        self._checkBox2.Text = "Bearings"
        self._checkBox2.UseVisualStyleBackColor = False
        # 
        # checkBox3
        # 
        self._checkBox3.BackColor = System.Drawing.Color.CadetBlue
        self._checkBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._checkBox3.Location = System.Drawing.Point(269, 287)
        self._checkBox3.Name = "checkBox3"
        self._checkBox3.Size = System.Drawing.Size(193, 22)
        self._checkBox3.TabIndex = 14
        self._checkBox3.Text = "Riser Pads"
        self._checkBox3.UseVisualStyleBackColor = False
        # 
        # checkBox4
        # 
        self._checkBox4.BackColor = System.Drawing.Color.CadetBlue
        self._checkBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox4.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._checkBox4.Location = System.Drawing.Point(269, 315)
        self._checkBox4.Name = "checkBox4"
        self._checkBox4.Size = System.Drawing.Size(193, 22)
        self._checkBox4.TabIndex = 15
        self._checkBox4.Text = "Nuts & Bots Kit"
        self._checkBox4.UseVisualStyleBackColor = False
        # 
        # checkBox5
        # 
        self._checkBox5.BackColor = System.Drawing.Color.CadetBlue
        self._checkBox5.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox5.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._checkBox5.Location = System.Drawing.Point(269, 345)
        self._checkBox5.Name = "checkBox5"
        self._checkBox5.Size = System.Drawing.Size(193, 22)
        self._checkBox5.TabIndex = 16
        self._checkBox5.Text = "Assembly"
        self._checkBox5.UseVisualStyleBackColor = False
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.LightCyan
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(12, 384)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(200, 29)
        self._label5.TabIndex = 17
        self._label5.Text = "Total:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.LightCyan
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(269, 384)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(200, 29)
        self._label6.TabIndex = 18
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label6.Click += self.Label6Click
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.PowderBlue
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(10, 441)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(147, 64)
        self._button1.TabIndex = 19
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.PowderBlue
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(191, 441)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(147, 64)
        self._button2.TabIndex = 20
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.PowderBlue
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(370, 441)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(147, 64)
        self._button3.TabIndex = 21
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkSlateGray
        self.ClientSize = System.Drawing.Size(529, 517)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._checkBox5)
        self.Controls.Add(self._checkBox4)
        self.Controls.Add(self._checkBox3)
        self.Controls.Add(self._checkBox2)
        self.Controls.Add(self._checkBox1)
        self.Controls.Add(self._groupBox3)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._groupBox1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg485Skateboard"
        self.Load += self.MainFormLoad
        self._groupBox1.ResumeLayout(False)
        self._groupBox2.ResumeLayout(False)
        self._groupBox3.ResumeLayout(False)
        self.ResumeLayout(False)


    def MainFormLoad(self, sender, e):
        pass
            
            

        
        

    def Button1Click(self, sender, e):
        deck = 1
        assem = 1
        wheel = 1

        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        
        if self._radioButton1.Checked == True:
            deck = 60
            
        if self._radioButton2.Checked == True:
            deck = 45
            
        if self._radioButton3.Checked == True:
            deck = 50
        
        if self._radioButton6.Checked == True:
            assem = 35
        
        if self._radioButton7.Checked == True:
            assem = 40
           
        if self._radioButton8.Checked == True:
            assem = 45
            
        if self._radioButton9.Checked == True:
            wheel = 20
            
        if self._radioButton10.Checked == True:
            wheel = 22
            
        if self._radioButton11.Checked == True:
            wheel = 24
            
        if self._radioButton12.Checked == True:
            wheel = 28
            
        if self._checkBox1.Checked == True:
            a = 10
        if self._checkBox2.Checked == True:
            b = 30
        if self._checkBox3.Checked == True:
            c = 2
        if self._checkBox4.Checked == True:
            d = 3
        if self._checkBox5.Checked == True:
            e = 10
        
        


        
        total = deck + assem + wheel + a + b + c + d + e

        self._label6.Text = str(total)

    def Button2Click(self, sender, e):
        self._label6.Text = ""
        

    def Button3Click(self, sender, e):
        Application.Exit()

    def RadioButton1CheckedChanged(self, sender, e):
        pass

    def Label6Click(self, sender, e):
        pass