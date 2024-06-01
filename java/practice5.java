import java.util.*;
public class practice5 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String word=sc.nextLine();
        for(int i=0;i<word.length();i++){
            if(i<word.indexOf("h")){
                System.out.print(word.charAt(i));
            }
            else if(i>word.lastIndexOf("h")){
            System.out.print(word.charAt(i));
            }
        }
    }
}
