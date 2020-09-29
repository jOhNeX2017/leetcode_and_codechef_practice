#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int test_case;
	cin >> test_case;
	for (int i=0; i<test_case; i++){
	    int n;
	    std::cin >> n;
	    int a[n];
	    if( n==1 ){
	        std::cin >> a[0];
	        if(a[0]>=0)
	            std::cout << "YES" << std::endl;
	        else
	            std::cout << "NO" << std::endl;
	    }
	    else{
	        int s=0;
	        for(int j=0; j<n; j++){
	            std::cin >> a[j];
	            s+=a[j];
	        }
	        
	        if(s==0)
	            std::cout << "YES" << std::endl;
	        else{
	            int val = (n*(n+1))/2;
	           // std::cout << "s:" << val<<" n: "<<n << std::endl;
	            if( s<=val && s>0 )
	                std::cout << "YES" << std::endl;
	            else
	                std::cout << "NO" << std::endl;
	        s=0;
	        }
	    }
	}
	return 0;
}

