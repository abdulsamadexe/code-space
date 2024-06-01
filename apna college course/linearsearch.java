public class linearsearch{
    public static int LinearSearch(int numbers[],int key){
        for(int i=0;i<numbers.length;i++){
            if(numbers[i]==key){
                return i;
            }
        }
        return -1;
    }
    public static int BinarySearch(int numbers[],int key){
        int start=0;
        int end=numbers.length;
        while (start<=end){
            int mid=(start+end)/2;
            if(key==numbers[mid]){
                return mid;
            }
            else if(key>numbers[mid]){
                start=mid;
            }
            else{
                end=mid;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int numbers[]={2,4,5,8,9,10,15,18,19};
        int key=9;
        int index=BinarySearch(numbers,key);
        System.out.println("Index of key is : "+index);
        
    }
}