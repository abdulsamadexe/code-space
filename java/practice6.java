public class practice6 {
    public static void main(String[] args) {
        System.out.println(sumDigits(1234));
    }
    public static int sumDigits(long num){
        int sum=0;
        while(num!=0){
            long digit=num%10;
            num=num/10;
            sum+=digit;
        }
        return sum;
    }
}
