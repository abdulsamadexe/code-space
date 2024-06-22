public class Oops {
    public static void main(String args[]){
        circle c1 = new circle(20);
        circle c2=new circle(20,24);

        c1.setRadius(30);
        c1.setEdgeThickness(10);
        c1.setColor("Red");

        c2.setRadius(40);
        c2.setEdgeThickness(20);
        c2.setColor("Blue");

        System.out.println("Circle 1: Radius: "+c1.radius+" Edge Thickness: "+c1.edgethickness+" Color: "+c1.color);

        System.out.println("Circle 2: Radius: "+c2.radius+" Edge Thickness: "+c2.edgethickness+" Color: "+c2.color);
        
    }
}
class circle{
    int radius;
    int edgethickness;
    String color;
    int password;
    circle(int radius){
        this.radius=radius;
    }
    circle(int radius, int password){
        this.radius=radius;
        this.password=password;
    }

    public void setRadius(int radius){
        this.radius=radius;
    }
     public void setEdgeThickness(int edgethickness){
        this.edgethickness=edgethickness;
    }

    public void setColor(String color){
        this.color=color;
    }

    public void setPassword(int password){
        this.password=password;
    }

    private void getPasswrod(){
        System.out.println("Password: "+this.password);
    }
}
