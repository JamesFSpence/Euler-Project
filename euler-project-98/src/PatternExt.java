import java.util.Map;

public class PatternExt {
	public String pattern;
	public Map<String,String> letterToDigit;
	
	public PatternExt(String pattern, Map<String,String> letterToDigit) {
		this.pattern = pattern;
		this.letterToDigit = letterToDigit;
	}
	public String toString() {
		return pattern;
	}
}
