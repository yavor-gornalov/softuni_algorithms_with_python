import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class Climbing {
    public static int[][] generateReversedDPMatrix(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;

        int[][] dp = new int[rows][cols];

        // First, find all base solutions
        dp[rows - 1][cols - 1] = matrix[rows - 1][cols - 1];
        for (int r = rows - 2; r >= 0; r--) {
            dp[r][cols - 1] = dp[r + 1][cols - 1] + matrix[r][cols - 1];
        }
        for (int c = cols - 2; c >= 0; c--) {
            dp[rows - 1][c] = dp[rows - 1][c + 1] + matrix[rows - 1][c];
        }

        // Fill rest of the cells
        for (int r = rows - 2; r >= 0; r--) {
            for (int c = cols - 2; c >= 0; c--) {
                dp[r][c] = matrix[r][c] + Math.max(dp[r + 1][c], dp[r][c + 1]);
            }
        }

        return dp;
    }

    public static Deque<Integer> reconstructPath(int[][] dp, int[][] matrix) {
        int rows = dp.length;
        int cols = dp[0].length;
        Deque<Integer> path = new ArrayDeque<>();

        int r = 0, c = 0;
        while (r < rows - 1 && c < cols - 1) {
            path.addFirst(matrix[r][c]);
            if (dp[r + 1][c] > dp[r][c + 1]) {
                r += 1;
            } else {
                c += 1;
            }
        }
        for (int i = r; i < rows - 1; i++) {
            path.addFirst(matrix[i][cols - 1]);
        }
        for (int j = c; j < cols - 1; j++) {
            path.addFirst(matrix[rows - 1][j]);
        }
        path.addFirst(matrix[rows - 1][cols - 1]);

        return path;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int rows = Integer.parseInt(scanner.nextLine());
        int cols = Integer.parseInt(scanner.nextLine());

        int[][] matrix = new int[rows][cols];
        for (int r = 0; r < rows; r++) {
            String[] rowValues = scanner.nextLine().split(" ");
            for (int c = 0; c < cols; c++) {
                matrix[r][c] = Integer.parseInt(rowValues[c]);
            }
        }

        int[][] dpMatrix = generateReversedDPMatrix(matrix);
        Deque<Integer> path = reconstructPath(dpMatrix, matrix);

        System.out.println(dpMatrix[0][0]);
        for (int num : path) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
