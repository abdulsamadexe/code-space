import java.util.Scanner;

public class new1{
    public static double rec(double money,int time){
        if(time==1){
            return money*1.005;
        }
        if(time==0){
            return money;
        }
        money = rec(money,time-1); // Assign the return value of the recursive call to 'money'
        return money*1.005;
    }
    public static void main(String[] args) {
        System.out.println(rec(10,5)); 
    }
}
