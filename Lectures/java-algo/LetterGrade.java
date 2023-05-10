

public class LetterGrade {
    
    public static void main(String args[]){
        double score = 79.5;
        char letter_grade;

        letter_grade = calcGrade(score);
        System.out.println("Your grade is " + letter_grade);
    }

    public static char calcGrade(double score){
        if (score >= 90) return 'A';
        else if (score >= 80) return 'B';
        else if (score >= 70) return 'C';
        else if (score >= 60) return 'B';
        else return 'F';
    }

}
