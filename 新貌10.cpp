#include <stdio.h>
#include <math.h>
int main (){
	float a,b,c,res,D;
	char cont;
	a:
	scanf ("%f%f%f",&a,&b,&c);
	D=(b*b-4*a*c);
	if (D<0){
		printf("����{��������");
		res=b*(-1)/(2*a);
		D*=-1;
		D=sqrt(D);
		D=D/(a*2);
		printf("%f+-%fi",res,D);
	}
	else if (D==0){
		printf("����{��������");
		res=b*(-1)/(2*a);
		printf("%f",res);
	}
	else {
		printf ("����{������۲����");
		res=b*(-1)/(a*2);
		D=sqrt(D)/(a*2);
		printf("%f+-%f",res,D);
	}
	printf("�O�_�A���p��");
	scanf("%s",&cont);
	if (cont=='y')goto a;
	else return 0;
}
