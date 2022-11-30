import java.util.HashSet;
import java.util.Set;

//Runtime: 18ms

public class Euler_project_93 {
	public static Set<Integer> findPossibleResults(double[] usedNums, Set<Integer> possibleResults) { 
		/*
		* Works by choosing pairs of numbers from a set, usedNums, carrying out arithmetic operations on them, 
		/ then using the results to create a collection of new sets with the results plus the remaining numbers in usedNums.
		*/
		int l = usedNums.length;
		int index;
		if (l==1) {
			if (usedNums[0]%1 == 0) { //only add the result to possibleResults if it is and integer
				possibleResults.add((int)usedNums[0]);
			}
			return possibleResults;
		}
		double[] dregs = new double[l-1];
		for (int i = 0; i < l-1; i++) {
			for (int j = i+1; j < l; j++) {
				index = 0;
				for (int n = 0; n < l; n++) {
					if ((n!=i)&&(n!=j)) { //creating dregs using leftover numbers
						dregs[index] = usedNums[n];
						index++;
					}
				}
				for (double k : doArithmetic(usedNums[i],usedNums[j])) { //iterate over all
					dregs[l-2] = k; //adding to dregs the number produced by operating on i and j
					findPossibleResults(dregs,possibleResults);
				}
				
			}
		}
		return possibleResults;		
	}
	
	public static double[] doArithmetic(double i, double j) { //Finds all operations on two numbers i and j
		double max;
		double min;
		double[] answers;
		if (i>j) {
			max = i;
			min = j;
		} else {
			max = j;
			min = i;
		}
		if (max == 0) {
			answers = new double[1];
			return answers;
		}
		else if (min == 0) {
			answers = new double[4];
		} else {
			answers = new double[5];
			answers[4] = max/min;
		}
		answers[0] = max + min;
		answers[1] = max - min;
		answers[2] = max*min;
		answers[3] = min/max;
		return answers;
	}
	
	public static void main(String[] args) {
		long startTime = System.nanoTime();
		
		Set<Integer> possibleResults = new HashSet<>();
		double[] usedNums = new double[4];
		int result;
		int maxResult = 1;
		int[] maxChoices = new int[4];
		int maxN = 9;
		for (int a = 1; a<=maxN; a++) {
			for (int b = a+1; b<=maxN; b++) {
				for (int c = b+1; c<=maxN; c++) {
					for (int d = c+1; d<=maxN; d++) {
						
						result = 1;
						usedNums[0] = a;
						usedNums[1] = b;
						usedNums[2] = c;
						usedNums[3] = d;
						possibleResults.clear();
						possibleResults = findPossibleResults(usedNums,possibleResults);
						while (possibleResults.contains(result)) {
							result++;
						}
						result--;
						if (result > maxResult) {
							maxResult = result;
							maxChoices[0] = a;
							maxChoices[1] = b;
							maxChoices[2] = c;
							maxChoices[3] = d;
						}
					}
				}
			}
		}
		for (int i : maxChoices) {
				System.out.print(i+ ", ");
				
		}
		System.out.println("create consecutive numbers up to: " + maxResult);
		
		long endTime   = System.nanoTime();
		long totalTime = endTime - startTime;
		System.out.println("\nRuntime: "+totalTime/1000000 + "ms");
	}

}
