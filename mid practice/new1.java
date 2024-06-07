import java.util.Scanner;

public class new1{
    public static void main(String[] args) {
        final int NUM_STUDENTS = 20;
        final int NUM_SUBJECTS = 5;
        int[][] marks = new int[NUM_STUDENTS][NUM_SUBJECTS];
        String[] subjects = {"Mathematics", "English", "Computer Science", "Chemistry", "Physics"};
        Scanner scanner = new Scanner(System.in);

        // Enter marks for each student in all subjects
        for (int i = 0; i < NUM_STUDENTS; i++) {
            System.out.println("Entering marks for student " + (i + 1) + ":");
            for (int j = 0; j < NUM_SUBJECTS; j++) {
                System.out.print("Enter marks for " + subjects[j] + ": ");
                marks[i][j] = scanner.nextInt();
            }
        }

        // Display total marks of each student
        studentResult(marks, NUM_STUDENTS, NUM_SUBJECTS);

        // Display marks obtained by all students in each subject
        subjectStats(marks, NUM_STUDENTS, NUM_SUBJECTS, subjects);

        // Display all marks in matrix form
        printResult(marks, NUM_STUDENTS, NUM_SUBJECTS, subjects);
    }

    public static void studentResult(int[][] marks, int numStudents, int numSubjects) {
        System.out.println("\nTotal marks of each student:");
        for (int i = 0; i < numStudents; i++) {
            int totalMarks = 0;
            for (int j = 0; j < numSubjects; j++) {
                totalMarks += marks[i][j];
            }
            System.out.println("Student " + (i + 1) + ": Total Marks = " + totalMarks);
        }
    }

    public static void subjectStats(int[][] marks, int numStudents, int numSubjects, String[] subjects) {
        System.out.println("\nMarks obtained by all students in each subject:");
        for (int j = 0; j < numSubjects; j++) {
            System.out.print(subjects[j] + ": ");
            for (int i = 0; i < numStudents; i++) {
                System.out.print(marks[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void printResult(int[][] marks, int numStudents, int numSubjects, String[] subjects) {
        System.out.println("\nMarks matrix:");
        System.out.print("Student\\Subject\t");
        for (String subject : subjects) {
            System.out.print(subject + "\t");
        }
        System.out.println();
        
        for (int i = 0; i < numStudents; i++) {
            System.out.print("Student " + (i + 1) + "\t\t");
            for (int j = 0; j < numSubjects; j++) {
                System.out.print(marks[i][j] + "\t\t");
            }
            System.out.println();
        }
    }
}
