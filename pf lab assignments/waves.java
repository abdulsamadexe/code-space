public class waves{
    public static void main(String [] args){
        for(int j=1;j<=6;j++){
            for(int i=1;i<j;i++){
                System.out.print("  ");
            }
            System.out.print("*");

            for(int i=5;i>=(j);i--){
                System.out.print(" ");
            }
            System.out.print("*");
            for(int i=5;i>=j;i--){
                System.out.print(" ");
            }
            System.out.print("*");
            for(int i=5;i>=j;i--){
                System.out.print(" ");
            }
            System.out.print("*");
            for(int i=5;i>=(j);i--){
                System.out.print(" ");
            }
            System.out.println("*");
        }
        System.out.println("           ***");
        System.out.print("            *\n  ");
        for(int i=2;i>=1;i--){
            for(int j=1;j<=11;j++){
                System.out.print("*  ");
            }
        System.out.println();
        }

          

}
}

