import java.util.*;
public class method {
    public static int Sum(int a,int b){
        int sum=a+b;
        return sum;
    }
    public static int Product(int a,int b){
        int product=a*b;
        return product;
    }
    public static int Factorial(int a){
        int factorial=1;
        for (int i=1;i<=a;i++){
            factorial*=i;
        }
        return factorial;
        }
    public static boolean Isprime(int a){
        if (a==2){
            return true;
        }
        for(int i=2;i<=Math.sqrt(a);i++){
            if (a%i==0){
                return false;
            }
        }
        return true;
    }
    public static void bintodec(int a){
        int base10=0;
        int pow=0;
        while (a>0){
            int digit=a%10;
            base10= base10+(int)(digit*Math.pow(2, pow));
            pow++;
            a/=10;
        }
        System.out.println(base10);

    }
    public static void Primesinrange(int a){
        for(int i=2;i<a;i++){
            if (Isprime(i)){
                System.out.print(i+"  ");
            }
        }
    
    }

    public static void dectobin(int dec){
        int bin=0;
        int power=0;
        while (dec>1){
            bin+=dec%2*(Math.pow(10, power));
            power++;
            dec/=2;
        }
        bin+=1*Math.pow(10, power);
        System.out.println(bin);
        
    }
    
    public static void main(String[] args) {
        System.out.println(Sum(68,28));
        System.out.println("Factorail of 5 is : "+Factorial(5));
        bintodec(1011);
        dectobin(10);

    }
}
