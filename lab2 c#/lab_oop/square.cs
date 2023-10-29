public class Square : Rectangle
{
    public new static string FigureType = "Квадрат";

    public Square(double a, string color) : base(a, a, color)
    {}

    public override string ToString()
    {
        return $"{FigureType} {RColor.GetColor()} цвета с длиной стороны {A}, площадью {Area()}.";
    }
}


