#include <iostream>
#include <cmath>
#include <vector>
#include <string>

using namespace std;

void printMatrix(const vector<vector<int>>& matrix) {
    for (const auto& row : matrix) {
        for (int value : row) {
            cout << value << " ";
        }
        cout << endl;
    }
}

int getIntegers(int max_digit_sum, int min_digit_sum, string num_limit){
	vector<vector<int>> dp(num_limit.size()+1, vector<int>(max_digit_sum+1, 0));
	
	for ( int i = 0; i < dp.size(); i++ ){
		for ( int j = 0; j < dp[0].size(); j++ ){
			if ( j >= 9*i )
				dp[i][j] = (int)pow(10, i);
			else {
				dp[i][j]=0;
				for ( int d = 0; d < 10 and j-d >= 0; d++)
					dp[i][j]+=dp[i-1][j-d];
			}
		}
	}

	int result = 0;
	int digit;
	int n = num_limit.size();
	for( int k = 0; k < n; k++){
		digit = num_limit[k] - '0';

		for ( int d = 0; d < digit and max_digit_sum-d >= 0 ; d++){
			result+=dp[n-1-k][max_digit_sum-d];
		        if ( min_digit_sum-1-d >=0 ) result-= dp[n-1-k][min_digit_sum-1-d];
		}
		max_digit_sum-=digit;
		min_digit_sum-=digit;
	}

	return result;

}


int count(string num1, string num2, int min_sum, int max_sum) {
	return getIntegers(max_sum, min_sum, num2) - getIntegers(max_sum, min_sum, to_string(stoi(num1)-1)) + 1;
}

int main(){
	cout << count("1", "12", 1, 8);
	return 0;
}
