package recursion;

public class recursion1{


    // print fibonaci series
    public static int fib(int n){
        if(n==0){
            return 0;
        }
        if(n==1){
            return 1;
        }
        
        int next=fib(n-2)+fib(n-1);
        System.out.print(next+" ");
        return next;

    }


    // print sum of natural numbers
    public static int natural(int n){
        int sum=0;
        if(n==1){
            return 1;
        }
        sum=n+natural(n-1);
        return sum;
    }


     //print factorial of a number
     public static int factorial(int n){
        int factorials=1;
        if(n==1){
            return 1;
        }
        factorials=n*factorial(n-1);
        return factorials;
    }


    // Print numbers in desending order
    public static  void printDec(int n){
        if(n==1){
            System.out.print(n+ " ");
            return;
        }
        System.out.print(n+ " ");
        printDec(n-1);
    }


    // print numbers in increasing order
    public static void printIncreasing(int n){
        if(n==1){
            System.out.print(n+ " ");
            return;
        }
        
        printIncreasing(n-1);
        System.out.print(n+ " ");
    }


    //check if array is sorted
    public static boolean isSorted(int[] arr,int i){
        if(i==arr.length-1){
            return true;
        }   
        if(arr[i]>arr[i+1]){
            return false;
        }
        return isSorted(arr,i+1);
        
    }
    public static void main(String args[]){
        int[] arr={3,4,5,6,9,7};
        System.out.print(isSorted(arr,0));

    }
}