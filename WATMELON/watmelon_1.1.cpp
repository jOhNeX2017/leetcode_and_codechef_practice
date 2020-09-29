// As the question is stated that we can decrease the a[i] by i as number of times we want then it's means that if the sum of the array is greater than zero then only we can make it goood sequene else it can't be formed.
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int test_case;
	std::cin >> test_case;
	for (int i=0; i<test_case; i++){
	    int n,s=0;
	    std::cin >> n;
	    int a[n];
	    for(int j=0;j<n;j++){
	        std::cin >> a[j];
	        s=s+a[j];
	    }
	    if(s>=0)
	        cout << "YES" << endl;
	    else
	        cout << "NO" << endl;
	}
	return 0;
}

