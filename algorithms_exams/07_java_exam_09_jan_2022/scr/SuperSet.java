import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class SuperSet {
    public static void generateSubsets(int[] nums, List<Integer> solution, List<List<Integer>> result) {
        result.add(new ArrayList<>(solution));
        for (int i = 0; i < nums.length; i++) {
            solution.add(nums[i]);
            generateSubsets(Arrays.copyOfRange(nums, i + 1, nums.length), solution, result);
            solution.remove(solution.size() - 1);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] numbersStr = scanner.nextLine().split(", ");
        int[] numbers = new int[numbersStr.length];
        for (int i = 0; i < numbersStr.length; i++) {
            numbers[i] = Integer.parseInt(numbersStr[i]);
        }

        List<List<Integer>> result = new ArrayList<>();
        generateSubsets(numbers, new ArrayList<>(), result);

        result.sort((a, b) -> Integer.compare(a.size(), b.size()));
        for (List<Integer> subset : result) {
            for (int i = 0; i < subset.size(); i++) {
                System.out.print(subset.get(i));
                if (i < subset.size() - 1) {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}
