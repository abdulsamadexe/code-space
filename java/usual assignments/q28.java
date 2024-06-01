public class q28 {
    public static void main(String[] args) {
            boolean sunnyDay = true;
            boolean weekend = true;
    
            boolean goOut = sunnyDay && weekend; // Logical AND
            boolean watchMovie = sunnyDay || !weekend; // Logical OR and NOT
    
            System.out.println("Can I go out? " + goOut);
            System.out.println("Should I watch a movie? " + watchMovie);
        }
    }

