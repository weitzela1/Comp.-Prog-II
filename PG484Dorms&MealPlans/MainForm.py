import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        self.DormOption = 0
        self.MealOption = 0
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.AppWorkspace
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(329, 55)
        self._label1.TabIndex = 0
        self._label1.Text = "Click for dorm info:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.AppWorkspace
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 75)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(329, 55)
        self._label2.TabIndex = 1
        self._label2.Text = "Click for meal plan info:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(347, 9)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(221, 55)
        self._button1.TabIndex = 2
        self._button1.Text = "Dorm"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(347, 78)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(221, 55)
        self._button2.TabIndex = 3
        self._button2.Text = "Meal Plan"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ScrollBar
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 221)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(329, 51)
        self._label3.TabIndex = 4
        self._label3.Text = "Total Price for both meal plan and dorm:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(347, 221)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(221, 51)
        self._label4.TabIndex = 5
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.AppWorkspace
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(418, 398)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(150, 34)
        self._button3.TabIndex = 6
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.BackColor = System.Drawing.SystemColors.AppWorkspace
        self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(12, 398)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(150, 34)
        self._button4.TabIndex = 7
        self._button4.Text = "Calculate"
        self._button4.UseVisualStyleBackColor = False
        self._button4.Click += self.Button4Click
        # 
        # button5
        # 
        self._button5.BackColor = System.Drawing.SystemColors.AppWorkspace
        self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.Location = System.Drawing.Point(221, 398)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(150, 34)
        self._button5.TabIndex = 8
        self._button5.Text = "Clear"
        self._button5.UseVisualStyleBackColor = False
        self._button5.Click += self.Button5Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ControlLight
        self.ClientSize = System.Drawing.Size(580, 444)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "PG484Dorms&MealPlans"
        self.ResumeLayout(False)
        

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        from Form1 import *
        form1 = Form1(self)
        form1.Show()
        self.Hide()

    def Button2Click(self, sender, e):
        from Form2 import *
        form2 = Form2(self)
        form2.Show()
        self.Hide()

    def Button5Click(self, sender, e):

        self._label4.Text = ""

    def Button4Click(self, sender, e):
        dorm = 0
        if self.DormOption == 1:
            dorm = 1500
        if self.DormOption == 2:
            dorm = 1600
        if self.DormOption == 3:
            dorm = 1200
        if self.DormOption == 4:
            dorm = 1800
        if self.MealOption == 1:
            meal = 560
        if self.MealOption == 2:
            meal = 1095
        if self.MealOption == 3:
            meal = 1500
            
        total = dorm + meal
            
        self._label4.Text = str(total)