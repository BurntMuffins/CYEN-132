public class Convert {
    public static final int NUMBER_OF_ITERATIONS = 15;
    public static void main(String[] args) {
        // While loop
        int count = 10;
        while(count > 0){
            System.out.println(count*5);
            count--;
        }

        // for loop (range)
        for (int i = 0; i < NUMBER_OF_ITERATIONS; i++){
            if (i < NUMBER_OF_ITERATIONS - 1){
                System.out.print(i + ",");
            } else {
                System.out.println(i);
            }

        // for each loop
        int[] randValues = {23, 27, 100, 86, 34};
        for (int val : randValues) {
            System.out.println(val/2.5);
        }

        }
    }
}
