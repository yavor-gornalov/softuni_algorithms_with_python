import java.util.*;

public class Socks {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[] leftSocks = scanner.nextLine().split(" ");
        String[] rightSocks = scanner.nextLine().split(" ");

        int count = longestCommonSequenceCount(leftSocks, rightSocks);

        System.out.println(count);
    }

    public static int longestCommonSequenceCount(String[] firstSeq, String[] secondSeq) {
        int rows = firstSeq.length + 1;
        int cols = secondSeq.length + 1;

        int[][] dp = new int[rows][cols];

        for (int row = 1; row < rows; row++) {
            for (int col = 1; col < cols; col++) {
                if (firstSeq[row - 1].equals(secondSeq[col - 1])) {
                    dp[row][col] = dp[row - 1][col - 1] + 1;
                } else {
                    dp[row][col] = Math.max(dp[row - 1][col], dp[row][col - 1]);
                }
            }
        }

        return dp[rows - 1][cols - 1];
    }
}
