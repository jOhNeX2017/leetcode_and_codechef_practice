// Try to find the second max first and loop unitil max did not becomes zero and every time update the moves count and updating the size of the sticks   
#include <iostream>
using namespace std;

int second_max(int *a,int );

int distinct(int *a ,int);

int main() {
	// your code goes here
	int t,n,moves=0;
	cin >> t;
	for(int i=0; i<t; i++){
	    cin >> n;
	    int a[n];
	    for(int j=0;j<n;j++){
	        std::cin >> a[j];
	    }
	    while(second_max(&a[0],n)!=0)
	        moves+=1;
	    std::cout << moves <<endl;
	    moves=0;
	}
	return 0;
}

int distinct( int *a, int n){

	unordered_set<int> s;
	
	for(int i=0; i<n; i++){
		if(s.find(a[i]) == s.end()){
			s.insert(a[i]);
		}
		
	}
	
	return s;

}

int second_max(int *a, int n){
    int max, max2,i;
    max=max2=0;
    
    for(i=0;i<n;i++){
        if(a[i]>max){
            max2=max;
            max=a[i];
        }
        else if(a[i]<max && a[i]>max2)
            max2=a[i];
        
    }
    for(i=0;i<n;i++){
        if(a[i]>max2)
            a[i]=max2;
    }
    if(max==0)
        return 0;
    else
        return 1;
    
}

