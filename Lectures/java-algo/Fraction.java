public class Fraction {

    private int numerator;
    private int denominator;

    // contructor
    public Fraction(){
        numerator = 0;
        denominator = 1;
    }

    // overload contructor
    public Fraction(int n, int d){
        setNumerator(n);
        setDenominator(d);
    }

    public int getNumerator(){
        return numerator;
    }

    public void setNumerator(int numerator){
        // refers to the class numerator = refers to the setter numerator
        this.numerator = numerator;
    }

    public int getDenominator(){
        return denominator;
    }

    public void setDenominator(int denominator){
        if (denominator != 0){
            this.denominator = denominator;
        } else {
            this.denominator = 1;
        }
    }

    public Fraction mul(Fraction x){
        Fraction f = new Fraction();
        f.setNumerator(x.getNumerator() * getNumerator());
        f.setDenominator(x.getDenominator() * getDenominator());
        return f;
    }

    public String toString(){
        return numerator + "/" + denominator;
    }


}


class FractionMain{
    public static void main(String[] args) {
        Fraction f1 = new Fraction(5, 6);
        Fraction f2 = new Fraction(2, 3);
        System.out.println(f1.mul(f2));
    }
}