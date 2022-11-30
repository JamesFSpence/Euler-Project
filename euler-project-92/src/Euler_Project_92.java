import java.util.HashSet;
import java.util.Set;

//Runtime: 1.6s

public class Euler_Project_92 {
	public static void main(String[] args) {
		long startTime = System.nanoTime();
		final int N = 10000000;
		int activeNum = 0;
		Set<Integer> goesTo89 = new HashSet<>();
		Set<Integer> goesTo1 = new HashSet<>();
		goesTo89.add(89);
		goesTo1.add(1);
		Set<Integer> inCurrentLoop = new HashSet<>();
		boolean terminated = false;
		for (int i = 1; i < N; i++) {
			activeNum = i;
			inCurrentLoop.clear();
			inCurrentLoop.add(i);
			if ((goesTo1.contains(i))||(goesTo89.contains(i))) {
				terminated = true;
			} else {
				terminated = false;
			}
			while (!terminated) {
				int squareDigitSum = 0;
				String stringInt = Integer.toString(activeNum);
				for (char c:stringInt.toCharArray()) {
					int digit = Character.getNumericValue(c);
					squareDigitSum += digit*digit;
				}
				if (goesTo89.contains(squareDigitSum)) {
					goesTo89.addAll(inCurrentLoop);
					terminated = true;
				} else if (goesTo1.contains(squareDigitSum)) {
					goesTo1.addAll(inCurrentLoop);
					terminated = true;
				} else {
					inCurrentLoop.add(squareDigitSum);
					activeNum = squareDigitSum;
				}
			}
		}
		System.out.println(goesTo89.size());
		long endTime   = System.nanoTime();
		long totalTime = endTime - startTime;
		System.out.println("\n"+totalTime/1000000);
	}
}
