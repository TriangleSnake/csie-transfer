#include <stdio.h>
#include <stdlib.h>
int main(){
	int inp,ans;
	ans=rand()%23+2;
	for (int i=1;i<=10;i++){
		scanf("%d",&inp);
		if (inp>ans)printf("�j�󥿽T��\n");
		else if (inp<ans)printf("�p�󥿽T��\n");
		else {
			printf("�z����F�A�@�q�F%d���A",i);
			goto a;	
		}
	}
	printf("�A���A�F��A");
	a:
		printf("���T���׬�:%d\n",ans);
		system("pause");
}
