//the program should have a function that accepts a sentence as an argument and  should print the number of vowels in the sentence.ensure proper exception handling in the code
public class vowel {
    public static void main(String[] args) {
        try {
            printVowelCount("Hello, world!");
        } catch (NullPointerException e) {
            System.out.println("Input string is null.");
        }
    }

    public static void printVowelCount(String sentence) {
        if (sentence == null) {
            throw new NullPointerException();
        }

        int vowelCount = 0;
        String vowels = "aeiouAEIOU";

        for (int i = 0; i < sentence.length(); i++) {
            if (vowels.indexOf(sentence.charAt(i)) != -1) {
                vowelCount++;
            }
        }

        System.out.println("Number of vowels: " + vowelCount);
    }
}