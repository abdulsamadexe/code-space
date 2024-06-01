// Write a program that checks a text file for several formatting and punctuation matters. The program asks for the names of both an input file and an output file. It then copies all the text from the input file to the output file, but with the following two changes: (1) Any string of two or more blank characters is replaced by a single blank; (2) all sentences start with an uppercase letter. All sentences after the first one begins after either a period, a question mark, or an exclamation mark that is followed by one or more whitespace characters.
import java.util.*;
import java.io.*;
public class practice2 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the name of the input file: ");
        String input=sc.nextLine();
        System.out.println("Enter the name of the output file: ");
        String output=sc.nextLine();
        try{
            File file1=new File(input);
            File file2=new File(output);
            Scanner sc1=new Scanner(file1);
            PrintWriter writer=new PrintWriter(file2);
            boolean first=true;
            while(sc1.hasNextLine()){
                String word=sc1.nextLine();
                Scanner lineScanner=new Scanner(word);
                while(lineScanner.hasNext()){
                    String line=lineScanner.next();
                    if(first){
                        line=line.substring(0,1).toUpperCase()+line.substring(1);
                        first=false;
                    }
                    writer.print(line+" ");
                    if(line.endsWith(".")||line.endsWith("?")||line.endsWith("!")){
                        first=true;
                    }
                }
                lineScanner.close(); // Close the lineScanner
            }
            writer.flush(); // Flush the writer
            writer.close(); // Close the writer
            sc1.close(); // Close the sc1
        }catch(FileNotFoundException e){
            System.out.println("File not found");
        }
        catch(IOException e){
            System.out.println("Error reading file");
        }
        finally{
            sc.close();
        }
}
}






// Scanner input = new Scanner(System.in);
//         System.out.print("Enter the name of the input file: ");
//         String inputFileName = input.nextLine();
//         System.out.print("Enter the name of the output file: ");
//         String outputFileName = input.nextLine();
//         try {
//             Scanner inputFile = new Scanner(new File(inputFileName));
//             PrintWriter outputFile = new PrintWriter(outputFileName);
//             boolean firstSentence = true;
//             while (inputFile.hasNextLine()) {
//                 String line = inputFile.nextLine();
//                 Scanner lineScanner = new Scanner(line);
//                 while (lineScanner.hasNext()) {
//                     String word = lineScanner.next();
//                     if (firstSentence) {
//                         word = word.substring(0, 1).toUpperCase() + word.substring(1);
//                         firstSentence = false;
//                     }
//                     outputFile.print(word + " ");
//                     if (word.endsWith(".") || word.endsWith("?") || word.endsWith("!")) {
//                         firstSentence = true;
//                     }
//                 }
//                 outputFile.println();
//             }
//             inputFile.close();
//             outputFile.close();
//         } catch (FileNotFoundException e) {
//             System.out.println("File not found.");