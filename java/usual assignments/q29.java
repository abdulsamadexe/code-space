import java.util.Scanner;

public class q29 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Is it raining? (true/false): ");
        boolean isRaining = scanner.nextBoolean();

        System.out.print("Do you have an umbrella? (true/false): ");
        boolean hasUmbrella = scanner.nextBoolean();

        boolean goOutside = !isRaining || hasUmbrella;

        if (goOutside) {
            System.out.println("You can go outside!");
        } else {
            System.out.println("It's better to stay indoors.");
        }

        scanner.close();
    }
}
