import java.util.*;

public class ContaminatedPath {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int size = Integer.parseInt(scanner.nextLine());

        int[][] grid = new int[size][size];
        for (int i = 0; i < size; i++) {
            String[] row = scanner.nextLine().split(" ");
            for (int j = 0; j < size; j++) {
                grid[i][j] = Integer.parseInt(row[j]);
            }
        }

        // Set abandoned cells to Integer.MIN_VALUE
        String[] abandonedCells = scanner.nextLine().split(" ");
        for (String cell : abandonedCells) {
            String[] indices = cell.split(",");
            int r = Integer.parseInt(indices[0]);
            int c = Integer.parseInt(indices[1]);
            grid[r][c] = Integer.MIN_VALUE;
        }

        int[][] dp = createDpMatrix(grid);

        Deque<String> result = reconstructPath(dp);

        System.out.println("Max total fertility: " + dp[size - 1][size - 1]);
        System.out.print("[");
        while (!result.isEmpty()) {
            System.out.print(result.removeFirst());
            if (!result.isEmpty()) {
                System.out.print(" ");
            }
        }
        System.out.println("]");
    }

    public static int[][] createDpMatrix(int[][] matrix) {
        int size = matrix.length;
        int[][] dpMatrix = new int[size][size];
        dpMatrix[0][0] = matrix[0][0];

        for (int idx = 1; idx < size; idx++) {
            dpMatrix[idx][0] = dpMatrix[idx - 1][0] + matrix[idx][0];
            dpMatrix[0][idx] = dpMatrix[0][idx - 1] + matrix[0][idx];
        }

        for (int r = 1; r < size; r++) {
            for (int c = 1; c < size; c++) {
                dpMatrix[r][c] = Math.max(dpMatrix[r - 1][c], dpMatrix[r][c - 1]) + matrix[r][c];
            }
        }

        return dpMatrix;
    }

    public static Deque<String> reconstructPath(int[][] dpMatrix) {
        int row = dpMatrix.length - 1;
        int col = dpMatrix[0].length - 1;
        Deque<String> path = new ArrayDeque<>();

        while (row > 0 && col > 0) {
            String cell = "(" + row + ", " + col + ")";
            path.addFirst(cell);
            if (dpMatrix[row - 1][col] > dpMatrix[row][col - 1]) {
                row--;
            } else {
                col--;
            }
        }

        for (int i = row; i > 0; i--) {
            String cell = "(" + i + ", 0)";
            path.addFirst(cell);
        }

        for (int j = col; j > 0; j--) {
            String cell = "(0, " + j + ")";
            path.addFirst(cell);
        }

        String cell = "(0, 0)";
        path.addFirst(cell);

        return path;
    }
}