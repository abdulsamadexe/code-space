public class arraysCC{
    public static int trappedrainwater(int height[]){
        int n=height.length;
        //Calculate left most boundary --array
        int leftmax[]=new int[n];
        leftmax[0]=height[0];
        for(int i=1;i<n;i++){
            leftmax[i]=Math.max(leftmax[i-1],height[i]);
        }
        //Calculate right max boundary --arr
        int rightmax[]=new int[n];
        rightmax[n-1]=height[n-1];
        for(int i=n-2;i>=0;i--){
            rightmax[i] = Math.max(height[i],rightmax[i+1]);
        }
        
        // loop
        int trappedwater=0;
        for(int i=0;i<n;i++){
                    // waterlevel=min(leftmax moundary,right max boundary)

        int waterlevel=Math.min(leftmax[i],rightmax[i]);
        //water stored= ater level-height[i]

        trappedwater+=waterlevel-height[i];;
        }
        return trappedwater;

        //trapped water+=water stored
    }

    public static void main(String args[]){
        int heights[]={4,2,0,6,3,2,5};
        int trappedwater=trappedrainwater(heights);
        System.out.print(trappedwater);
    }
}