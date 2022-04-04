#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
int main(){
	char pwd[100];
	int a=0,A=0,num=0,check=0;
	gets(pwd);
	int len=strlen(pwd);
	if (len<12){
		printf("您只輸入了%d個密碼，最少需要12個\n",len);
		return 0;
	}
	for (int i=0;i<len;i++){
		if (pwd[i]==' '){
			printf("不可有空格\n");
			check=1;
		}
		else if (isascii(pwd[i])==false){
			printf("密碼不可有中文\n");
			check=1;
		}
		if (int(pwd[i])>=97&&int(pwd[i])<=122)a++;
		else if (int(pwd[i])>=65&&int(pwd[i])<=90)A++;
		else if (int(pwd[i])>=48&&int(pwd[i])<=57)num++;
		else{
			printf("不可以有標點符號:%c\n",pwd[i]);
			check=1;
		}
	}
	if (num<2)printf("至少要有兩個數字\n");
	if (A<2||a<2)printf("至少要有兩個大/小寫英文\n");
	if (check==1)printf("請重新設定符合規定的密碼!\n");
	else printf("您輸入合格的密碼為:\n%s\n其中包含數字:%d\n其中包含文字:%d\n其中包含文字大寫%d\n其中包含文字小寫%d\n",pwd,num,A+a,A,a);
	system("pause");
} 
