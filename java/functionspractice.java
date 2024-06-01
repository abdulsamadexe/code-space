// import java.util.*;
// public class functionspractice {
//     public static boolean Palindrome(int a){
//         int originalnumber =a;
//         int reverse=0;
//         int pow=0;
//         while (a>0){
            
//             a=a/10;
//             pow++;
//         }
//         int b=originalnumber;
//         while (b>0){
//             reverse=reverse+(b%10*(int)(Math.pow(10, pow)));
//             pow--;
//             b/=10;
//         }
//         if (reverse==originalnumber){
//             return true;
//     }
//         else{
//             return false;
//     }
//     }
    

    
// }
import java.util.*;

public class functionspractice {
    public static boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        int revertedNumber = 0;
        while (x > revertedNumber) {
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        }

        return x == revertedNumber || x == (revertedNumber / 10);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int x = scan.nextInt();
        boolean isPalindrome = isPalindrome(x);

        if (isPalindrome) {
            System.out.println(x + " is a palindrome.");
        } else {
            System.out.println(x + " is not a palindrome.");
        }

        scan.close();
    }
}