namespace Periodic_Table_FINAL
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Hydrogen", 1, "H", 1.008, "2.2", "Gas", "1s", button1.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Lithium", 3, "Li", 6.938, ".98", "Solid", "1s^2, 2s", button2.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button19_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Beryllium", 4, "Be", 9.012, "1.57", "Solid", "1s^2, 2s^2", button19.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button54_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Aluminum", 13, "Al", 26.98, "1.61", "Solid", "[Ne] 3s^2, 3p", button54.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button86_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Krypton", 36, "Kr", 83.80, "---", "Gas", "[Ar] 3d^10, 4s^2, 4p^6", button86.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button90_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Helium", 2, "He", 4.003, "---", "Gas", "1s^2", button90.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button60_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Carbon", 6, "C", 12.01, "2.55", "Solid", "1s^2, 2s^2, 2p^2", button60.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button55_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Boron", 5, "B", 10.81, "2.04", "Solid", "1s^2, 2s^2, 2p", button55.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button66_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Nitrogen", 7, "N", 14.01, "3.04", "Gas", "1s^2, 2s^2, 2p^3", button66.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button72_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Oxygen", 8, "O", 16.00, "3.44", "Gas", "1s^2, 2s^2, 2p^4", button72.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button78_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Fluorine", 9, "F", 19.00, "3.98", "Gas", "1s^2, 2s^2, 2p^5", button78.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button84_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Neon", 10, "Ne", 20.18, "---", "Gas", "1s^2, 2s^2, 2p^6", button84.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button119_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Sodium", 11, "Na", 23.00, "0.93", "Solid", "[Ne] 3s", button3.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Magnesium", 12, "Mg", 24.31, "1.31", "Solid", "[Ne] 3s^2", button7.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button61_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Silicon", 14, "Si", 28.01, "1.9", "Solid", "[Ne] 3s^2, 3p^2", button61.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button67_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Phosphorus", 15, "P", 30.97, "2.19", "Solid", "[Ne] 3s^2, 3p^3", button67.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button73_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Sulfur", 16, "S", 32.06, "2.58", "Solid", "[Ne] 3s^2, 3p^4", button73.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button79_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Chlorine", 17, "Cl", 35.45, "3.16", "Gas", "[Ne] 3s^2, 3p^5", button79.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button85_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Argon", 18, "Ar", 39.95, "---", "Gas", "[Ne] 3s^2, 3p^6", button85.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Potassium", 19, "K", 39.10, "0.82", "Solid", "[Ar] 4s", button4.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Calcium", 20, "Ca", 40.08, "1.00", "Solid", "[Ar] 4s^2", button8.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button12_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Scandium", 21, "Sc", 44.96, "1.36", "Solid", "[Ar] 3d, 4s^2", button12.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button16_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Titanium", 22, "Ti", 47.87, "1.54", "Solid", "[Ar] 3d^2, 4s^2", button16.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button22_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Vanadium", 23, "V", 50.94, "1.63", "Solid", "[Ar] 3d^3, 4s^2", button22.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button26_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Chromium", 24, "Cr", 52.00, "1.66", "Solid", "[Ar] 3d^5, 4s", button26.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button30_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Manganese", 25, "Mn", 54.94, "1.55", "Solid", "[Ar] 3d^5, 4s^32", button30.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button34_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Iron", 26, "Fe", 55.85, "1.83", "Solid", "[Ar] 3d^6, 4s^2", button34.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button38_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Cobalt", 27, "Co", 58.93, "1.88", "Solid", "[Ar] 3d^7, 4s^2", button38.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button42_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Nickel", 28, "Ni", 58.69, "1.91", "Solid", "[Ar] 3d^8, 4s^2", button42.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button46_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Copper", 29, "Cu", 63.55, "1.90", "Solid", "[Ar] 3d^10, 4s", button46.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button50_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Zinc", 30, "Zn", 65.38, "1.65", "Solid", "[Ar] 3d^10, 4s^2", button50.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button56_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Gallium", 31, "Ga", 69.72, "1.81", "Solid", "[Ar] 3d^10, 4s^2, 4p", button56.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button62_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Germanium", 32, "Ge", 72.63, "2.01", "Solid", "[Ar] 3d^10, 4s^2, 4p^2", button62.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button68_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Arsenic", 33, "As", 74.92, "2.18", "Solid", "[Ar] 3d^10, 4s^2, 4p^3", button68.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button74_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Selenium", 34, "Se", 78.96, "2.55", "Solid", "[Ar] 3d^10, 4s^2, 4p^4", button74.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button80_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Bromine", 35, "Br", 79.90, "2.96", "Liquid", "[Ar] 3d^10, 4s^2, 4p^5", button80.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Rubidium", 37, "Rb", 85.47, "0.82", "Solid", "[Kr] 5s", button5.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Stronium", 38, "Sr", 87.62, ".95", "Solid", "[Kr] 5s^2", button9.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button13_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Yttrium", 39, "Y", 88.91, "1.22", "Solid", "[Kr] 4d, 5s^2", button13.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button17_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Zirconium", 40, "Zr", 91.22, "1.33", "Solid", "[Kr] 4d^2, 5s^2", button17.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button23_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Niobium", 41, "Nb", 92.91, "1.60", "Solid", "[Kr] 4d^4, 5s", button23.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button27_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Molybdenum", 42, "Mo", 95.96, "2.16", "Solid", "[Kr] 4d^5, 5s", button27.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button31_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Technetium", 43, "Tc", 98.00, "2.10", "Solid", "[Kr] 4d^5, 5s^2", button31.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button35_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Ruthenium", 44, "Ru", 101.1, "2.20", "Solid", "[Kr] 4d^7, 5s", button35.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button39_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Rhodium", 45, "Rh", 102.9, "2.28", "Solid", "[Kr] 4d^8, 5s", button39.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button43_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Palladium", 46, "Pd", 106.4, "2.20", "Solid", "[Kr] 4d^10", button43.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button47_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Silver", 47, "Ag", 107.9, "1.93", "Solid", "[Kr] 4d^10, 5s", button47.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button51_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Cadmium", 48, "Cd", 112.4, "1.69", "Solid", "[Kr] 4d^10, 5s^2", button51.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button57_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Indium", 49, "In", 114.8, "1.78", "Solid", "[Kr] 4d^10, 5s^2, 5p", button57.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button63_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Tin", 50, "Sn", 118.7, "1.96", "Solid", "[Kr] 4d^10, 5s^2, 5p^2", button63.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button69_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Antimony", 51, "Sb", 121.8, "2.05", "Solid", "[Kr] 4d^10, 5s^2, 5p^3", button69.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button75_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Tellurium", 52, "Te", 127.6, "2.10", "Solid", "[Kr] 4d^10, 5s^2, 5p^4", button75.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button81_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Iodine", 53, "I", 126.9, "2.66", "Solid", "[Kr] 4d^10, 5s^2, 5p^5", button81.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button87_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Xenon", 54, "Xe", 131.3, "2.10", "Gas", "[Kr] 4d^10, 5s^2, 5p^6", button87.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Caesium", 55, "Cs", 132.9,"0.79", "Solid","[Xe] 6s", button6.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button10_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Barium", 56, "Ba", 137.3, "0.89", "Solid", "[Xe] 6s^2", button10.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button14_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Lanthanum", 57, "La", 138.9, "1.10", "Solid", "[Xe] 5d, 6s^2", button14.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button91_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Cerium", 58, "Ce", 140.1, "1.12", "Solid", "[Xe] 4f, 5d, 6s^2", button91.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button93_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Praseodymium", 59, "Pr", 140.9, "1.13", "Solid", "[Xe] 4f^3, 6s^2", button93.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button95_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Neodymium", 60, "Nd", 144.2, "1.14", "Solid", "[Xe] 4f^4, 6s^2", button95.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button97_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Promethium", 61, "Pm", 145.0, "---", "Solid", "[Xe] 4f^5, 6s^2", button97.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button99_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Samarium", 62, "Sm", 150.4, "1.17", "Solid", "[Xe] 4f^6, 6s^2", button99.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button101_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Europium", 63, "Eu", 152.0, "--", "Solid", "[Xe] 4f^7, 6s^2", button101.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button103_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Gadolinium", 64, "Gd", 157.3, "1.20", "Solid", "[Xe] 4f^7, 5d, 6s^2", button103.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button105_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Terbium", 65, "Tb", 158.9, "---", "Solid", "[Xe] 4f^9, 6s^2", button105.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button107_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Dyaprosium", 66, "Dy", 162.5, "1.22", "Solid", "[Xe] 4f^10, 6s^2", button107.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button109_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Holium", 67, "Ho", 164.9, "1.23", "Solid", "[Xe] 4f^11, 6s^2", button109.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button111_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Erbium", 68, "Er", 167.3, "1.24", "Solid", "[Xe] 4f^12, 6s^2", button111.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button113_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Thulium", 69, "Tm", 168.9, "1.25", "Solid", "[Xe] 4f^13, 6s^2", button113.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button115_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Ytterbium", 70, "Yb", 173.1, "---", "Solid", "[Xe] 4f^14, 6s^2", button115.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button117_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Lutetium", 71, "Lu", 175.0, "1.00", "Solid", "[Xe] 4f^14, 5d, 6s^2", button117.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button20_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Hafnium", 72, "Hf", 178.5, "1.30", "Solid", "[Xe] 4f^14, 5d^2, 6s^2", button20.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button24_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Tantalum", 73, "Ta", 180.9, "1.50", "Solid", "[Xe] 4f^14, 5d^3, 6s^2", button24.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button28_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Tungsten", 74, "W", 183.9, "1.70", "Solid", "[Xe] 4f^14, 5d^4, 6s^2", button28.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button32_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Rhenium", 75, "Re", 186.2, "1.90", "Solid", "[Xe] 4f^14, 5d^5, 6s^2", button32.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button36_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Osmium", 76, "Os", 190.2, "2.20", "Solid", "[Xe] 4f^14, 5d^6, 6s^2", button36.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button40_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Iridium", 77, "Ir", 192.2, "2.20", "Solid", "[Xe] 4f^14, 5d^7, 6s^2", button40.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button44_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Platinum", 78, "Pt", 195.1, "2.28", "Solid", "[Xe] 4f^14, 5d^9, 6s", button44.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button48_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Gold", 79, "Au", 197.0, "2.40", "Solid", "[Xe] 4f^14, 5d^10, 6s", button48.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button52_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Mercury", 80, "Hg", 200.6, "1.90", "Liquid", "[Xe] 4f^14, 5d^10, 6s^2", button52.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button58_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Thallium", 81, "Tl", 204.4, "1.80", "Solid", "[Xe] 4f^14, 5d^10, 6s^2, 6p", button58.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button64_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Lead", 82, "Pb", 207.2, "1.62", "Solid", "[Xe] 4f^14, 5d^10, 6s^2, 6p^2", button64.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button70_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Bismuth", 83, "Bi", 209.0, "1.80", "Solid", "[Xe] 4f^14, 5d^10, 6s^2, 6p^3", button70.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button76_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Polonium", 84, "Po", 209.0, "2.00", "Solid", "[Xe] 4f^14, 5d^10, 6s^2, 6p^4", button76.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button82_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Astatine", 85, "At", 210.0, "2.20", "Solid", "[Xe] 4f^14, 5d^10, 6s^2, 6p^5", button82.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button88_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Radon", 86, "Rn", 222.0, "---", "Gas", "[Xe] 4f^14, 5d^10, 6s^2, 6p^6", button88.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button18_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Francium", 87, "Fr", 223.0, "0.70", "Solid", "[Rn] 7s", button18.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button11_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Radium", 88, "Ra", 226.0 ,".90", "Solid", "[Rn] 7s^2", button11.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button15_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Actinium", 89, "Ac", 227.0, "1.10", "Solid", "[Rn] 6d, 7s^2", button15.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button92_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Thorium", 90, "Th", 232.0, "1.30", "Solid", "[Rn] 6d^2, 7s^2", button92.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button96_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Uranium", 92, "U", 238.0, "1.70", "Solid", "[Rn] 5f^3, 6d, 7s^2", button96.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button94_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Protactinum", 91, "Pa", 231.0, "1.50", "Solid", "[Rn] 5f^2, 6d, 7s^2,", button20.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button98_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Neptunium", 93, "Np", 237, "1.30", "Solid", "[Rn] 5f^4, 6d, 7s^2,", button98.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button100_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Plutonium", 94, "Pu", 244, "1.30", "Solid", "[Rn] 5f^6, 7s^2,", button100.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button102_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Americium", 95, "Am", 243.0, "---", "Solid", "[Rn] 5f^7, 7s^2,", button102.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button104_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Curium", 96, "Cm", 247.0, "---", "Solid", "[Rn] 5f^7, 6d, 7s^2,", button104.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button106_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Berkelium", 97, "Bk", 247.0, "---", "Solid", "[Rn] 5f^9, 7s^2,", button106.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button108_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Californium", 98, "Cf", 251.0, "---", "Solid", "[Rn] 5f^10, 7s^2,", button108.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button110_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Einsteinium", 99, "Es", 252.0, "---", "Solid", "[Rn] 5f^11, 7s^2,", button110.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button112_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Fermium", 100, "Fm", 257.0, "---", "Solid", "[Rn] 5f^12, 7s^2,", button112.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button114_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Mendelevium", 101, "Md", 258.0, "---", "Solid", "[Rn] 5f^13, 7s^2,", button114.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button116_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Nobelium", 102, "No", 259.0, "---", "Solid", "[Rn] 5f^14, 7s^2,", button116.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button118_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Lawrencium", 103, "Lr", 262.0, "---", "Solid", "[Rn] 5f^14, 7s^2, 7p", button118.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button21_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Rutherfordium", 104, "Rf", 261.0, "---", "Solid", "[Rn] 5f^14, 6d^2, 7s^2,", button21.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button25_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Dubnium", 105, "Db", 262.0, "---", "Solid", "[Rn] 5f^14, 6d^3, 7s^2,", button25.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button29_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Seaborgium", 106, "Sg", 263.0, "---", "Solid", "[Rn] 5f^14, 6d^4, 7s^2,", button29.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button33_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Bohrium", 107, "Bh", 264.0, "---", "Solid", "[Rn] 5f^14, 6d^5, 7s^2,", button33.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button37_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Hassium", 108, "Hs", 265.0, "---", "Solid", "[Rn] 5f^14, 6d^6, 7s^2,", button37.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button41_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Meitnerium", 109, "Mt", 268.0, "---", "Solid", "[Rn] 5f^14, 6d^7, 7s^2,", button41.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button45_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Darmstadtium", 110, "Ds", 281.0, "---", "Solid", "[Rn] 5f^14, 6d^9, 7s^2,", button45.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button49_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Roentgenium", 111, "Rg", 273.0, "---", "Solid", "[Rn] 5f^14, 6d^10, 7s,", button49.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button53_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Copernicium", 112, "Cn", 277.0, "---", "Solid", "[Rn] 5f^14, 6d^10, 7s^2,", button53.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button59_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Nihonium", 113, "Nh", 286.0, "---", "Solid", "[Rn] 5f^14, 6d^10, 7s^2, 7p", button59.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button65_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Flerovium", 114, "Fl", 289.0, "---", "Solid", "[Rn] 5f^14, 6d^10, 7s^2, 7p^2", button65.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button71_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Moscovium", 115, "Mc", 289.0, "---", "Solid", "[Rn] 5f^14, 6d^10, 7s^2, 7p^3", button71.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button77_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Livermorium", 116, "Lv", 293.0, "---", "Solid", "[Rn] 5f^14, 6d^10, 7s^2, 7p^4", button77.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button83_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Tennessine", 117, "Ts", 294.0, "---", "Solid", "[Rn] 5f^14, 6d^10, 7s^2, 7p^5", button83.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button89_Click(object sender, EventArgs e)
        {
            var elem = new AtomicElement("Organesson", 118, "Og", 294.0, "---", "Gas", "[Rn] 5f^14, 6d^10, 7s^2, 7p^6", button89.BackColor);
            var Form2 = new Form2(elem);
            Form2.Show();
            this.Hide();
        }

        private void button120_Click(object sender, EventArgs e)
        {
            var Form4 = new Form4();
            Form4.Show();
            this.Hide();
        }
    }
}