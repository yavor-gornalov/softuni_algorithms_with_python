import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class AlphaDecay {
    public static List<List<String>> generateCombinations(int idx, String[] vect, String[] seq) {
        if (idx == vect.length) {
            List<String> combination = new ArrayList<>();
            Collections.addAll(combination, vect);
            List<List<String>> combinations = new ArrayList<>();
            combinations.add(combination);
            return combinations;
        }

        List<List<String>> combinations = new ArrayList<>();
        for (String el : seq) {
            boolean found = false;
            for (String v : vect) {
                if (v != null && v.equals(el)) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                vect[idx] = el;
                combinations.addAll(generateCombinations(idx + 1, vect, seq));
                vect[idx] = null;
            }
        }
        return combinations;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] nucleusSequence = scanner.nextLine().split(" ");
        int combinationsLength = Integer.parseInt(scanner.nextLine());

        String[] vect = new String[combinationsLength];
        List<List<String>> result = generateCombinations(0, vect, nucleusSequence);

        for (List<String> combination : result) {
            System.out.println(String.join(" ", combination));
        }
    }
}
