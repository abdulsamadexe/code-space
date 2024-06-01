import java.util.*;
public class spiratMatrix {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int matrix[][]=new int[3][3];
        for(int i=0;i<=2;i++){
            for(int j=0;j<3;j++){
                matrix[i][j]=sc.nextInt();
            }
        }
        for(int i=0;i<=2;i++){
            for(int j=0;j<3;j++){
                System.out.print(matrix[i][j]+" ");
            }
            System.out.println();
        }
        System.out.println();
        System.out.println();
        
        int startingrow=0;
        int startingcolumn=0;
        int endrow=matrix.length-1;
        int endcolumn=matrix[0].length-1;
        while(startingrow!=endrow && startingcolumn != endcolumn){
            for(int i=startingcolumn;i<endcolumn;i++){
                System.out.print(matrix[startingrow][i]+ " ");
            }
            for(int i=startingrow;i<endrow;i++){
                System.out.print(matrix[i][endcolumn]+ " ");
            }
            for(int i=endcolumn;i>startingcolumn;i--){
                System.out.print(matrix[endrow][i]+ " ");
            }
            for(int j=endrow;j>startingrow;j--){
                System.out.print(matrix[j][startingcolumn]+" ");
            }
            startingrow++;
            endrow--;
            startingcolumn++;
            endcolumn--;

        }
    }
}
