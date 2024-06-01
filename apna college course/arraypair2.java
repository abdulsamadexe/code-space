public class arraypair2 {
    public static void main(String[] args) {
        int[] nums={0,1,2,3,4,5,6,7,8,9,};
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                System.out.printf("(%d,%d)  ",nums[i],nums[j]);
            }
            System.out.println();
        }
    }
}
