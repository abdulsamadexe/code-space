// Write a Java program that will read a file named given by the user. This file contains student ID and the scores of the student. Two lines of the file are shown below:

// 1234 67.5

// 1235 89.0

// Print out the total number of students and the average score. Find the number of students who obtains score above the average score. Your program must use proper Exception handling where required.

// Write the above output in another file named AvgScore.txt.


import java.util.*;
import java.io.*;
public class prac {
    public static void main(String[] args) {
        int students=0;
        double totalScore=0;
        
        File file=new File("students.txt");
        try{
            Scanner sc=new Scanner(file);
            while(sc.hasNextLine()){
                String line=sc.nextLine();
                Scanner lineScanner = new Scanner(line);
                while(lineScanner.hasNext()){
                    int id=Integer.parseInt(lineScanner.next());
                    students+=1;
                    double score=Double.parseDouble(lineScanner.next());
                    totalScore+=score;
                }
                lineScanner.close();
            }
            System.out.println("Total number of students: "+students);

            double avgScore=totalScore/students;
            System.out.println("Average score: "+avgScore);
            int aboveavg=0;
            


            while(sc.hasNextLine()){
                String line=sc.nextLine();
                Scanner lineScanner = new Scanner(line);
                while(lineScanner.hasNext()){
                    
                    double score=Double.parseDouble(lineScanner.next());
                    if(score>avgScore){
                        aboveavg+=1;
                    }
                    lineScanner.close();
                }
            }
            System.out.println("Number of students who obtained score above average: "+aboveavg);
            FileWriter fw = new FileWriter("avgscore.txt"); 
                fw.write("Total number of students: " + students + "\n");
                fw.write("Average score: " + avgScore + "\n");
                fw.write("Number of students who obtained score above average: " + aboveavg);
           fw.close();
           sc.close();
           

        }catch(IOException e){
            e.printStackTrace();
        }
    }
    
}
