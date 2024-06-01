public class arraypairs {
    public static void main(String[] args) {
        int array[]={2,4,6,8,10,12,14};
        for (int i=0;i<array.length;i++){
            for(int j=i+1;j<array.length;j++){
                System.out.printf("(%d,%d)",array[i],array[j]);
            }
        }
    }
}
