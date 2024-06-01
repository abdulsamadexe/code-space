public class maxsumarray2 {
    public static void main(String[] args) {
        int[] nums={1,-2,6,-1,3};
        int maxsum=Integer.MIN_VALUE;

        int prefix[]=new int[nums.length];
        prefix[0]=nums[0];
        for(int i=1;i<nums.length;i++){
            prefix[i]=prefix[i-1]+nums[i];
        }
        
        for(int i=0;i<nums.length;i++){
            int start=i;
            for(int j=i;j<nums.length;j++){
                int end=j;
                int cursum=start==0?prefix[end]:prefix[end]-prefix[start-1];                
                if(cursum>maxsum){
                    maxsum=cursum;
                }
            }
        }
        System.out.println("max sum is : "+maxsum);
    }
}

