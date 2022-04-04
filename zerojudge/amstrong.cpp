#include <iostream>
using namespace std;
int rec(int n,int p){
	if (n>=10) return (n%10)^p+rec(n/10,p);
	else return n^p;
}
int main(){
	int a,b,p=0,tmp;
	cin >>a >>b;
	for (int i=a;i<=b;i++){
		tmp=i;
		while (tmp){
			p++;
			tmp/=10;
		}
		cout <<i <<" " <<rec(i,p) <<endl;
		if (i==rec(i,p)){
			cout <<i <<"¡@";
			return 0; 
		}
		p=0;
	}
	cout <<"none";
	return 0;
} 
