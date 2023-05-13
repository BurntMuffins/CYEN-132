package Programs.Program_5;

public class GameCharacter {
    /* VARIABLES */
    private String name;
    private int lives;
    private String[] inventory;
    private final int MAXLIVES = 5;

    /* CONSTRUCTORS */

    // default constructor
    public GameCharacter(){
        name = "Sam Sung";
        lives = MAXLIVES;
        inventory = new String[5];
    }

    // overload contructor
    public GameCharacter(String name, int lives){
        setName(name);;
        setLives(lives);
        inventory = new String[5];
    }

    /* ACCESSORS AND MUTATORS */
    public String getName(){
        return name;
    }

    public void setName(String name){
        this.name = name;
    }

    public int getLives(){
        return lives;
    }

    // Sets the lives to MAXLIVES if lives > MAXLIVES or less than 0, otherwise sets it to the input
    public void setLives(int lives){
        if (lives > MAXLIVES || lives < 0){
            this.lives = MAXLIVES;
        } else {
            this.lives = lives;
        }
    }

    // Returns a string with all of the items in the inventory separated by commas and spaces
    public String getInventory(){
        String str = "";
        for (int i = 0; i < inventory.length; i++) {
            if (inventory[i] != null){
                str += inventory[i] + ", ";
            }
        }
        str += "\n";
        return str;
    }

    public void setInventory(String[] inv){
        this.inventory = inv;
    }

    /* METHODS */

    // returns a boolean value based on the amount of lives the player has
    public boolean isAlive(){
        if (lives < 1){
            return false;
        } else {
            return true;
        }
    }

    // retruns a boolean value based on if the player has a weapon
    public boolean hasWeapon(){
        for (int i = 0; i < inventory.length; i++) {
            if ("gun".equals(inventory[i]) || "knife".equals(inventory[i])){
                return true;
            }
        }
        return false;
    }

    // returns an integer representing the ammount of non-null objects in the inventory
    public int sizeOfInventory(){
        int count = 0;
        for (int i = 0; i < inventory.length; i++) {
            if (inventory[i] != null){
                count++;
            }
        }
        return count;
    }

    // sets the lives to max
    public void heal(){
        setLives(MAXLIVES);
    }

    // removes a life from the player
    public void damage(){
        if (isAlive()){
            lives--;
        }
    }

    // adds an item to the inventory if there is enough toom in the list
    public void pickUp(String item){
        for (int i = 0; i < inventory.length; i++) {
            if (inventory[i] == null){
                inventory[i] = item;
                return;
            }
        }
    }

    // removes the given input from the list if it is in the list
    public void drop(String item){
        for (int i = 0; i < inventory.length; i++) {
            if (item.equals(inventory[i])){
                inventory[i] = null;
            }
        }
    }

    // returns a string displaying some base information of the player
    public String toString(){
        return "Name:\t" + name + "\nLives:\t" + lives + "\nInventory: " + getInventory();
    }
}
