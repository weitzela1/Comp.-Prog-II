﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form2(Form):
    def __init__(self, parent):
        self.MyParent = parent
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.AppWorkspace
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(285, 411)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(133, 31)
        self._button1.TabIndex = 0
        self._button1.Text = "RETURN"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(273, 44)
        self._label1.TabIndex = 1
        self._label1.Text = "The university also offers the following meal plans:"
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.SystemColors.Control
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(12, 56)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(273, 26)
        self._radioButton1.TabIndex = 2
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "7 meals per weak:  $560 per semster"
        self._radioButton1.UseVisualStyleBackColor = False
        self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.SystemColors.Control
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(12, 88)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(273, 26)
        self._radioButton2.TabIndex = 3
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "14 meals per weak:  $1095 per semster"
        self._radioButton2.UseVisualStyleBackColor = False
        self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.SystemColors.Control
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(12, 120)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(273, 26)
        self._radioButton3.TabIndex = 4
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Unlimited Meals: $1500 per semester"
        self._radioButton3.UseVisualStyleBackColor = False
        self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
        # 
        # Form2
        # 
        self.BackColor = System.Drawing.SystemColors.ControlLight
        self.ClientSize = System.Drawing.Size(430, 454)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button1)
        self.Name = "Form2"
        self.Text = "Form2"
        self.Load += self.Form2Load
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self.MyParent.Show()
        self.Hide()

             

    def Form2Load(self, sender, e):
        pass

    def RadioButton1CheckedChanged(self, sender, e):
        self.MyParent.MealOption = 1

    def RadioButton2CheckedChanged(self, sender, e):
        self.MyParent.MealOption = 2

    def RadioButton3CheckedChanged(self, sender, e):
        self.MyParent.MealOption = 3