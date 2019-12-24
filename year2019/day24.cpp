#include <iostream>
#include <fstream>
#include <vector>

using namespace std;



void debug(vector<vector<char>>& matrix){
	for(auto& row:matrix){
		for(auto& col:row){
			cout << col;
		}
		cout << '\n';
	}

}
int biodiversity(vector<vector<char>>& matrix){

	// Adjacent tiles
	vector<vector<vector<char>>> prev_layout;

	const row = 5;
	const col = 5;

	// A bug dies (becoming an empty space) unless there is exactly one bug adjacent to it.
	// An empty space becomes infested with a bug if exactly one or two bugs are adjacent to it.
	
	


	return 0;
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

	debug(matrix);

	return 0;
}

