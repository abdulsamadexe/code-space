import java.util.*;
public class Assigment2 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter string : ");
        String a=sc.nextLine();
        System.out.print("Enter string : ");
        String b=sc.nextLine();
        if(a.contains(b)){
            System.out.println(b+" is a substring of "+a);
        }
    }
}
