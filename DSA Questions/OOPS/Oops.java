public class Oops {
    public static void main(String args[]){
        Pen a=new Pen();
        a.setColor("blue");
        a.setTip(5);
        System.out.println(a.getColor);
    }
}
class Pen{
    private int tip;
    private String color;
    public static void setColor(String color){
        this.color=color;
    }
    public static void setTip(int tip){
        this.tip=tip;
    }
    public static void getColor{
        return this.color;
    }
    public static void getTip(){
        return this.tip;
    }
}
