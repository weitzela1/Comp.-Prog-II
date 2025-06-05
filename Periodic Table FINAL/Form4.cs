using Microsoft.VisualBasic;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Periodic_Table_FINAL
{
    public partial class Form4 : Form
    {
        public Form4()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            var Form1 = new Form1();
            Form1.Show();
            this.Hide();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string Speed;
            Speed = Interaction.InputBox("Please enter a number 1-8 that correspons the given slot.");
            if (Speed == "1")
            {
                textBox1.Text = "299792458";
                textBox2.Text = "m";
            }
            else if (Speed == "2")
            {
                textBox5.Text = "299792458";
                textBox7.Text = "m";
            }
            else if (Speed == "3")
            {
                textBox12.Text = "299792458";
                textBox11.Text = "m";

            }
            else if (Speed == "4")
            {
                textBox15.Text = "299792458";
                textBox16.Text = "m";

            }
            else if (Speed == "5")
            {
                textBox3.Text = "299792458";
                textBox4.Text = "m";
            }
            else if (Speed == "6")
            {
                textBox6.Text = "299792458";
                textBox8.Text = "m";

            }
            else if (Speed == "7")
            {
                textBox9.Text = "299792458";
                textBox10.Text = "m";
            }
            else if (Speed == "8")
            {
                textBox13.Text = "299792458";
                textBox14.Text = "m";
            }

            //private void button2_Click(object sender, EventArgs e)
            {

            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string Avo;
            Avo = Interaction.InputBox("Please enter a number 1-8 that correspons the given slot.");
            if (Avo == "1")
            {
                textBox1.Text = "602200000000000000000000";
                textBox2.Text = "";
            }
            else if (Avo == "2")
            {
                textBox5.Text = "602200000000000000000000";
                textBox7.Text = "";
            }
            else if (Avo == "3")
            {
                textBox12.Text = "602200000000000000000000";
                textBox11.Text = "";

            }
            else if (Avo == "4")
            {
                textBox15.Text = "602200000000000000000000";
                textBox16.Text = "";

            }
            else if (Avo == "5")
            {
                textBox3.Text = "602200000000000000000000";
                textBox4.Text = "";
            }
            else if (Avo == "")
            {
                textBox6.Text = "602200000000000000000000";
                textBox8.Text = "";

            }
            else if (Avo == "7")
            {
                textBox9.Text = "602200000000000000000000";
                textBox10.Text = "";
            }
            else if (Avo == "8")
            {
                textBox13.Text = "602200000000000000000000";
                textBox14.Text = "";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string Planck;
            Planck = Interaction.InputBox("Please enter a number 1-8 that correspons the given slot.");
            if (Planck == "1")
            {
                textBox1.Text = "0.000000000000000000000000000000000662607";
                textBox2.Text = "J";
            }
            else if (Planck == "2")
            {
                textBox5.Text = "0.000000000000000000000000000000000662607";
                textBox7.Text = "J";
            }
            else if (Planck == "3")
            {
                textBox12.Text = "0.000000000000000000000000000000000662607";
                textBox11.Text = "J";

            }
            else if (Planck == "4")
            {
                textBox15.Text = "0.000000000000000000000000000000000662607";
                textBox16.Text = "J";

            }
            else if (Planck == "5")
            {
                textBox3.Text = "0.000000000000000000000000000000000662607";
                textBox4.Text = "J";
            }
            else if (Planck == "")
            {
                textBox6.Text = "0.000000000000000000000000000000000662607";
                textBox8.Text = "J";

            }
            else if (Planck == "7")
            {
                textBox9.Text = "0.000000000000000000000000000000000662607";
                textBox10.Text = "J";
            }
            else if (Planck == "8")
            {
                textBox13.Text = "0.000000000000000000000000000000000662607";
                textBox14.Text = "J";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            double top1 = double.Parse(textBox1.Text);
            double top2 = double.Parse(textBox5.Text);
            double top3 = double.Parse(textBox12.Text);
            double top4 = double.Parse(textBox15.Text);

            double bottom1 = double.Parse(textBox3.Text);
            double bottom2 = double.Parse(textBox6.Text);
            double bottom3 = double.Parse(textBox9.Text);
            double bottom4 = double.Parse(textBox13.Text);

            {
                MessageBox.Show("Please enter numbers into all boxes! ");
            }
            double totaltop = top1 + top2 + top3 + top4;
            double totalbottom = bottom1 + bottom2 + bottom3 + bottom4;
            double quotient = totaltop / totalbottom;
            label13.Text = quotient.ToString();
            // I purposely chose not to round because of sf, you dont know how it works teacher-teacher
        }

        private void button6_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            textBox2.Text = "";
            textBox3.Text = "";
            textBox4.Text = "";
            textBox5.Text = "";
            textBox6.Text = "";
            textBox7.Text = "";
            textBox8.Text = "";
            textBox9.Text = "";
            textBox10.Text = "";
            textBox11.Text = "";
            textBox12.Text = "";
            textBox13.Text = "";
            textBox14.Text = "";
            textBox15.Text = "";
            textBox16.Text = "";
            label13.Text = "";

        }
    }
}
