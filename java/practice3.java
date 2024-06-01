// Write a program to create a file named Text_IO.txt if it does not exist. Append new data to it if it already exists. Write 100 integers created randomly into the file using text I/O. Integers are separated by a space.(You may look into FileWrite and BufferedWriter)
import java.io.*;
import java.util.*;
public class practice3 {
    public static void main(String[] args) {
        File file =new File("Text_IO.txt");
        try{
            FileWriter writer=new FileWriter(file);
            for(int i=0;i<100;i++){
                double num=(Math.random()*100);
                
                writer.write(num+  " ");
            }
        }catch(IOException e){
            System.out.println("Error reading file");
        }
        finally{
            System.out.println("File created successfully");
        
    }
}
}