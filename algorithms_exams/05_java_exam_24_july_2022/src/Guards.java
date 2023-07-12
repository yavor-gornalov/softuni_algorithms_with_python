import java.util.*;

public class Guards {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int nodes = Integer.parseInt(scanner.nextLine()) + 1;
        int edges = Integer.parseInt(scanner.nextLine());

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < nodes; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < edges; i++) {
            String[] input = scanner.nextLine().split(" ");
            int source = Integer.parseInt(input[0]);
            int destination = Integer.parseInt(input[1]);
            graph.get(source).add(destination);
        }

        int startNode = Integer.parseInt(scanner.nextLine());

        boolean[] visited = constructVisited(startNode, graph);

        List<Integer> result = getUnreachableNodes(visited);

        for (int node : result) {
            System.out.print(node + " ");
        }
    }

    public static boolean[] constructVisited(int startNode, List<List<Integer>> graph) {
        int nodes = graph.size();
        boolean[] visited = new boolean[nodes];

        Queue<Integer> queue = new LinkedList<>();
        queue.add(startNode);
        visited[startNode] = true;

        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int child : graph.get(node)) {
                if (!visited[child]) {
                    visited[child] = true;
                    queue.add(child);
                }
            }
        }

        return visited;
    }

    public static List<Integer> getUnreachableNodes(boolean[] visited) {
        List<Integer> unreachableNodes = new ArrayList<>();
        for (int node = 1; node < visited.length; node++) {
            if (!visited[node]) {
                unreachableNodes.add(node);
            }
        }

        return unreachableNodes;
    }
}
