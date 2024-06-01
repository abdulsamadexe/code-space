public class maxsumarray {
    public static void main(String[] args) {
        int[] nums={1,-2,6,-1,3};
        int maxsum=Integer.MIN_VALUE;
        
        for(int i=0;i<nums.length;i++){
            int start=i;
            for(int j=i;j<nums.length;j++){
                int sum=0;
                int end=j;
                for(int k=start;k<=end;k++){
                    sum+=nums[k];
                }
                if(sum>maxsum){
                    maxsum=sum;
                }
                System.out.println(sum);
            }
        }
        System.out.println("max sum is : "+maxsum);
    }
}
