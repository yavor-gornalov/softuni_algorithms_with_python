import java.util.*;
import java.util.stream.Collectors;

public class TrainsProblem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Deque<Double> arrivalTimes = new ArrayDeque<>();
        String[] arrivalInputs = scanner.nextLine().split(" ");
        for (String arrivalInput : arrivalInputs) {
            arrivalTimes.add(Double.parseDouble(arrivalInput));
        }
        arrivalTimes = arrivalTimes.stream().sorted().collect(Collectors.toCollection(ArrayDeque::new));

        Deque<Double> departureTimes = new ArrayDeque<>();
        String[] departureInputs = scanner.nextLine().split(" ");
        for (String departureInput : departureInputs) {
            departureTimes.add(Double.parseDouble(departureInput));
        }
        departureTimes = departureTimes.stream().sorted().collect(Collectors.toCollection(ArrayDeque::new));

        int totalTrains = 0;
        int maxTrains = 0;

        while (!arrivalTimes.isEmpty() && !departureTimes.isEmpty()) {
            double currentArrivalTime = arrivalTimes.pollFirst();
            double currentDepartureTime = departureTimes.pollFirst();

            if (currentArrivalTime < currentDepartureTime) {
                departureTimes.addFirst(currentDepartureTime);
                totalTrains++;
            } else {
                arrivalTimes.addFirst(currentArrivalTime);
                totalTrains--;
            }

            maxTrains = Math.max(maxTrains, totalTrains);
        }

        System.out.println(maxTrains);
    }
}
