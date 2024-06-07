import java.io.*;
import java.util.*;
public class prac1 {
    public static void main(String[] args) {
        File file=new File("numbers.txt");
        try{
            FileWriter fw=new FileWriter(file);
            Scanner sc1=new Scanner(System.in);
            System.out.print("Enter the number of random number sto generate: ");
            int n=sc1.nextInt();
            for (int i = 0; i < n; i++) {
                fw.write((int)(Math.random()*100)+" ");
                
            }
            fw.close();
            int min=Integer.MAX_VALUE;
            int max=Integer.MIN_VALUE;
            try{
                Scanner sc=new Scanner(file);
                while(sc.hasNextInt()){
                    int num=sc.nextInt();
                    if(num<min){
                        min=num;
                    }
                    if(num>max){
                        max=num;
                    }
                }
                System.out.println("Minimum number: "+min
                +"\nMaximum number: "+max);
                sc.close();
                
            }catch(IOException e){
                e.printStackTrace();
            }
        }catch(IOException e){
            e.printStackTrace();


    
    }
    
}
}
