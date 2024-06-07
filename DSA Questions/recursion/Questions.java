package recursion;

public class Questions {
    public static void occurence(int[] arr,int n,int index){
        if(index==arr.length){
            return;
        }
        
        if((arr[index]==n)){
            System.out.print(index+" ");
        }
        occurence(arr,n,index+1);
    }
    public static void main(String[] args) {
        int arr[]={1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10};
        occurence(arr,10,0);
    }
}
