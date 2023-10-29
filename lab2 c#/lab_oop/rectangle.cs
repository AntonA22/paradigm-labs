public class Rectangle : Figure
{
    public static string FigureType = "Прямоугольник";
    private double _a;
    private double _b;
    private Color _rColor;

    public Rectangle(double a, double b, string color)
    {
        _a = a;
        _b = b;
        _rColor = new Color(color);
    }

    public override double Area()
    {
        return _a * _b;
    }

    protected Color RColor
    {
        get { return _rColor; }
    }

    protected double A
    {
        get { return _a; }
    }

    protected double B
    {
        get { return _b; }
    }

    public override string ToString()
    {
        return $"{FigureType} {RColor.GetColor()} цвета с длиной стороны {A}, шириной стороны {B}, площадью {Area()}.";
    }
}
