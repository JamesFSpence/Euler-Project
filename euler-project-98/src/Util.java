import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public abstract class Util {
	public static List<String> getWordList() throws IOException {
		BufferedReader objReader = null;
		List<String> wordList = new ArrayList<String>();
		try {
			String strCurrentLine;
			objReader = new BufferedReader(new FileReader("src/euler-project-98-text-file.txt"));
			while ((strCurrentLine = objReader.readLine()) != null) {
				for (String s: strCurrentLine.split(","))
				wordList.add((s.replace("\"","")).toUpperCase());
			}
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			objReader.close();
		}
		return wordList;
	}
	public static Map<String, Set<String>> findAnagramDictionary(List<String> wordList) {
		Map<String,Set<String>> anagramDict = new HashMap<>();
		Set<String> toRemove = new HashSet<>();
		for (String word:wordList) {
			String[] letterArray = word.split("");
			Arrays.sort(letterArray);
			StringBuilder sortedLettersBuilder = new StringBuilder();
			for (String str:letterArray) {
				sortedLettersBuilder.append(str);
			}
			String sortedLetters = sortedLettersBuilder.toString();
			if (anagramDict.containsKey(sortedLetters)) {
				anagramDict.get(sortedLetters).add(word);
				toRemove.remove(word);
			} else {
				Set<String> s = new HashSet<>();
				s.add(word);
				toRemove.add(sortedLetters);
				anagramDict.put(sortedLetters, s);
			}
		}
		for (String key : toRemove) {
			if (anagramDict.get(key).size() == 1) {
				anagramDict.remove(key);
			}
		}
		return anagramDict;
	}
	public static PatternExt createPatternKey(String word) {
		StringBuilder pattern = new StringBuilder();;
		String[] wordArray = word.split("");
		Map<String,String> letterToDigit = new HashMap<>();

		int nextDigit = 1;
		for (String c:wordArray) {
			if (letterToDigit.containsKey(c)) {
				pattern.append(letterToDigit.get(c));
			} else {
				pattern.append(Integer.toString(nextDigit));
				letterToDigit.put(c, Integer.toString(nextDigit));
				nextDigit++;
			}
		}
		PatternExt patternExt = new PatternExt(pattern.toString(),letterToDigit);
		return patternExt;
	}
	public static String usePatternKey(String word, Map<String,String> letterToDigit) {
		StringBuilder pattern = new StringBuilder();
		String[] wordArray = word.split("");
		for (String c:wordArray) {
			pattern.append(letterToDigit.get(c));
		}
		return pattern.toString();
	}
	public static Set<List<String>> getPatternList(Map<String, Set<String>> anagramDictionary) {
		Set<List<String>> patternList = new HashSet<>();
		boolean firstWord;
		String pattern = "";
		Map<String,String> letterToDigit = new HashMap<>();;
		for (String s:anagramDictionary.keySet()) {
			firstWord = true;
			List<String> patternSet = new ArrayList<>();
			Set<String> anagrams = anagramDictionary.get(s);
			for (String word:anagrams) {
				if (firstWord) {
					PatternExt p = createPatternKey(word);
					pattern = p.pattern;
					letterToDigit = p.letterToDigit;
					patternSet.add(pattern);
					firstWord = false;
				} else {
					patternSet.add(usePatternKey(word,letterToDigit));
				}
			}
			patternList.add(patternSet);
		}
		return patternList;
	}
	public static Set<Long> getSquaresFromPatternSet(List<String> patterns, Map<String, String> letterToDigit) {
		Set<Long> squareSet = new HashSet<>();
		for (int i = 1; i<patterns.size();i++) {
			String numString = "";
			String p = patterns.get(i);
			String[] pArray = p.split("");
			for (String c:pArray) {
				numString += getKey(c,letterToDigit);
			}
			Long num = Long.parseLong(numString);
			if ((isSquare(num))&&(num.toString().length() == p.length())) {
				squareSet.add(num);
			}
		}
		return squareSet;
	}
	private static boolean isSquare(Long num) {
		Long squareRoot = (long) Math.sqrt(num);
		if (squareRoot*squareRoot == num) {
			return true;
		}
		return false;
	}
	private static String getKey(String c, Map<String, String> letterToDigit) {
		for (String key:letterToDigit.keySet()) {
			if (letterToDigit.get(key).equals(c)) {
				return key;
			}
		}
		System.out.println("No key found!");
		return "";
	}	
}
