import java.util.*;
public class q7 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int num=sc.nextInt();
        if(num>90){
            System.out.println("Grade = A");
        }
        else if(num>80){
            System.out.println("Grade = B");
        }
        else if(num>70){
            System.out.println("Grade = C");
        }
        else if(num>60){
            System.out.println("Grade = D");
        }
        else if(num>50){
            System.out.println("Grade = F");
        }
        else if (num>=40){
            System.out.println("Grade = E");
        }
        else{
            System.out.println("Grade = F");
        }

    }
}
