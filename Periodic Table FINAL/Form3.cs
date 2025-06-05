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
    public partial class Form3 : Form
    {
 

        public Form3(AtomicElement element)
        {
            InitializeComponent();
            label2.Text = element.Symbol;
            label1.Text = element.Number.ToString();
            label3.Text = element.Name;
            label4.Text = element.Weight.ToString();
            label5.Text = element.ElectronConfig.ToString();
            //Form3.DefaultBackColor = element.GroupColor;
            //label1.BackColor = element.GroupColor;
            label2.BackColor = element.GroupColor;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            var Form1 = new Form1();
            Form1.Show();
            this.Hide();
        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }
    }
}
