import java.math.BigInteger;

//Runtime: 1ms

public class Euler_Project_100 {
	public static boolean checkIfWorks(BigInteger numerator, BigInteger denominator) throws InterruptedException {
		BigInteger numerSquared = numerator.multiply(numerator);
		BigInteger twoDenomSquared = denominator.multiply(denominator).multiply(
												BigInteger.valueOf(2));
		if ((numerSquared.subtract(twoDenomSquared)).longValue() == -1) {
			return true;
		}
		return false;
	}
	public static void main(String[] args) throws InterruptedException {
		long startTime = System.nanoTime();
	
		//Method: find approximations to root 2 and work out answer from that
		BigInteger numerator = BigInteger.valueOf(1);
		BigInteger denominator = BigInteger.valueOf(1);
		BigInteger numerComparator = BigInteger.valueOf(2*(long)1E12 - 1);
		//numerator must be bigger than ^^this^^ to get totalDiscs above 1E12
		
		boolean keepGoing = true;
		boolean oddDenom = false;
		while (keepGoing) {
			numerator = numerator.add(denominator.add(denominator));
			denominator = numerator.subtract(denominator);
			
			if (oddDenom == true) {
				//we don't get an integer value for numBlueDiscs and totalDiscs
				//unless both numerator and denominator are odd
				if (numerator.compareTo(numerComparator) >= 0) {
					if (checkIfWorks(numerator, denominator)) {
						BigInteger numBlueDiscs = denominator.add(
													BigInteger.valueOf(1)).divide(
														BigInteger.valueOf(2));
						System.out.print(numBlueDiscs);
						keepGoing = false;
					}
				}
				oddDenom = false;
			} else {
				oddDenom = true;
			}
		}
		
		long endTime   = System.nanoTime();
		long totalTime = endTime - startTime;
		System.out.println("\nRuntime: "+totalTime/1000000 + "ms");
	}
}
