// See https://aka.ms/new-console-template for more information
using System;

class Program
{
    static void Main()
    {
        Rectangle r = new Rectangle(1, 2, "красного");
        Circle c = new Circle(1, "зеленого");
        Square s = new Square(2, "синего");
        Console.WriteLine(r);
        Console.WriteLine(c);
        Console.WriteLine(s);
    }
}

