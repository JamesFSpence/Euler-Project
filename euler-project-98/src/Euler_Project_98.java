import java.io.IOException;
import java.util.List;
import java.util.Map;
import java.util.Set;

//Runtime: 313ms


public class Euler_Project_98 {

	public static void main(String[] args) throws IOException {
		long startTime = System.nanoTime();
		
		List<String> wordList = Util.getWordList();
		Map<String,Set<String>> anagramDictionary = Util.findAnagramDictionary(wordList);
		Set<List<String>> patternList = Util.getPatternList(anagramDictionary);
		int maxI = 100000;
		long maxSquare = 0;
		for (long i = 1; i<maxI;i++) {
			long squared = i*i;
			PatternExt p = Util.createPatternKey(Long.toString(squared));
			String squaredPattern = p.pattern;
			Map<String,String> letterToDigit = p.letterToDigit;
			for (List<String> patterns:patternList) {
				if (squaredPattern.equals(patterns.get(0))) {
					Set<Long> squares = Util.getSquaresFromPatternSet(patterns,letterToDigit);
					if (squares.size()>0) {
						squares.add(squared);
						for (long num:squares) {
							if (maxSquare<num) {
								maxSquare = num;
							}
						}
					}
				}
			}
		}
		System.out.print(maxSquare);

		long endTime   = System.nanoTime();
		long totalTime = endTime - startTime;
		System.out.println("\nRuntime: "+totalTime/1000000 + "ms");
	}
}
