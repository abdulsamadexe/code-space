// //Write a Three different programs using recursion and Draw Complete Stack diagram.

// a. Factorial of each digit of a 3 digit number given through the keyboard.

// b. power of x

// c. Sum of all Prime Numbers in the Range (1 to N) where N is given by the user.


import java.util.*;
public class a{
    public static int factorial(int n){
        if(n==0){
            return 1;
        }
        int result=n*factorial(n-1);
        return result;

    }


    public static int power(int n,int pow){
        if(pow==0){
            return 1;
        }
        int result=n*power(n,pow-1);

        return result;
    }

    public static int sumOfPrime(int n){
        if(n==1){
            return 0;
        }
        boolean prime=true;
        for(int i=2;i<n;i++){
            if(n%i==0){
                prime=false;
            }
        }
        if(prime){
            return n+sumOfPrime(n-1);
        }
        else{
            return sumOfPrime(n-1);
        }
        

    }
    



    public static void main(String[] args) {
        
        
    }
}