import java.util.*;
public class javapractice {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        // int sum=0;
        // System.out.print("ENter the range to print : ");
        // int range=sc.nextInt();
        // int counter=1;
        // while (counter<=range) {
        //     sum+=counter;
        //     counter++;
        // }
        // System.out.println("Sum of intgers upto "+ range+" is "+sum);

        // System.out.print("Enter the number : ");
        // int num=sc.nextInt();
        // while (num!=0){
        //     int digit=num%10;
        //     num/=10;
        //     System.out.print(digit);

        
        
        // while (true){
        //     System.out.print("Enter a number : ");
        //     int num=sc.nextInt();
        //     if (num%10==0){
        //         continue;
        //     }
        //     else{
        //         System.out.println(num);
        // }
        // }
            
        int test=sc.nextInt();
        for(int i=2;i<test;i++){
            if (test%i==0){
                System.out.println("Number is not a prime number");
                break;
            }
            if(i==(test-1)){
                System.out.println("Number is a prime number");
                break;
            
            }
            }
        }
    }
    

