public class practice7 {
    public static void reverse(int num){
        int num2=0;
        int temp=num;
        int digits=1;
        System.out.println(num);
        while(num!=0){
            if(num/10!=0){
                digits*=10;
                }
            num/=10;
            
        }
        while(temp!=0){
            int digit = temp%10;
            num2+=digit*(digits);
            digits/=10;
            temp/=10;
        }
        
        System.out.println(num2);

    }
    public static void main(String[] args) {
        reverse(4563);
    }
}
