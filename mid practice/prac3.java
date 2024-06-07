import java.util.*;
import java.io.*;
public class prac3 {
    public static void studentResult(double[][] data){
        for (int i = 0; i < data.length; i++) {
            System.out.println("student "+(i+1)+" has obtained marks : ");
            double marks=0;
            for (int j = 0; j < data[0].length; j++) {
                  marks+=data[i][j];
            }
            System.out.println(marks+" out of 500");
        }
    }
    public static void main(String[] args) {
        double[][] data=new double[5][5];
        Scanner sc=new Scanner(System.in);
        for (int i = 0; i < 5; i++) {
            System.out.print("Enter the 5 scores of student "+(i+1)+": ");
            for (int j = 0; j < 5; j++) {
                data[i][j]=sc.nextDouble();
            }
        }
        studentResult(data);
    }
}
