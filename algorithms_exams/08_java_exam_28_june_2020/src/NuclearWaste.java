import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class NuclearWaste {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[] costsStr = scanner.nextLine().split(" ");
        int[] costs = new int[costsStr.length];
        for (int i = 0; i < costsStr.length; i++) {
            costs[i] = Integer.parseInt(costsStr[i]);
        }

        int flasksCount = Integer.parseInt(scanner.nextLine());
        int size = flasksCount + 1;

        int[] dp = new int[size];
        int[] prev = new int[size];

        for (int i = 1; i < size; i++) {
            dp[i] = Integer.MAX_VALUE;
            for (int j = 1; j <= i; j++) {
                if (j > costs.length) {
                    break;
                }
                int currentCost = dp[i - j] + costs[j - 1];
                if (currentCost < dp[i]) {
                    dp[i] = currentCost;
                    prev[i] = j;
                }
            }
        }

        System.out.println("Cost: " + dp[size - 1]);

        List<String> path = new ArrayList<>();
        int p = flasksCount;
        while (p > 0) {
            path.add(prev[p] + " => " + costs[prev[p] - 1]);
            p -= prev[p];
        }

        for (String step : path) {
            System.out.println(step);
        }
    }
}
