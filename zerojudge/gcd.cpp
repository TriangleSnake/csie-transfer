#include <iostream>
using namespace std;
int rec(int a,int b){
	if (a==0 || b==0)return a+b;
    if (a>b)return rec(a%b,b);
    else return rec(b%a,a);
}
int main(){
	int a,b;
	cin >>a >>b;
	cout <<rec(a,b);
}
