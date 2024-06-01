import java.util.*;
public class q4 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        char a=sc.nextLine().charAt(0);
        if(a=='a' || a=='e' || a=='i' || a=='o' || a=='u'){
            System.out.println("vowel");
        }
        else{
            System.out.println("consonant");
        }
    }
}
