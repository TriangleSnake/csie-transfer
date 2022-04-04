#include <stdio.h>
int main (){
	char c[5];
	gets(c);
	for (int i=0;i<5;i++) c[i]=char(int(c[i])-i-6);
	printf("%s",c);
} 
