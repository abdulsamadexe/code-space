import java.util.*;
public class Question8 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter todays day : ");
        int day=sc.nextInt();
        System.out.print("Enter the number of days elapsed since today : ");
        int futureday=sc.nextInt();
        String days[]={"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"};
        
        String today=days[day];
        String daysFromToday=days[day+futureday];
        System.out.print("Today is "+today+" and the future days is "+daysFromToday);
        sc.close();
    }
}
