// First I found all the distinct number from the arrays and after that output the size of the distinct array
#include <iostream>
#include<bits/stdc++.h> 
using namespace std;

int main(void){
    // Your code here!
    int t,n,moves=0;
	cin >> t;
	
	for(int i=0;i<t;i++){
	    	cin>>n;
        	unordered_set<int> s;
        	int a[n];
        	for(int j=0; j<n; j++){
        		std::cin >> a[j];
           		if(s.find(a[j]) == s.end() && a[j]!=0){
    				s.insert(a[j]);
    			}
        	}
        
        	std::cout << s.size() <<endl;
  
	}
    
    return 0;
}



