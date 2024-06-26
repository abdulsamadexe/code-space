package recursion;

public class recursion1{

        // print Fibonacci series using recursion
        public static void printFibonacci(int n, int a, int b){
            if(n > 0){
                System.out.print(a + " ");
                printFibonacci(n - 1, b, a + b);
            }
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

    //find x to the power n
    public static int power(int x,int n){
        if(n==0){
            return 1;
        }

        return x*power(x,n-1);
    }


    //optimzed x to the power n
    public static int Power(int n,int pow){
        if(pow==0){
            return 1;
        }
        int x=Power(n,pow/2);
        if(pow%2==0){
            return x*x;
        }
        return n*x*x;
    }

    public static void main(String args[]){
        printFibonacci(10,0,1);

    }
}