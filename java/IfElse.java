import java.util.Scanner;

public class IfElse {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.close();
        if (n % 2 == 1) {
            System.out.println("Weird");
        }
        if ((n % 2 == 0) && 2 <= n && n <= 5) {
            System.out.println("Not Weird");
        }
        if ((n % 2 == 0) && 6 <= n && n <= 20) {
            System.out.println("Weird");
        }
        if ((n % 2 == 0) && 20 < n) {
            System.out.println("Not Weird");
        }
    }
}
