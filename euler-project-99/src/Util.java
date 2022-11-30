import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public abstract class Util {
	public static List<int[]> getNumberExponentPairs()  throws IOException {
		
		List<int[]> numExpPairs = new ArrayList<>();
		BufferedReader objReader = null;
		try {
			String strCurrentLine;
			objReader = new BufferedReader(new FileReader("src/euler-project-99-text-file.txt"));
			while ((strCurrentLine = objReader.readLine()) != null) {
				int[] intArray = new int[2];
				String[] numExpArray = strCurrentLine.split(",");
				intArray[0] = Integer.parseInt(numExpArray[0]);
				intArray[1] = Integer.parseInt(numExpArray[1]);
				numExpPairs.add(intArray);
			}
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			objReader.close();
		}
		return numExpPairs;
	}
}
