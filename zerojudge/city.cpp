#include <iostream>
#include <math.h>
using namespace std;
struct point{
	int x;
	int y;
	int protect=0;
};
int energy(struct point a,struct point b){
	return pow((a.x-b.x),2)+pow((a.y-b.y),2);
}
int main(){
	struct point a,b;
	int sum;
	cin >>a.x >>a.y >>b.x >>b.y >>sum;
	struct point city[sum];
	for (int i=0;i<sum;i++)cin >>city[i].x >>city[i].y;
	for (int i=0;i<sum;i++){
		if (energy(a,city[i])>energy(b,city[i])) b.protect=max(b.protect,energy(b,city[i]));
		else a.protect=max(a.protect,energy(a,city[i]));
	}
	cout <<a.protect+b.protect;
	
}
