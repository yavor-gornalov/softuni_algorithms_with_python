import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Paths {
    public static void dfs(int node, int target, List<List<Integer>> graph, boolean[] visited, List<Integer> path) {
        visited[node] = true;
        path.add(node);

        if (node == target) {
            for (int i = 0; i < path.size(); i++) {
                System.out.print(path.get(i));
                if (i < path.size() - 1) {
                    System.out.print(" ");
                }
            }
            System.out.println();
        } else {
            for (int child : graph.get(node)) {
                if (visited[child]) {
                    continue;
                }
                dfs(child, target, graph, visited, path);
            }
        }

        path.remove(path.size() - 1);
        visited[node] = false;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int nodes = Integer.parseInt(scanner.nextLine());

        List<List<Integer>> graph = new ArrayList<>();
        for (int node = 0; node < nodes; node++) {
            String[] childrenStr = scanner.nextLine().split(" ");
            List<Integer> children = new ArrayList<>();
            for (String childStr : childrenStr) {
                if (!childStr.isEmpty()) {  // Skip empty strings
                    children.add(Integer.parseInt(childStr));
                }
            }
            graph.add(children);
        }

        for (int startNode = 0; startNode < nodes - 1; startNode++) {
            boolean[] visited = new boolean[nodes];
            List<Integer> path = new ArrayList<>();
            dfs(startNode, nodes - 1, graph, visited, path);
        }
    }
}
