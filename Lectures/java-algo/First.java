class First{

/*
    static- a function or definition that does not change during runtime
    There is only one copy of something (main function or other functions)

    Private or public
    Modifiers:
    Private - can only be accessed by the class where it is defined
    Public - can be accessed outside of the class

    return types -> Data Types
    what the function will return 
    void - return nothing (return is not required)
    all other data types are required to return that data type

    if we have int we return an int => return 0; 
    Or return a variable defined as an int

    primitive types:
    long, double, boolean, String, char
*/

/*
 *      modifier return_type function_name(parameters){
 *              depending on the function if it is void return nothing
 *              or return the type
 *      }
 * 
 *      private int add(int a, int b){
 *              return a + b;
 *      }
 * 
 *      public void showStatus(String status){
 *          System.out.println("The current status of the ship is " + status);
 *      }
 * 
 */

public static final int ITERATIONS = 10_000; // Can't change becasue it is a constant

// Main execution of the program
public static void main(String args[]) {
        int num1, num2, num3, num4;
        double num5 = .12;
        boolean isHere = false;
        num3 = 5;
        num4 = 12;
        System.out.println(num3+" + "+num4+" = "+(num3+num4)); // Similar to printing
        //ITERATIONS += 1; // this isn't possible
        System.out.println(ITERATIONS);
    }

}