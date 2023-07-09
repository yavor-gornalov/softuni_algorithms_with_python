//https://judge.softuni.org/Contests/Practice/Index/4004#0

//This is a problem from Algorithms with Java course.
//Python to Java converter used for testing the code in judge system

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class BitcoinMiners {

    public static int calcBinomialCoefficient(int n, int k, Map<Pair, Integer> memo) {
        if (k < 1 || k >= n) {
            return 1;
        }

        Pair pair = new Pair(n, k);
        if (memo.containsKey(pair)) {
            return memo.get(pair);
        }

        int result = calcBinomialCoefficient(n - 1, k, memo) + calcBinomialCoefficient(n - 1, k - 1, memo);
        memo.put(pair, result);
        return result;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int transactionsCount = scanner.nextInt();
        int transactionsCouldBePicked = scanner.nextInt();
        scanner.close();

        System.out.println(calcBinomialCoefficient(transactionsCount, transactionsCouldBePicked, new HashMap<>()));
    }

    static class Pair {
        int n;
        int k;

        public Pair(int n, int k) {
            this.n = n;
            this.k = k;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Pair pair = (Pair) o;
            return n == pair.n && k == pair.k;
        }

        @Override
        public int hashCode() {
            int result = n;
            result = 31 * result + k;
            return result;
        }
    }
}
