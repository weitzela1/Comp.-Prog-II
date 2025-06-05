using System;
namespace Periodic_Table_FINAL
{
	public class AtomicElement
	{
		public string Name;
		public int Number;
		public string Symbol;
		public double Weight;
		public string Electronegativity;
		public string State;
		public string ElectronConfig;
		public Color GroupColor;

		public AtomicElement(string name, int number, string symbol, double weight, string electronegativity, string state, string electronconfig, Color color)
		{
			Name = name;
			Number = number;
			Symbol = symbol;
			Weight = weight;
			Electronegativity = electronegativity;
			State = state;
			ElectronConfig = electronconfig;
			GroupColor = color;
		}
	}
}