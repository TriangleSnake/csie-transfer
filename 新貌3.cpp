#include <stdio.h>
#include <stdlib.h>
int main(){
	int val;
	scanf("%d",&val);
	for (int i=0;i<val;i++){
		for (int j=0;j<val;j++){
			if (i+j==val-1||i==0||j==0||i==val-1||j==val-1||i==j){
				printf("*");
			}
			else printf(" ");
			if (j==val-1)printf("\n");
		}
	}
}
 
