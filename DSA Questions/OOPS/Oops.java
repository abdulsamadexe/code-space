public class Oops {
    public static void main(String args[]){
        Pen a=new Pen();
        a.setColor("blue");
        a.setTip(5);
        System.out.println(a.getColor());
    }
}
    class Pen{
        private int tip;
        private String color;
        public void setColor(String color){
            this.color=color;
        }
        public void setTip(int tip){
            this.tip=tip;
        }
        public String getColor(){
            return this.color;
        }
        public int getTip(){
            return this.tip;
        }
    }
