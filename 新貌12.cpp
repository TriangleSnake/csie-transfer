#include <stdio.h>
#include <math.h>
int main(){
	float lat,lon,reslat,reslon;
	lon =6371*2*3.14/4/90;
	reslon=2000/lon;
	lat =6371*cos(reslon)*2*3.14/180;
	reslat=2000/lat;
	
	printf("%f\n%f",reslat,reslon);
} 
