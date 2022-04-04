#include <iostream>
using namespace std;
int main (){
	long long int val,lav=0,vval;
	int i=0,add=0;
	int tmp;
	cin >>vval;
	val=vval;
	while (1){
		

		i=0;
		add=val%10;
		val/=10;
		tmp=val;
		while (1){
			if (tmp==0)break;
			tmp/=10;
			add*=10;
		}
		lav+=add;
		if (val==0)break;
	}
	cout <<lav<<endl;
	vval+=lav;
	cout <<vval;
}
