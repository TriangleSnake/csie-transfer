#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
	char s[100];
	int n[100],sum=0;
	gets(s);
	for (int i=0;i<strlen(s);i++){
		switch (s[i]){
		 case 'I':{
			n[i]=1;
			break;
		 }
		 case 'V':{
			n[i]=5;
			break;
		 }
		 case 'X':{
			n[i]=10;
			break;
		 }
		 case 'L':{
			n[i]=50;
			break;
		 }
		 case 'C':{
			n[i]=100;
			break;
		 }
		 case 'D':{
			n[i]=500;
			break;
		 }
		 case 'M':{
			n[i]=1000;
			break;
		 }
		}
		sum+=n[i];
	}
	for (int i=0;i<strlen(s)-1;i++){
		if (strlen(s)%2==0){
			if (i%2==0&&n[i]<n[i+1]) sum-=2*(n[i]);
		}
		else {
			if (i%2==1&&n[i]<n[i+1]) sum-=2*(n[i]);
		}
	}
	printf("%d",sum); 
}
