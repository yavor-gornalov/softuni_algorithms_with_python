import java.util.*;

public class CryptoExchange {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int edgesCount = Integer.parseInt(scanner.nextLine());

        Map<String, List<String>> graph = new HashMap<>();

        for (int i = 0; i < edgesCount; i++) {
            String[] currencies = scanner.nextLine().split(" - ");
            String currencyFrom = currencies[0];
            String currencyTo = currencies[1];

            graph.putIfAbsent(currencyFrom, new ArrayList<>());
            graph.putIfAbsent(currencyTo, new ArrayList<>());

            graph.get(currencyFrom).add(currencyTo);
            graph.get(currencyTo).add(currencyFrom);
        }

        String[] sourceTargetCurrencies = scanner.nextLine().split(" -> ");
        String sourceCurrency = sourceTargetCurrencies[0];
        String targetCurrency = sourceTargetCurrencies[1];

        int result = calculateCurrencySwaps(sourceCurrency, targetCurrency, graph);

        System.out.println(result);
    }

    public static int calculateCurrencySwaps(String startNode, String targetNode, Map<String, List<String>> currentGraph) {
        Set<String> visited = new HashSet<>();
        Map<String, String> parent = new HashMap<>();

        Queue<String> queue = new LinkedList<>();
        queue.add(startNode);
        visited.add(startNode);

        // BFS
        while (!queue.isEmpty()) {
            String node = queue.poll();
            if (node.equals(targetNode)) {
                break;
            }
            for (String child : currentGraph.get(node)) {
                if (!visited.contains(child)) {
                    visited.add(child);
                    parent.put(child, node);
                    queue.add(child);
                }
            }
        }

        if (!parent.containsKey(targetNode)) {
            return -1;
        }

        List<String> path = new ArrayList<>();
        String node = targetNode;
        while (node != null) {
            path.add(node);
            node = parent.get(node);
        }

        return path.size() - 1;
    }
}
