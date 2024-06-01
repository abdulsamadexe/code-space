import java.io.*;
import java.util.*;
public class practice4 {
    public static void main(String[] args) {
        File file=new File("numer.txt");
        System.out.println("Enter the name : ");
        Scanner sc1=new Scanner(System.in);
        String name=sc1.nextLine();
        System.out.println("Enter the gender m/F :");
        String gender=sc1.nextLine();
        gender=gender.toLowerCase();
        char gend=gender.charAt(0);
        try{
            Scanner sc=new Scanner(file);


            while(sc.hasNextLine()){
                int count=0;
                String[] words=new String[5];
                Scanner sc2=new Scanner(sc.nextLine());
                while(sc2.hasNext()){
                    words[count]=sc2.next().toLowerCase();
                    count++;
                }
                    
                    if(gend=='m' && words[1].equals(name)){
                        System.out.println("name : "+ name);
                        System.out.println("Rank : "+words[0]);
                    }
                    else if(gend=='f' && words[3].equals(name)){
                        System.out.println("name : "+ name);
                        System.out.println("Rank : "+words[0]);
        
                
            }
             
        }}catch(FileNotFoundException e){
            System.out.println("File not found");
        }catch(IOException e){
            System.out.println("Error reading file");
        }
        catch(Exception e){
            System.out.println("Error reading file");
        }
        finally{
            System.out.println("File read successfully");
        }
    }    
    }


