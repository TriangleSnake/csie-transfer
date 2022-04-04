#include <stdio.h>
#include <stdlib.h>
int main(){
	int inp,ans;
	ans=rand()%23+2;
	for (int i=1;i<=10;i++){
		scanf("%d",&inp);
		if (inp>ans)printf("大於正確值\n");
		else if (inp<ans)printf("小於正確值\n");
		else {
			printf("您答對了，共猜了%d次，",i);
			goto a;	
		}
	}
	printf("再接再厲喔，");
	a:
		printf("正確答案為:%d\n",ans);
		system("pause");
}
