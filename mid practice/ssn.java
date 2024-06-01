
import java.util.*;
public class ssn {
    public static void main(String[] args) {
    Scanner sc=new Scanner(System.in);
    String ssn=sc.nextLine();
    boolean valid=false;
    for(int i=0;i<ssn.length()-1;i++){
        char ch=ssn.charAt(i);
        if(i==4 || i==7){
            if(ch=='-' && i==4){
                valid=true;
            }
        
            else if(ch=='-' && i==7){
                valid=true;
            }
            else{
                valid=false;
                break;
            }
    }
        else{
            if(Character.isDigit(ch)){
                valid=true;
            }
            else{
                valid=false;
                break;
            }
        }
        if(ssn.length()!=12){
            valid=false;
            break;
        }


    }
    if(valid){
        System.out.println("valid ssn");
    }
    else{
        System.out.println("invalid ssn");
    }
}
}

