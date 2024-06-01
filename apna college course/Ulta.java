public class Ulta{
    public static void arrayreverse(int numbers[]){
        int first=0,last=numbers.length-1;
        while(first<last){
            int temp=numbers[first];
            numbers[first]=numbers[last];
            numbers[last]=temp;
            first++;
            last--;
        }
    }

public static void main(String[] args){
    int numbers[]={0,1,2,3,4,5,6,7,8,9};
    System.out.println(numbers.length);
    arrayreverse(numbers);
    for(int i=0;i<numbers.length;i++){
        System.out.print(numbers[i]+" ");
    }
}
}