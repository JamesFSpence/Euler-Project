import java.io.IOException;
import java.util.List;

//Runtime Runtime: 29ms

public class Euler_Project_99 {

	public static void main(String[] args) throws IOException {
		long startTime = System.nanoTime();

		List<int[]> numExpPairs = Util.getNumberExponentPairs();
		double maxResult = 0;
		double result;
		int lineNumber = 1;
		int maxLine = 1;
		for (int[] pair: numExpPairs) {
			result = pair[1]*Math.log(pair[0]);
			if (result>maxResult) {
				maxLine = lineNumber;
				maxResult = result;
			}
			lineNumber++;
		}
		System.out.println(maxLine);

		long endTime   = System.nanoTime();
		long totalTime = endTime - startTime;
		System.out.println("\nRuntime: "+totalTime/1000000 + "ms");
	}
}
