
public class test {
 public void readFile(String filename) throws FileNotFoundException {
     // Code to open the file (would throw FileNotFoundException) 
    Scanner reader = new Scanner(new File(filename));
    // Code to read the file contents (would never be reached due to exception) reader.close();
    }
 public static void main(String[] args) { 
    FileReader reader = new FileReader(); 
    reader.readFile("nonexistent_file.txt");
    // Potential FileNotFoundException (not handled) 
    // Code that would normally follow reading the file (would not execute) System.out.println("Successfully read the file!");
    }
 }
