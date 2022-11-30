import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

//Runtime: 13s

public class Euler_Project_95 {
	public static int[] doLoop(int n, Set<Integer> processed,int maxLoop, int answer) {
		int currentNum = n;
		int lengthAmicableChain;
		int size;
		int index;
		int min;
		int[] answerArray = {answer, maxLoop};
		boolean goodLoop = true;
		List<Integer> currentLoop = new ArrayList<>();

		while (!(currentLoop.contains(currentNum))) {
			if (processed.contains(currentNum)) {
				processed.addAll(currentLoop);
				return answerArray;
			}
			currentLoop.add(currentNum);
			currentNum = findFactorSum(currentNum);
			if (currentNum > 1000000) {
				goodLoop = true;
			}
		}
		if (goodLoop) {
			processed.addAll(currentLoop);
			size = currentLoop.size();
			index = currentLoop.indexOf(currentNum);
			lengthAmicableChain = size - index;
			if (lengthAmicableChain > maxLoop) {
				 answerArray[1] = lengthAmicableChain;
				 min = currentLoop.get(size-1);
				 for (int j = index; j < size;j++) {
					 if (currentLoop.get(j) < min) {
						 min = currentLoop.get(j);
					 }
				 }
				 answerArray[0] = min;
			}
		}
		return answerArray;
	}
	public static int findFactorSum(int currentNum) {
		int factorSum = 1;
		for (int i = 2; i <= Math.sqrt(currentNum); i++) {
			if (currentNum%i == 0) {
				factorSum += i;
				factorSum += currentNum/i;
			}
		}
		return factorSum;
	}
		
	public static void main(String[] args) {
		long startTime = System.nanoTime();
		
		int[] answerArray = new int[2];
		int maxN = 1000000;
		int answer = 0;
		int maxLoop = 1;
		Set<Integer> processed = new HashSet<>();
		processed.add(1);
		for (int n = 2; n<maxN; n++) {
			answerArray = doLoop(n,processed,maxLoop, answer);
			answer = answerArray[0];
			maxLoop = answerArray[1];
		}
		System.out.println(Arrays.toString(answerArray));

		
		
		
		long endTime   = System.nanoTime();
		long totalTime = endTime - startTime;
		System.out.println("\nRuntime: "+totalTime/1000000 + "ms");
	}
}
