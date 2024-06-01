import java.util.*;
public class assignment3 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        String binary="";
        while(a!=0){
            int digit=a%2;
            binary=binary+Integer.toString(digit);
            a/=2;
        }
        for(int i=binary.length()-1;i>=0;i--){
            System.out.print(binary.charAt(i));
        }
        sc.close();
    }
    
}
