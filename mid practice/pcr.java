public class pcr {
    public static void main(String[] args) {
        int[] array = {1, 2, 2, 3, 4, 4, 5, 6, 6, 7};
        int[] uniqueArray = removeDuplicates(array);
        for (int i : uniqueArray) {
            if (i != 0) {
                System.out.print(i + " ");
            }
        }
    }

    public static int[] removeDuplicates(int[] array) {
        int[] uniqueArray = new int[array.length];
        int uniqueCount = 0;

        for (int i = 0; i < array.length; i++) {
            boolean isDuplicate = false;
            for (int j = 0; j < i; j++) {
                if (array[i] == array[j]) {
                    isDuplicate = true;
                    break;
                }
            }
            if (!isDuplicate) {
                uniqueArray[uniqueCount++] = array[i];
            }
        }
        return uniqueArray;
    }
}
