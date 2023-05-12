public class Lists {
    public static void main(String[] args) {
        int[] x = new int[5];
        // {0, 0, 0, 0, 0}

        for (int i = 0; i < x.length; i++){
            System.out.print(x[i]+",");
        }

        System.out.println();
        
        // {0, 5, 0, 0, 0}
        x[1] = 5;
        
        for (int i = 0; i < x.length; i++){
            System.out.print(x[i]+",");
        }

        System.out.println();

        String[] sentence = {"hello", "how", "was", "your", "day?"};
        for (int i = 0; i < sentence.length; i++){
            System.out.print(sentence[i]+" ");
        }
    }
}
