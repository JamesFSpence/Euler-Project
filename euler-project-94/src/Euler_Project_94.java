import java.math.BigInteger;

//Runtime: 25s

public class Euler_Project_94 {

	public static void main(String[] args) {
		//x-x-(x+1) is an almost equilateral triangle iff n(3n+2) is a perfect square, where x = 2n + 1.
		//Similarly, x-x-(x-1) is an almost equilateral triangle iff n(3n+4) is a perfect square.
		long startTime = System.nanoTime();
		
		int maxPerimeter = 1000000000;
		long totalPerimeter = 0;
		double sqrtThreeLower = 1.7320508075; //slightly less than root 3
		double sqrtThreeUpper = 1.7320508076; //slightly bigger than root 3
		double lowerBound = sqrtThreeLower/3;
		double upperBound = 8*sqrtThreeUpper/3;
		BigInteger m;
		BigInteger bigH;
		BigInteger target1;
		BigInteger target2;
		BigInteger squared;
		for (int n = 1; n<=(maxPerimeter-4)/6; n++) {
			m = BigInteger.valueOf(n);
			target1 = m.multiply(BigInteger.valueOf(2).add(m.multiply(BigInteger.valueOf(3))));
			target2 = BigInteger.valueOf(1).add(m.multiply(BigInteger.valueOf(4).add(m.multiply(BigInteger.valueOf(3)))));
			for (long h = (long)lowerBound+1; h<=(long)upperBound; h++) {
				bigH = BigInteger.valueOf(h);
				squared = bigH.multiply(bigH);
				if (squared.equals(target1)) {
					totalPerimeter += 6*n + 4;
					System.out.print("Tall triangle found: ");
					System.out.println((2*n+1) + "-" + (2*n+1) + "-" + (2*n+2));
				} else if (squared.equals(target2)) {
					totalPerimeter += 6*n + 2;
					System.out.print("Short triangle found: ");
					System.out.println((2*n+1) + "-" + (2*n+1) + "-" + 2*n);
				}
			}
			lowerBound += sqrtThreeLower;
			upperBound += sqrtThreeUpper;
			
		}
		System.out.println(totalPerimeter);

		long endTime   = System.nanoTime();
		long totalTime = endTime - startTime;
		System.out.println("\nRuntime: "+totalTime/1000000 + "ms");
	}
}