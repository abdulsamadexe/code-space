public class subarrays {
    public static void main(String[] args) {
        int[] nums={0,1,2,3,4,5,6,7,8,9,};
        int total=0;

        for(int i=0;i<nums.length;i++){
            int sum=0;
            System.out.printf("(%d) ",i);
            for(int j=i+1;j<nums.length;j++){
                int start=i;
                int end=j;
                System.out.print("(");
                for(start=i;start<=end;start++){
                    if(start==end){
                        System.out.print(nums[start]);

                    }
                    else{
                        System.out.print(nums[start]+",");
                    }
                    sum+=nums[start];
                }

                System.out.print(")");
            }
            System.out.println();
            total+=sum;

        }
        System.out.println("max sum is : "+total);
        System.out.println("min sumis : "+nums[0]);
    }
}
