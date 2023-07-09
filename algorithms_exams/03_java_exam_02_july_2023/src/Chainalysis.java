//https://judge.softuni.org/Contests/Practice/Index/4004#1

//This is a problem from Algorithms with Java course.
//Python to Java converter used for testing the code in judge system

import java.util.*;

class Edge implements Comparable<Edge> {
    String first;
    String second;
    int amount;

    public Edge(String first, String second, int amount) {
        this.first = first;
        this.second = second;
        this.amount = amount;
    }

    @Override
    public int compareTo(Edge other) {
        return Integer.compare(this.amount, other.amount);
    }
}

public class Chainalysis {

    public static int prim(String node, Map<String, List<Edge>> graph, Set<String> forest) {
        if (forest.contains(node)) {
            return 0;
        }

        forest.add(node);
        Queue<Edge> pq = new PriorityQueue<>();

        pq.addAll(graph.get(node));

        int totalTreesInForest = 0;
        while (!pq.isEmpty()) {
            Edge minEdge = pq.poll();
            String nonTreeNode = null;

            if (forest.contains(minEdge.first) && !forest.contains(minEdge.second)) {
                nonTreeNode = minEdge.second;
            } else if (!forest.contains(minEdge.first) && forest.contains(minEdge.second)) {
                nonTreeNode = minEdge.first;
            }

            if (nonTreeNode == null) {
                continue;
            }

            forest.add(nonTreeNode);

            pq.addAll(graph.get(nonTreeNode));

        }

        return 1;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int edges = Integer.parseInt(scanner.nextLine());

        Map<String, List<Edge>> graph = new HashMap<>();
        Set<String> forest = new HashSet<>();

        for (int i = 0; i < edges; i++) {
            String[] inputs = scanner.nextLine().split(" ");
            String first = inputs[0];
            String second = inputs[1];
            int amount = Integer.parseInt(inputs[2]);

            Edge edge = new Edge(first, second, amount);

            if (!graph.containsKey(first)) {
                graph.put(first, new ArrayList<>());
            }
            if (!graph.containsKey(second)) {
                graph.put(second, new ArrayList<>());
            }

            graph.get(first).add(edge);
            graph.get(second).add(edge);
        }

        int totalTreesInForest = 0;
        for (String node : graph.keySet()) {
            totalTreesInForest += prim(node, graph, forest);
        }

        System.out.println(totalTreesInForest);
    }
}
