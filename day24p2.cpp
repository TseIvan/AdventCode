// If I can figure out how to implement depth properly I can avoid search
// Test from -1,0,1. Initialize as vector<vector<vector<char>>> then for all depth > 1 => pushback all depth < -1 requires insert at pos 0.

#include <iostream>
#include <fstream>
#include <set>
#include <tuple>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

void printVector(vector<tuple<int, int, int>> v){
        for (int i = 0; i < v.size(); i++){
            cout << get<0>(v[i]) << " "
            << get<1>(v[i]) << " "
            << get<2>(v[i]) << "\n";
    }
}
bool vectorFindTuple(vector<tuple<int, int, int>> input_vec, int x, int y, int z){

        for (int i = 0; i <  input_vec.size(); i++){
            if (make_tuple(x,y,z) == input_vec[i]){
                return true;
            }
        }
        return false;
}
int neighbors(const int x, const int y, const int z, vector<tuple<int, int, int>> bug_vec){
    int total_neighbors = 0;


    // https://gyazo.com/e09f41dc16c316137b5ce6ca2e95d87b >> diagram from AOC
    // https://pastebin.com/3tYPUHZz >> output for the first 10 time iteration using dummy example given

    // Compute all the levels below us

    // if X = 0 (eg Central grid all left column has neighhbors 1 level up on left side)
    if  (vectorFindTuple(bug_vec,1,2,z-1) && x == 0){
        total_neighbors += 1;
    }
    // if X = 4 (eg Central grid all right column has neighhbors 1 level up on right side)
    if  (vectorFindTuple(bug_vec,3,2,z-1) && x == 4){
        total_neighbors += 1;
    }
    if  (vectorFindTuple(bug_vec,2,1,z-1) && y == 0){
        total_neighbors += 1;
    }
    if  (vectorFindTuple(bug_vec,2,3,z-1) && y == 4){
        total_neighbors += 1;
    }


    // Compute all the levels above us
    // Example Tile 8
    if (x == 1 && y == 2){
        for (int t = 0; t < 5; t++){
            if (vectorFindTuple(bug_vec,0,t,z+1)){
                total_neighbors += 1;
            }
        }
    }
    // Example Tile 14
    if (x == 3 && y == 2){
        for (int t = 0; t < 5; t++){
            if (vectorFindTuple(bug_vec,4,t,z+1)){
                total_neighbors += 1;
            }
        }
    }
    // Example Tile 12
    if (x == 2 && y == 1){
        for (int t = 0; t < 5; t++){
            if (vectorFindTuple(bug_vec,t,0,z+1)){
                total_neighbors += 1;
            }
        }
    }
    //  Example Tile 18 -> Seek one level up: U|V|W|X|Y
    if (x == 2 && y == 3){
        for (int t = 0; t < 5; t++){
            if (vectorFindTuple(bug_vec,t,4,z+1)){
                total_neighbors += 1;
            }
        }
    }
    // Compute all on the same level.
    vector<int> p_x = {0,-1,0,1};
	vector<int> p_y = {1,0,-1,0};
	int delta_x;
	int delta_y;
    for (int dir = 0; dir < 4; dir++){
        // For each direction >> check if outside dimensions
        delta_x = x+p_x[dir];
        delta_y = y+p_y[dir];

        if (x == 2 && y == 2) continue;
        if (delta_x >= 0 && delta_x < 5 && delta_y >= 0 && delta_y < 5){
            // cout << delta_x << " " << delta_y << " " << " " << z << " " << endl;
            if(vectorFindTuple(bug_vec,delta_x,delta_y,z)){
                total_neighbors += 1;
            }
        }
    }
    // cout << total_neighbors << endl;
    return total_neighbors;
}
vector<tuple<int, int, int>> time(vector<tuple<int, int, int>> original){
    vector<tuple<int, int, int>> updated_vec;
    const int row = 5;
    const int col = 5;
    // Need to start at minimum level to highest level
    // At each iteration*2 + 1 layers

    sort(original.begin(), original.end(), [](auto const &t1, auto const &t2) {
        return get<2>(t1) < get<2>(t2);
    });


    // Time 1: z - > -1,0,1, Time 2: z - > -2,-1,0,1,2
    for(int z = get<2>(original[0]) - 1; z < 2 + get<2>(original[original.size() - 1]); z++){
        for(int y = 0; y < row; y++){
            for (int x = 0; x < col; x++){
                if (x == 2 && y == 2){
                    ;
                }
                else{ // Middle square is left blank for recursive. Do not create new bugs on this position
                    int amt_neighbors = neighbors(x,y,z,original); //
                    // cout << x << " " << y << " " << z << " " << amt_neighbors << endl;
                    // Rule sets for spawn and death are the same as previous
                    if  (vectorFindTuple(original,x,y,z)){ // original contains the tuple (x,y,z) its a '#'
                        if (amt_neighbors == 1){
                            updated_vec.push_back(make_tuple(x,y,z));
                        }
                    }else if (amt_neighbors > 0 && amt_neighbors <= 2){ //  its a '.' character
                        updated_vec.push_back(make_tuple(x,y,z));
                    }
                }
            }
        }
    }

    return updated_vec;
}

int main(){

	ifstream infile("day24.txt");
	string line;

    vector<tuple<int, int, int> > vec;
    int y = 0;
    int x = 0;
    int iteration = 10;
	while(infile >> line){
        x = 0;
		for(int i = 0; i < line.size(); i++){
            if (line[i] == '#'){
                vec.push_back(make_tuple(x,y,0));
            }
            x++;
		}
        y++;
	}

    for (int iter = 0; iter < 200; iter++){
        vec = time(vec);
        cout <<  iter << endl;
    }

    printVector(vec);

    cout <<  "\n" << vec.size() << endl;

	return 0;
}
