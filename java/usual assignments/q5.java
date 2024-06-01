import java.util.*;
public class q5 {
    public static void main(String[] args){
        String username="abdulsamad";
        String password="12345";
        Scanner sc=new Scanner(System.in);
        String user=sc.nextLine();
        String pass=sc.nextLine();
        if(user==username && password==pass){
            System.out.println("Welcome ");
        }
        else{
            System.out.println( "Username or Password is incorrect");
        }
    }
}
