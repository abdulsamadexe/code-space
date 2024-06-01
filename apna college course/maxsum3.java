public class maxsum3 {
        public static void main(String[] args) {
            int[] nums={1,-2,6,-1,3};
            int maxsum=Integer.MIN_VALUE;
            int cursum=0;
            for(int i=0;i<nums.length;i++){
                
                cursum+=nums[i];
                if (cursum<0){
                    cursum=0;
                }
                if(cursum>maxsum){
                    maxsum=cursum;
                }
            }
            System.out.println(maxsum);
    }
}
