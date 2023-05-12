public class Searching {
    public static void main(String[] args) {
        int[] x = {5, 10, 32, 12, 8};
        //int item = 32;
        showList(x);
        // sorting a list
        int n = x.length;
        for (int i = 0; i < n-2; i++){
            int minPosition = i;
            for (int j = i+1; j < x.length; j++){
                if (x[j] < x[minPosition]){
                    minPosition = j;
                }
            }
            //swapping items in an array
            int temp = x[i];
            x[i] = x[minPosition];
            x[minPosition] = temp;
        }
        showList(x);
    }

    public static void showList(int[] list){
        for (int i = 0; i < list.length; i++){
            System.out.print(list[i]+", ");
        }
        System.out.println("");
    }
}
