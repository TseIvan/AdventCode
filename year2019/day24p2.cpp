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
vector<vector<char>> emptyMatrix(){
    vector<vector<char>> emptyMatrix;
    vector<char> row;
    for(int x = 0; x < 5; x++){
		for(int y = 0; y < 5; y++){
            if (x==2 && y==2){
                row.push_back('?');
            }else
            {
                row.push_back('.');
            }
		}
        emptyMatrix.push_back(row);
		row.clear();
	}
    return emptyMatrix;
}
vector<vector<char>> biodiversity(vector<vector<char>>& matrix){

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

	prev_layout.push_back(matrix);
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
    debug(temp);
    return matrix;
}

int main(){

	ifstream infile("day24p2.txt");
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
	// biodiversity(matrix); // Level 0
    matrix = emptyMatrix(); // Empty matrix works
    debug(matrix);
    //  How to store and retrieve stacked matrixes
	return 0;
}
