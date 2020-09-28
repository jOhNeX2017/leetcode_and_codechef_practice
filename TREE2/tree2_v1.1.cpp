// in this first I found all the distict number from the arrays and after that repeated the same step as followed in first.
#include <iostream>
#include<bits/stdc++.h> 
using namespace std;

// int distinct(int *a, int);
int second_smallest(int *a,int );

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
            if(s.find(a[j]) == s.end()){
    			s.insert(a[j]);
    		}
        }
        
        int m=s.size();
        int b[m],j=0;
        
        for(auto itr=s.begin(); itr!=s.end();itr++){
             b[j]=*itr;
             j++;
        }
        
        while(second_smallest(&a[0],n)!=0)
	        moves+=1;
	    std::cout << moves <<endl;
	    moves=0;
	}
    // std::cout << s.size() << std::endl;
    
    return 0;
}

int second_smallest(int *a, int n){
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



