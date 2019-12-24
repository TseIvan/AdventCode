#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

void debug(vector<vector<char>>& matrix){
	for(auto& row:matrix){
		for(auto& col:row){
			cout << col;
		}
		cout << endl;
	}

}
long int compute_rating(vector<vector<char>>& matrix, int row, int col){
	debug(matrix);
	long int sum;
	// increasing powers of two: 1, 2, 4, 8, 16, 32
	// 1, 2, 4, 8, 16, 
	// 32, 64, 128, 256, 512,
	// 1024 ..

	for(int x = 0; x < row; x++){
		for(int y = 0; y < col; y++){
			if (matrix[x][y] == '#'){
				cout << x*5 + y << endl;
				sum += pow(2, x*5 + y);
			}
		}
	}
	cout << sum;
	return sum;
}

int biodiversity(vector<vector<char>>& matrix){

	// Adjacent tiles
	vector<vector<vector<char>>> prev_layout;
	vector<vector<char>> temp(matrix);
	const int row = 5;
	const int col = 5;
	int bugs = 0;
	// Adjacent is only N W S E directions not diagonal
	vector<int> p_x = {0,-1,0,1};
	vector<int> p_y = {1,0,-1,0};
	int delta_x;
	int delta_y;

	// A bug dies (becoming an empty space) unless there is exactly one bug adjacent to it. 
	// An empty space becomes infested with a bug if exactly one or two bugs are adjacent to it.
	// Spawn new bug before death
	prev_layout.push_back(matrix);
	// debug(matrix);
	while (true){
		for (int x = 0; x < row; x++){
			for (int y = 0; y < col; y++){
				bugs = 0;
				// cout << matrix[x][y] << endl;
				for (int dir = 0; dir < 4; dir++){
					// For each direction >> check if outside dimensions
					delta_x = x+p_x[dir];
					delta_y = y+p_y[dir];	
					if (delta_x >= 0 && delta_x < 5 && delta_y >= 0 && delta_y < 5){
						if (matrix[delta_x][delta_y] == '#'){
							bugs++;
						}
					}
				}
				// // Implement death and spawn
				if (matrix[x][y] == '#' && bugs != 1){
					temp[x][y] = '.';
				}
				else if (matrix[x][y] == '.' && bugs > 0 && bugs <=2){
					temp[x][y] = '#';
				}
			}
		}
		// debug(temp);
		// Check in previous then push back
		for (auto prev:prev_layout){
			if (prev == temp){
				debug(temp); // Works
				// cout << "terminated" << endl;
				return compute_rating(temp, row, col);
			}
		}
		prev_layout.push_back(matrix);
		matrix = temp;
	}
}

int main(){

	ifstream infile("day24.txt");
	string line;
	vector<vector<char>> matrix;
	vector<char> row;

	while(infile >> line){
		for(int i = 0; i < line.size(); i++){
			row.push_back(line[i]);
		}
		matrix.push_back(row);
		row.clear();
	}

	biodiversity(matrix);

	// debug(matrix);

	return 0;
}

