import java.util.*;

public class TBC {
    private static final int[][] DIRECTIONS = {
            {-1, 0},  // UP
            {-1, 1},  // UP RIGHT
            {0, 1},   // RIGHT
            {1, 1},   // DOWN RIGHT
            {1, 0},   // DOWN
            {1, -1},  // DOWN LEFT
            {0, -1},  // LEFT
            {-1, -1}  // UP LEFT
    };

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int rows = Integer.parseInt(scanner.nextLine());
        int cols = Integer.parseInt(scanner.nextLine());

        char[][] cityMap = new char[rows][cols];
        boolean[][] visited = new boolean[rows][cols];

        for (int i = 0; i < rows; i++) {
            String line = scanner.nextLine();
            for (int j = 0; j < cols; j++) {
                cityMap[i][j] = line.charAt(j);
            }
        }

        int result = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (cityMap[i][j] != 't') {
                    continue;
                }
                if (visited[i][j]) {
                    continue;
                }
                result += connectedTunnels(i, j, cityMap, visited);
            }
        }

        System.out.println(result);
    }

    public static int connectedTunnels(int row, int col, char[][] matrix, boolean[][] visited) {
        if (row < 0 || row >= matrix.length || col < 0 || col >= matrix[0].length) {
            return 0;
        }
        if (matrix[row][col] != 't') {
            return 0;
        }
        if (visited[row][col]) {
            return 0;
        }

        visited[row][col] = true;

        for (int[] dir : DIRECTIONS) {
            connectedTunnels(row + dir[0], col + dir[1], matrix, visited);
        }

        return 1;
    }
}
