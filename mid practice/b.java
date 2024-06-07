import java.util.*;
public class b {
    public static int[] sortarr(int[] list1,int[] list2){
        int[] list3=new int[list1.length];
        for(int i=0;i<list1.length;i++){
            if(i%2==0){
                list3[i]=list1[i];
            }
            else{
                list3[i]=list2[i];
            }
        }
        
        
        return list3;
    }

    public static int[][] transpose(int[][] arr){
       
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr[0].length; j++) {
                int tem = arr[i][j];
                arr[i][j] = arr[j][i];
                arr[j][i] = tem;
            }
        }
        return arr;

    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int[][] arr=new int[5][5];
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                arr[i][j]=sc.nextInt();
            }
        }
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                System.out.print(arr[i][j]+ " ");
            }
            System.out.println();
            
        }
        System.out.println();
        System.out.println();
        int[][] arr2=transpose(arr);

        for (int i = 0; i < arr2.length; i++) {
            for (int j = 0; j < arr2[0].length; j++) {
                System.out.print(arr2[i][j]+" ") ;
            }
            System.out.println();
            
        }

        
        
    }
}
