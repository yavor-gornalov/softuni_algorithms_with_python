import java.util.*;

public class PathFinder {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int nodes = Integer.parseInt(scanner.nextLine());

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < nodes; i++) {
            graph.add(new ArrayList<>());
        }

        for (int node = 0; node < nodes; node++) {
            String[] childrenInput = scanner.nextLine().split(" ");
            if (childrenInput.length > 0 && !childrenInput[0].equals("")) {
                List<Integer> children = new ArrayList<>();
                for (String child : childrenInput) {
                    if (!child.equals("")) {
                        children.add(Integer.parseInt(child));
                    }
                }
                graph.set(node, children);
            }
        }

        int pathsCount = Integer.parseInt(scanner.nextLine());
        List<List<Integer>> possiblePaths = new ArrayList<>();
        for (int i = 0; i < pathsCount; i++) {
            String[] pathInput = scanner.nextLine().split(" ");
            List<Integer> currentPath = new ArrayList<>();
            for (String node : pathInput) {
                if (!node.equals("")) {
                    currentPath.add(Integer.parseInt(node));
                }
            }
            possiblePaths.add(currentPath);
        }

        for (List<Integer> currentPath : possiblePaths) {
            boolean isPathPossible = pathFinder(currentPath, graph);
            System.out.println(isPathPossible ? "yes" : "no");
        }
    }

    public static boolean pathFinder(List<Integer> path, List<List<Integer>> graph) {
        boolean pathExists = true;
        for (int idx = 1; idx < path.size(); idx++) {
            int currentParent = path.get(idx - 1);
            int currentChild = path.get(idx);
            if (!graph.get(currentParent).contains(currentChild)) {
                pathExists = false;
                break;
            }
        }
        return pathExists;
    }
}
