//https://judge.softuni.org/Contests/Practice/Index/4004#2

//This is a problem from Algorithms with Java course.
//Python to Java converter used for testing the code in judge system


import java.util.*;

public class BitcoinTransactions {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] first = scanner.nextLine().split(" ");
        String[] second = scanner.nextLine().split(" ");

        int[][] lcsMatrix = getLcsMatrix(first, second);
        Deque<String> result = reconstructLcsSequence(first, second, lcsMatrix);

        StringBuilder sb = new StringBuilder();
        sb.append("[");
        while (!result.isEmpty()) {
            sb.append(result.removeFirst());
            if (!result.isEmpty()) {
                sb.append(" ");
            }
        }
        sb.append("]");

        System.out.println(sb.toString());
    }

    public static int[][] getLcsMatrix(String[] firstSeq, String[] secondSeq) {
        int rows = firstSeq.length + 1;
        int cols = secondSeq.length + 1;
        int[][] dp = new int[rows][cols];

        // Calculating the Longest Common Subsequence (LCS) - Table
        for (int row = 1; row < rows; row++) {
            for (int col = 1; col < cols; col++) {
                if (firstSeq[row - 1].equals(secondSeq[col - 1])) {
                    dp[row][col] = dp[row - 1][col - 1] + 1;
                } else {
                    dp[row][col] = Math.max(dp[row - 1][col], dp[row][col - 1]);
                }
            }
        }

        return dp;
    }

    public static Deque<String> reconstructLcsSequence(String[] firstSeq, String[] secondSeq, int[][] dp) {
        int row = firstSeq.length;
        int col = secondSeq.length;
        Deque<String> path = new ArrayDeque<>();

        while (row > 0 && col > 0) {
            if (firstSeq[row - 1].equals(secondSeq[col - 1])) {
                path.addFirst(firstSeq[row - 1]);
                row--;
                col--;
            } else if (dp[row - 1][col] >= dp[row][col - 1]) {
                row--;
            } else {
                col--;
            }
        }

        return path;
    }
}