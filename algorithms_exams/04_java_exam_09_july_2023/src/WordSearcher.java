import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class WordSearcher {
    private static final int[][] directions = {
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

        char[][] grid = new char[rows][cols];
        for (int i = 0; i < rows; i++) {
            String row = scanner.nextLine();
            for (int j = 0; j < cols; j++) {
                grid[i][j] = row.charAt(j);
            }
        }

        String[] words = scanner.nextLine().split(" ");
        Set<String> uniqueWords = new HashSet<>();

        for (String word : words) {
            for (int r = 0; r < rows; r++) {
                for (int c = 0; c < cols; c++) {
                    StringBuilder currentWord = new StringBuilder();
                    if (findWordInMatrix(r, c, 0, currentWord, word.toCharArray(), grid)) {
                        uniqueWords.add(currentWord.toString());
                    }
                }
            }
        }

        for (String uniqueWord : uniqueWords) {
            System.out.println(uniqueWord);
        }
    }

    public static boolean findWordInMatrix(int row, int col, int idx, StringBuilder currentWord, char[] target, char[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;

        if (row < 0 || col < 0 || row >= rows || col >= cols) {
            return false;
        }

        if (idx >= target.length) {
            return currentWord.toString().equals(new String(target));
        }

        if (matrix[row][col] != target[idx]) {
            return false;
        }

        currentWord.append(matrix[row][col]);

        for (int[] direction : directions) {
            int newRow = row + direction[0];
            int newCol = col + direction[1];
            if (findWordInMatrix(newRow, newCol, idx + 1, currentWord, target, matrix)) {
                return true;
            }
        }

        currentWord.deleteCharAt(currentWord.length() - 1);
        return false;
    }
}
