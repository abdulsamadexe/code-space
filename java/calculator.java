import java.util.*;
public class calculator {
    public static void main(String[] args) {
        int a,b,c,op;
        Scanner sc=new Scanner(System.in);
        
        System.out.print("Select the operation you want to perform\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Remainder\nEnter the operation you want to perform : ");
        a=sc.nextInt();
        System.out.print("ENter the value of number 1  : ");
        b=sc.nextInt();
        System.out.print("ENter the value of number 2 : ");
        c=sc.nextInt();
        switch(a){
            case 1:
                op=b+c;
                System.out.println(b+"+"+c+"="+op);
                break;
            case 2:
                op=b-c;
                System.out.println(b+"-"+c+"="+op);
                break;
            case 3:
                op=b*c;
                System.out.println(b+"*"+c+"="+op);
                break;
            case 4:
                op=b/c;                  
                System.out.println(b+"/"+c+"="+op);
                break;
            case 5:
                op=b%c;
                System.out.println("the remainder of a/b is "+op);
                break;
            default:
                System.out.println("Invalid Input");
        }
        sc.close();
    }
}
