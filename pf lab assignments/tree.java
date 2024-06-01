public class tree{
    public static void main(String [] args){
        for(int i=1;i<=3;i++){
            for(int j=1;j<=5;j++){
                for(int k=1;k<j;k++){
                    System.out.print(" ");
                }   
                System.out.print("*");
                for(int k=5;k>j;k--){
                    System.out.print(" ");
                }
                System.out.print("*");
                for(int k=5;k>j;k--){
                    System.out.print(" ");
                }            
                System.out.println("*");
    }
}
    }}