import java.util.*;
import java.math.BigInteger;

public class Stairs {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int stairs = Integer.parseInt(scanner.nextLine());

        BigInteger result = stairsCombinations(stairs);
        System.out.println(result);
    }

    public static BigInteger stairsCombinations(int stairs) {
        if (stairs == 0) {
            return BigInteger.ONE;
        }

        BigInteger[] dp = new BigInteger[stairs + 1];
        dp[0] = BigInteger.ONE;
        dp[1] = BigInteger.ONE;

        for (int i = 2; i <= stairs; i++) {
            dp[i] = dp[i - 1].add(dp[i - 2]);
        }

        return dp[stairs];
    }
}
