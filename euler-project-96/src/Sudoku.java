import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Sudoku {
	public int[][] values;
	public List<Set<Integer>> possibilities;
	
	public Sudoku(int[][] values, ArrayList<Set<Integer>> possibilities) {
		this.values = values;
		this.possibilities = possibilities;
	}
	public Sudoku() {
		values = new int[9][9];
		List<Set<Integer>> defaultArray = new ArrayList<>();
		for (int i = 0; i<81; i++) {
			defaultArray.add(new HashSet<Integer>());
		}
		possibilities = defaultArray;
	}
	public void setValues(int[][] values) {
		this.values = values;
	}
	public void setPossibilities(ArrayList<Set<Integer>> possibilities) {
		this.possibilities = possibilities;
	}
	public void setValue(int i, int j, int value) {
		values[i][j] = value;
	}
	public void setValueProper (int i, int j, int value) {
		values[i][j] = value;
		Set<Integer> tempSet = new HashSet<>();
		tempSet.add(value);
		
		for (int index = 0; index<9; index++) {
			this.getPossibility(i,index).remove(value);
			this.getPossibility(index,j).remove(value);
		}
		int[][] boxIndices = this.getBoxIndices(i,j); 
		for(int a = 0; a<3; a++) {
			for (int b = 0; b<3; b++) {
				this.getPossibility(i + boxIndices[0][a], j + boxIndices[1][b]).remove(value);
			}
		}
		this.setPossibility(i, j,tempSet);
	}
	public void setPossibility(int i, int j, Set<Integer> possibility) {
		possibilities.set(9*i + j,possibility);
	}
	public int getValue(int i, int j) {
		return values[i][j];
	}
	public Set<Integer> getPossibility(int i,int j) {
		return possibilities.get(9*i + j);
	}
	
	@Override
	public String toString() {
		
		StringBuilder s = new StringBuilder("Values: \n");
		s.append(this.valuesToString());
		s.append("\nPossibilities: \n");
		s.append(possibilitiesToString());
		return s.toString();
	}
	public String valuesToString() {
		StringBuilder s = new StringBuilder();
		for (int i = 0; i<9; i++) {
			s.append(Arrays.toString(values[i]) + "\n");
		}
		return s.toString();
	}
	public String possibilitiesToString() {
		StringBuilder s = new StringBuilder();
		int count;
		for (int i = 0; i<9; i++) {
			s.append("\n[");
			for (int j = 0; j<9; j++) {
				if (j!=0) s.append(", ");
				s.append("[");
				count = 0;
				for (int x: this.getPossibility(i,j)) {
					if (count != 0) s.append(", "); 
					s.append(x);
					count++;
				}
				s.append("]");
			}
			s.append("]");
		}
		s.append("\n");
		return s.toString();
	}
	
	public void printPossibilities() {
		System.out.print(this.possibilitiesToString());
	}
	
	public void setInitialPossibilities() {
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				if (this.getValue(i,j) != 0) {
					this.getPossibility(i,j).add(this.getValue(i,j));
					continue;
				}
				Set<Integer> temp = new HashSet<>();
				for (int num = 1; num<=9; num++) {
					if (this.canBe(i,j,num)) {
						temp.add(num);
					}
				} 
				this.setPossibility(i, j, temp);
			}
		}
	}
	
	public boolean canBe(int i, int j, int num) {
		for (int index = 0; index<9; index++) {
			if ((this.getValue(i, index) == num)||(this.getValue(index, j) == num)) {
				return false;
			}
		}
		int[][] boxIndices = this.getBoxIndices(i,j);
		for(int a = 0; a<3; a++) {
			for (int b = 0; b<3; b++) {
				if (this.getValue(i + boxIndices[0][a], j + boxIndices[1][b]) == num) {
					return false;
				}
			}
		}
		return true; // TODO
	}
	
	public int[][] getBoxIndices(int i, int j) {
		int[] iIndices = {0,1,2};
		int[] jIndices = {0,1,2};
		if (i%3 == 1) {
			iIndices[2] = -1;
		} else if (i%3 == 2) {
			iIndices[1] = -2;
			iIndices[2] = -1;
		}
		if (j%3 == 1) {
			jIndices[2] = -1;
		} else if (j%3 == 2) {
			jIndices[1] = -2;
			jIndices[2] = -1;
		}
		int[][] boxIndices = {iIndices,jIndices};
		return boxIndices;
	}
	public Sudoku updatePossibility(int i, int j) {
		for (int num = 1; num<=9; num++) {
			if (!(this.canBe(i,j,num))) {
				this.getPossibility(i,j).remove(num);
			}
		}
		return this;
	}
	public static int[] getStartingIndex(int i) {
		int[] coords = {(i%3)*3,((i/3)%3)*3};
		return coords;
	}
	public int solveSudoku(int depth) {
		this.setInitialPossibilities();
		boolean solved = false;
		boolean seenChange = false;
		int answer = 0;
		while (!solved) {
			seenChange = false;
			for (int i = 0;i<9; i++) {
				for (int j = 0; j<9; j++) {
					if (this.getValue(i, j) == 0) {
						if (this.getPossibility(i,j).size() == 1) {
							for (int value : this.getPossibility(i,j)) {
								this.setValueProper(i,j,value);
								seenChange = true;
							}
						} else if (this.getPossibility(i,j).size() == 0) {
							return -1;
						}
					}
				}
				int count;
				int activeIndex = 0;
				int[] coords = getStartingIndex(i);
				for (int value = 1; value<10; value++) {
					count = 0;
					for (int index = 0; index < 9; index++) { //checking where 'value' can fit in row 'i'
						if (this.getPossibility(i,index).contains(value)) {
							count++;
							activeIndex = index;
						}
					}
					if ((count == 1)&&(this.getValue(i,activeIndex) == 0)) {
						this.setValueProper(i,activeIndex,value);
						seenChange = true;
					}
					count = 0;
					for (int index = 0; index < 9; index++) { //checking where 'value' can fit in column 'i' 
						if (this.getPossibility(index,i).contains(value)) {
							count++;
							activeIndex = index;
						}
					}
					if ((count == 1)&&(this.getValue(activeIndex, i) == 0)) {
						this.setValueProper(activeIndex,i,value);
						seenChange = true;
					}
					count = 0;
					int[][] b = {{0,0},{0,1},{0,2},{1,0},{1,1},{1,2},{2,0},{2,1},{2,2}}; 
					for (int index = 0;index<9;index++) { //checking where 'value' can fit in box 'i' 
						if (this.getPossibility(coords[0] + b[index][0],coords[1] + b[index][1]).contains(value)) {
							count++;
							activeIndex = index;
						}
					}
					if ((count == 1)&&(this.getValue(coords[0] + b[activeIndex][0],coords[1] + b[activeIndex][1]) == 0)) {
						
						this.setValueProper(coords[0] + b[activeIndex][0],coords[1] + b[activeIndex][1],value);
						seenChange = true;
					}
				}
			}	
			if (!seenChange) {
				solved = true;
				for (Set<Integer> possibility : possibilities) {
					if (possibility.size() != 1) {
						solved = false;
						break;
					}
				}
				break;
			}
		}
		if (solved) {
			StringBuilder answerString = new StringBuilder();
			for (int i = 0; i<3; i++) {
				answerString = answerString.append(this.getValue(0, i));
			}
			return Integer.parseInt(answerString.toString());
		} else {
			if (depth == 2) { //May need to increase for harder to solve problems
				return 0;
			}
			
			for (Set<Integer> possibility : possibilities) {
				if (possibility.size() != 1) {
					int indOfPoss = possibilities.indexOf(possibility);
					int m = indOfPoss/9;
					int n = indOfPoss%9;
					for (int p : possibility) {
						Sudoku sudokuCopy = new Sudoku();
						for (int i = 0; i<9; i++) {
							for (int j = 0; j<9; j++) {
								sudokuCopy.setValue(i,j,this.getValue(i, j));
							}
						}
						sudokuCopy.setValue(m,n,p);
						int tempAns = sudokuCopy.solveSudoku(depth+1);
						if (tempAns > 0) {
							this.values = sudokuCopy.values;
							this.possibilities = sudokuCopy.possibilities;
							return tempAns;
						}
					}
				}
			}
		}
		return answer;
	}
}
