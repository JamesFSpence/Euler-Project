import java.util.ArrayList;
import java.util.List;

//Runtime: 19ms

public class Euler_Project_91 {
	
	public static int GetNumOfSolutions(int x1, int y1, int x2, int y2, int rootedDeterminant, int gridSize) {
		int delta = 0;
		if (rootedDeterminant > 0){	
			for (int i = -1; i<=1; i+=2) {
				x2 = (x1 + i*rootedDeterminant)/2;
				if (IsViableSolution(x1, y1, x2, y2, gridSize)) {
					delta+=1;
				}
			}
		}
		else {
			x2 = x1/2;
			if (IsViableSolution(x1, y1, x2, y2, gridSize)) {
				delta+=1;
			}
		}
		return delta;
	}
		
		
	public static boolean IsViableSolution(int x1, int y1, int x2, int y2,int gridSize) {
		if ((x2>=0)&&(x2<=gridSize)&&(!((x2==0)&&(y2==0)))&&(!((x1==x2)&&(y1==y2)))) {
			return true;
		}
		return false;
	}

	public static void main(String[] args) {
		long startTime = System.nanoTime();
		
		int GRIDSIZE = 50;
		int totalSolutions = 0;
		int determinant = 0;
		int rootedDeterminant = 0;
		int x2 = 0;
		int diff = 0;
		List<Integer> squares = new ArrayList<>();
		for (int i = 0; i <= GRIDSIZE*2; i++) {
			squares.add(i*i);
		}
		for (int x1 = 0; x1 <= GRIDSIZE; x1++) {
			for (int y1 = 0; y1 <= GRIDSIZE; y1++) {
				if ((x1==0)&&(y1==0)) {
					continue;
				}
				diff = 0;
				for (int y2 = 0; y2 <= GRIDSIZE; y2++) {
					determinant = x1*x1 - 4*y2*(y2-y1);
					if (squares.contains(determinant)) {
						rootedDeterminant = squares.indexOf(determinant);
						if ((x1 + rootedDeterminant)%2 != 0) continue;
						x2 = (x1 + rootedDeterminant)/2;
						diff += GetNumOfSolutions(x1,y1,x2,y2,rootedDeterminant,GRIDSIZE); //error here
					}
				}
				totalSolutions += diff;
			}
		}
		totalSolutions += GRIDSIZE*GRIDSIZE;
		System.out.println(totalSolutions);
		
		long endTime   = System.nanoTime();
		long totalTime = endTime - startTime;
		System.out.println("\nRuntime: "+totalTime/1000000 + "ms");
	}

}
