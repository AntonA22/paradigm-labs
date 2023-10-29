using System;

public class Circle : Figure
{
    public static string FigureType = "Круг";
    private double radius;
    private Color Circle_Color;

    public Circle(double r, string color)
    {
        radius = r;
        Circle_Color = new Color(color);
    }

    public override double Area()
    {
        return Math.PI * (radius * radius);
    }

    public override string ToString()
    {
        return $"{FigureType} {Circle_Color.GetColor()} цвета радиусом {radius} площадью {Area()}.";
    }
}
