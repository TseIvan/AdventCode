#include <iostream>
#include <fstream>
#include <set>
#include<tuple>
#include<vector>
#include <algorithm>
using namespace std;
int neighbors(const int x, const int y, const int z, vector<tuple<int, int, int>> bug_vec){
    int total_neighbors = 0;






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
                if (x != 2 && y != 2){ // Middle square is left blank for recursive. Do not create new bugs on this position
                    int amt_neighbors = neighbors(x,y,z,original); // 
                    // Rule sets for spawn and death are the same as previous
                    if  (find(original.begin(),original.end(),(x,y,z)) != original.end()){ // original contains the tuple (x,y,z) its a '#'
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

	ifstream infile("day24p2.txt");
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


    time(vec);
    
    // // Test Sort ing
    // vec.push_back(make_tuple(1,1,-1));
    // vec.push_back(make_tuple(1,1,20));

   
    
    
    // for (int i = 0; i < vec.size(); i++)  
    //     cout << get<0>(vec[i]) << " " 
    //          << get<1>(vec[i]) << " " 
    //          << get<2>(vec[i]) << "\n"; 

    
    // std::sort(vec.begin(), vec.end(), [](auto const &t1, auto const &t2) {
    //     return get<2>(t1) < get<2>(t2); 
    // });

    // cout << get<2>(vec[vec.size() - 1]) << endl;
    // // cout << vec.size() << endl;

    // for (int i = 0; i < vec.size(); i++){
       
    //     cout << get<0>(vec[i]) << " " 
    //             << get<1>(vec[i]) << " " 
    //             << get<2>(vec[i]) << "\n"; 
    // }

    // cout << vec.size();

	return 0;
}
