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
		printf("�z�u��J�F%d�ӱK�X�A�ֻ̤ݭn12��\n",len);
		return 0;
	}
	for (int i=0;i<len;i++){
		if (pwd[i]==' '){
			printf("���i���Ů�\n");
			check=1;
		}
		else if (isascii(pwd[i])==false){
			printf("�K�X���i������\n");
			check=1;
		}
		if (int(pwd[i])>=97&&int(pwd[i])<=122)a++;
		else if (int(pwd[i])>=65&&int(pwd[i])<=90)A++;
		else if (int(pwd[i])>=48&&int(pwd[i])<=57)num++;
		else{
			printf("���i�H�����I�Ÿ�:%c\n",pwd[i]);
			check=1;
		}
	}
	if (num<2)printf("�ܤ֭n����ӼƦr\n");
	if (A<2||a<2)printf("�ܤ֭n����Ӥj/�p�g�^��\n");
	if (check==1)printf("�Э��s�]�w�ŦX�W�w���K�X!\n");
	else printf("�z��J�X�檺�K�X��:\n%s\n�䤤�]�t�Ʀr:%d\n�䤤�]�t��r:%d\n�䤤�]�t��r�j�g%d\n�䤤�]�t��r�p�g%d\n",pwd,num,A+a,A,a);
	system("pause");
} 
