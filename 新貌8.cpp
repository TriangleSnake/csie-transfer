#include <stdio.h>
int main(){
	int n;
	scanf("%d",&n);
	printf("YES");
	for (int i=1;i<=n;i++)if (i*i==n)return 0;
	printf("\rNO "); 
} 
