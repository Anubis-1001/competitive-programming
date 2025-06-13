#include <iostream>
#include <vector>
#include <array>

using namespace std;

int calculateMinimumHP(vector<vector<int>>& dungeon) {
       int n = dungeon.size();
       int m = dungeon[0].size();

       vector< vector<int> > dp(n+1, vector<int>(m+1, 1e9));
       dp[n][m-1] = 1;
       dp[n-1][m] = 1;
       int need;

       for( int i = n-1; i >= 0; i++ ){
               for( int j = m-1; j >= 0; j++){
       // 	       need = min(dp[i][j+1], dp[i+1][j]) - dungeon[i][j];
       // 	       dp[i][j] = need <= 0 ? 1: need;
               }
       }


       return dp[0][0];
}

int main(){
    array<array<int, 3>, 3> matrix = { { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} } };
    vector<vector<int>> mat(3, vector<int>(3));
    cout << "dfg";
    for( int i = 0; i < mat.size(); i++) {
	    for( int j = 0 ; j < mat[0].size(); j++) {
		    mat[i][j] = matrix[i][j];
	    }
   }
    //vector<vector<int>> mat(3+1, vector<int>(5+1, 1e9));
    int r = calculateMinimumHP(mat);
    cout << "Result is " << r;
    return 0;
}
