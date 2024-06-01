import java.util.Scanner;

public class assignment1 {
    public static void main(String[] args) {
        int count=1;
        for(int i=101;i<=2100;i++){
            if(isLeapYear(i)) {
                System.out.print(i + " ");
                count+=1;
                if(count%10==0){
                    System.out.println();
                }
            }
            
    }
    }

    public static boolean isLeapYear(int year) {        
        return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    }
}
