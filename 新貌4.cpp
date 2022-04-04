#include<stdio.h>
#include<stdlib.h>
int sub(int val,int i){
	int tmp;
	tmp=val/i;
	val%=i;
	printf("%d:%d\n",i,tmp);
	return val;
}
int main(){
	int v;
	scanf("%d",&v);
	sub(sub(sub(sub(sub(sub(sub(v,1000),500),100),50),10),5),1);	
}
