// Write a Program to overload a function num_calc() as follows:

// a. With one integer argument and one character argument, computes the square of integer argument

// if choice ch is's otherwise finds its cube.

// b. With two integer arguments and one character argument. It computes the product of integer arguments if ch is 'p' else adds the integers.

// c. With two string arguments, which prints whether the strings are equal or not.


import java.util.*;
public class hexa {
    Scanner sc=new Scanner(System.in);
    public void num_calc(int a,char ch){
        if(ch=='s'){
            System.out.println(a*a);
        }
        else{
            System.out.println(a*a*a);
        }
    }
    public static void num_calc(int a,int b,char ch){
        if(ch=='p'){
            System.out.println(a*b);
        }
        else{
            System.out.println(a+b);
        }
    }
    public static void num_calc(String a,String b){
        if(a.equals(b)){
            System.out.println("Equal");
        }
        else{
            System.out.println("Not Equal");
        }
    }
    
}
