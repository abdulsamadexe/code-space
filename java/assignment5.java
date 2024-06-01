import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a SSN: ");
        String ssn = input.nextLine();

        if (isValidSSN(ssn)) {
            System.out.println(ssn + " is a valid social security number");
        } else {
            System.out.println(ssn + " is an invalid social security number");
        }
    }

    public static boolean isValidSSN(String ssn) {
        if (ssn.length() != 11) {
            return false;
        }

        for (int i = 0; i < ssn.length(); i++) {
            if (i == 3 || i == 6) {
                if (ssn.charAt(i) != '-') {
                    return false;
                }
            } else {
                if (!Character.isDigit(ssn.charAt(i))) {
                    return false;
                }
            }
        }

        return true;
    }
}
