import java.util.Scanner;

public class Input {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        while(s.hasNextLine()){
            String line = s.nextLine();
            if (line.equalsIgnoreCase("hello")) {
                System.out.println("How are you?");
            } else {
                System.out.println("-> " + line);
            }
        }
        int a = 5555;
        Integer.toString(a);
        System.out.println((String) ""+a);
    }
}

