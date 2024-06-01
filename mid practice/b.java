import java.util.*;
public class b {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String num=sc.next();
        boolean palindrome=false;
        for(int i=0;i<=num.length()/2;i++){
            if(num.charAt(i)==num.charAt(num.length()-(i+1))){
                palindrome=true;
            }
            else{
                palindrome=false;
                break;
            }
        }
        if(palindrome){
            System.out.println("palindro e");
        }
        else{
            System.out.println("not palindore");
        }
    }
}
