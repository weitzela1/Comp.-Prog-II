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
    public partial class Form2 : Form
    {
        AtomicElement MyElement;
        public Form2(AtomicElement element)
        {
            InitializeComponent();
            label1.Text = element.Name;
            label1.BackColor = element.GroupColor;
            label7.Text = element.Number.ToString();
            label8.Text = element.Symbol;
            label9.Text = element.Weight.ToString();
            label10.Text = element.Electronegativity;
            label11.Text = element.State;
            label13.Text = element.ElectronConfig;
            MyElement = element;
            //label2.Text = element.Weight;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            var Form1 = new Form1();
            Form1.Show();
            this.Hide();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label7_Click(object sender, EventArgs e)
        {

        }

        private void label12_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            // switch to form 3
            Form3 frm3 = new Form3(MyElement);
            frm3.Show();
            this.Hide();
        }
    }
}
