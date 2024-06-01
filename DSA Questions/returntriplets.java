public class returntriplets {
    public static void main(String[] args) {
        int nums[]=new int[10];
        for(int i=-4;i<5;i++){
            nums[i+4]=i;
        }
        for(int i=0;i<nums.length-1;i++){
            for(int j=0;j<nums.length-1;j++){
                for(int k=0;k<nums.length-1;k++){
                    if(nums[i]+nums[j]+nums[k]==0){
                        System.out.printf("(%d , %d , %d)\n",nums[i],nums[j],nums[k]);
                    }
                }
            }
        }
    }
}
