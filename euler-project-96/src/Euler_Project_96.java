import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

//Runtime: 55ms

public class Euler_Project_96 {
	public static String[][] getSudokuList() throws IOException {
		int line = 9;
		int sNum = -1;
		BufferedReader objReader = null;
		String[][] sudokuList = new String[51][9];
		try {
			String strCurrentLine;
			objReader = new BufferedReader(new FileReader("src/euler-project-96-text-file.txt"));
			while ((strCurrentLine = objReader.readLine()) != null) {
				if (line == 9) {
					line = 0;
					sNum++;
					continue;
				}
				sudokuList[sNum][line] = strCurrentLine;
				line++;
			}
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			objReader.close();
		}
		return sudokuList;
	}
	public static Sudoku formatSudoku(String[] sudoku) {
		Sudoku formattedSudoku = new Sudoku();
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				formattedSudoku.setValue(i, j, sudoku[i].charAt(j)-48);
			}
		}
		//System.out.println(Arrays.deepToString(formattedSudoku));
		return formattedSudoku;
	}
	
	public static void main(String[] args) throws IOException{
		long startTime = System.nanoTime();
		
		int totalSum = 0;
		String[][] sudokuList = getSudokuList();
		for (int i = 0; i<50; i++) {
			Sudoku currentSudoku = formatSudoku(sudokuList[i]);
			totalSum += currentSudoku.solveSudoku(0);
			System.out.println(currentSudoku.valuesToString());
		}
		System.out.println(totalSum);
		

		long endTime   = System.nanoTime();
		long totalTime = endTime - startTime;
		System.out.println("\nRuntime: "+totalTime/1000000 + "ms");
	}
}
