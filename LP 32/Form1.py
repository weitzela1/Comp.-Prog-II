﻿
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self.SuspendLayout()
        # 
        # Form1
        # 
        self.ClientSize = System.Drawing.Size(440, 455)
        self.Name = "Form1"
        self.Text = "Form1"
        self.ResumeLayout(False)

