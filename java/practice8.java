import java.util.*;
public class practice8 {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.print("Enter a decimal integer (0 to 15) : ");
        int num=sc.nextInt();
        String hex;
        if(num>15 || num<0){
            System.out.print(num + " is invalid input");
        }
        else{
            if(num==10){
                System.out.println("A");
            }
            else if(num==11){
                System.out.println("B");
            }
            else if(num==12){
                System.out.println("C");
            }
            else if (num==13){
                System.out.println("D");
            }
            else if(num==14){
                System.out.println("E");
            }
            else if(num==15){
                System.out.println("F");
            }
            else{
                System.out.println(num);
            }
        }
        System.out.println(((char)num));
    }
}
