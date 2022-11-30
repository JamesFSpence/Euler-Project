public class Euler_Project_97 {

//Runtime: 14ms
	
	public static void main(String[] args) {
		long startTime = System.nanoTime();
		
		long prod = 1L;
		long N = 1L;
		for (int j = 0; j<10; j++) {
			N*=10L;
		}
		for (long i = 0L; i < 7830457L;i++) {
			prod *= 2L;
			prod = prod%N;
		}
		prod *= 28433L;
		prod += 1;
		prod = prod%N;
		System.out.println(prod);
		
		long endTime   = System.nanoTime();
		long totalTime = endTime - startTime;
		System.out.println("\nRuntime: "+totalTime/1000000 + "ms");
	}

}
