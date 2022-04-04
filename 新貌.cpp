#include <iostream>
using namespace std;
int check(int x){
	if (x%4==0){
		if (x%400==0||x%100!=0){
			return 1;
		}
		else return 0;
	}
	else return 0;
}
int main (){
	int num;
	cin >>num;
	int date=num%100;
	int month=(num/100)%100;
	int year=(num/10000);
	int DaysOfMonth[12]={31,28,31,30,31,30,31,31,30,31,30,31};
	if (check(year)==1){
		DaysOfMonth[1]=29;
	}
	if (date>DaysOfMonth[month-1]){
		cout <<"日期錯誤";
		return 0; 
	}
	if (month<1||month>12){
		cout <<"日期錯誤";
		return 0;
	}
	for (int i=0;i<month-1;i++){
		date+=DaysOfMonth[i];
	}
	
	
	cout <<date;	
} 
