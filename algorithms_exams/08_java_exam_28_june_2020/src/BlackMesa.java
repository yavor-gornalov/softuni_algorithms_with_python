import java.util.*;

public class BlackMesa {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int nodes = scanner.nextInt();
        int edges = scanner.nextInt();

        int[][] graph = constructGraph(nodes, edges, scanner);

        int startNode = scanner.nextInt();
        int targetNode = scanner.nextInt();

        scanner.close();

        graphShortestPath(startNode, targetNode, graph);
    }

    private static int[][] constructGraph(int nodes, int edges, Scanner scanner) {
        int[][] graph = new int[nodes + 1][nodes + 1];
        for (int i = 0; i < edges; i++) {
            int source = scanner.nextInt();
            int destination = scanner.nextInt();
            graph[source][destination] = 1;
        }

        return graph;
    }

    private static void graphShortestPath(int start, int target, int[][] graph) {
        boolean[] visited = new boolean[graph.length];
        ArrayList<Integer> path = new ArrayList<>();
        Deque<Integer> queue = new ArrayDeque<>();

        queue.add(start);
        boolean targetFound = false;
        // BFS
        while (!queue.isEmpty()) {
            int node = queue.poll();
            visited[node] = true;
            if (!targetFound) {
                path.add(node);
                targetFound = node == target;
            }

            for (int i = 0; i < graph[node].length; i++) {
                if (graph[node][i] != 0 && !visited[i]) {
                    visited[i] = true;
                    queue.offer(i);
                }
            }
        }

        for (int node : path) {
            System.out.print(node + " ");
        }
        System.out.println();

        for (int i = 1; i < visited.length; i++) {
            if (!visited[i]) {
                System.out.print(i + " ");
            }
        }
    }
}
