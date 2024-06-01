// Write a program that searches a file of numbers and displays the largest number, the smallest number, and the average of all the numbers in the file. Do not assume that the numbers in the file are in any special order. Your program should obtain the file name from the user. Use either text or  binary file. For the text-file version, assume one number per line. For the binary-file version, use numbers of type double that are written using writeDouble.
import java.util.*;
import java.io.*;
public class practice1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the file name: ");
        String fileName = sc.nextLine();
        File file = new File(fileName);
        try {
            Scanner fileScanner = new Scanner(file);
            double largest = Double.MIN_VALUE;
            double smallest = Double.MAX_VALUE;
            double sum = 0;
            int count = 0;
            while (fileScanner.hasNextDouble()) {
                double num = fileScanner.nextDouble();
                if (num > largest) {
                    largest = num;
                }
                if (num < smallest) {
                    smallest = num;
                }
                sum += num;
                count++;
            }
            System.out.println("Largest number: " + largest);
            System.out.println("Smallest number: " + smallest);
            System.out.println("Average: " + sum / count);
            fileScanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        }
        
}
}