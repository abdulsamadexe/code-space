import java.util.*;
public class a{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String pass=sc.nextLine();
        boolean good=false;
        boolean digit=false;
        boolean alpha= false;
        while(!good){
            if(pass.length()>8){
                for(int i=0;i<pass.length();i++){
                    char ch=pass.charAt(i);
                    if(Character.isDigit(ch)){
                        digit=true;
                    }
                    if(Character.isUpperCase(ch)){
                        alpha=true;
                    }
                }
                if(alpha&&digit){
                    System.out.println("password is strong");
                    good=true;
                    break;
                }
                else{
                    pass=sc.nextLine();
                }
            }
            else{
                pass=sc.nextLine();
            }
            
        }
    }
}