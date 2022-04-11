#include <iostream>
#include <stdlib.h>
#include <Windows.h>
#include <math.h>
#include <vector>
#include <conio.h>
#include <time.h>
using namespace std;
const int size=38;
const float speed=32;
string screen[size][size];
int lng=2;

void HideCursor() {
	CONSOLE_CURSOR_INFO cursor_info = {1, 0};
	SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &cursor_info); 
}



void show(){
	HideCursor();
	COORD pos;
	pos.X=0;
	pos.Y=0;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),pos);
	for (int i=0;i<size;i++){
		for (int j=0;j<size;j++){
			cout <<screen[i][j];
		}
		cout <<endl;
	}
	Sleep(speed);
}
void menu(){
	HideCursor();
	COORD pos;
	pos.X=0;
	pos.Y=size/2-3;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),pos);
			string icon=
"\
―   .oooooo..o ooooo      ooo       .o.       oooo    oooo oooooooooooo \n\
―  d8P'    `Y8 `888b.     `8'      .888.      `888   .8P'  `888'     `8 \n\
―  Y88bo.       8 `88b.    8      .8\"888.      888  d8'     888        \n\
―   `\"Y8888o.   8   `88b.  8     .8' `888.     88888[       888oooo8   \n\
―       `\"Y88b  8     `88b.8    .88ooo8888.    888`88b.     888    \"   \n\
―  oo     .d8P  8       `888   .8'     `888.   888  `88b.   888       o\n\
―  8\"\"88888P'  o8o        `8  o88o     o8888o o888o  o888o o888ooooood8\
";
	while (1){
		SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),pos);
		cout <<icon <<endl;
		cout <<"―- - - - - - - - - - - - press  ANY  key  to  START - - - - - - - - - - -";
		Sleep(1000);
		show();
		Sleep(1000-speed);
		if (_kbhit())break;
	}
}

struct pos{
	int x;
	int y;
};
struct pos apple;
struct pos tmp;
void food(){
	srand(time(NULL));
	apple.x=1+rand()%(size-2);
	srand(time(NULL)*2);
	apple.y=1+rand()%(size-2);
}

vector <struct pos> snake;
void kill(){
	COORD pos;
	pos.X=0;
	pos.Y=size/2-3;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),pos);
	cout <<"\
oooooo   oooo   .oooooo.   ooooo     ooo    oooooooooo.   ooooo oooooooooooo \n\
 `888.   .8\'   d8P\'  `Y8b  `888\'     `8\'    `888\'   `Y8b  `888\' `888\'     `8 \n\
  `888. .8\'   888      888  888       8      888      888  888   888         \n\
   `888.8\'    888      888  888       8      888      888  888   888oooo8    \n\
    `888\'     888      888  888       8      888      888  888   888    \"    \n\
     888      `88b    d88\'  `88.    .8\'      888     d88\'  888   888       o \n\
    o888o      `Y8bood8P\'     `YbodP\'       o888bood8P\'   o888o o888ooooood8 \
	";
	pos.X=size;
	pos.Y=size/2+6;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),pos);
	cout <<"SCORE:" <<lng+1;
	while (1) if (_getch()==27)break;
	exit(0);
}
void longer(){
	if (snake[lng].x==snake[lng-1].x){
		tmp.x=snake[lng].x*2-snake[lng-1].x;
	}
	else if (snake[lng].y==snake[lng-1].y){
		tmp.y=snake[lng].y*2-snake[lng-1].y;
	}
	snake.push_back(tmp);
}
void update(){
	if (apple.x==snake[0].x&&apple.y==snake[0].y){
		food();
		longer();
		lng++;
	}
	
	for (int i=1;i<size-1;i++){
		for (int j=1;j<size-1;j++) screen[i][j]="  ";
	}
	screen[apple.y][apple.x]="O ";
	screen[snake[0].y][snake[0].x]="―";
	for (int i=1;i<=lng;i++){
		screen[snake[i].y][snake[i].x]="―";
		if (apple.x==snake[i].x&&apple.y==snake[i].y){
			food();
		}
	}
	if (snake[0].x>=size-1||snake[0].y>=size-1||snake[0].x<=0||snake[0].y<=0) kill();
}

int main(){
	keybd_event(16,0,0,0);
	keybd_event(16,0,KEYEVENTF_KEYUP,0);
	keybd_event(122,0,0,0);
	keybd_event(122,0,KEYEVENTF_KEYUP,0);
	HideCursor();
	int cmd=int('d');
	tmp.x=size/2;
	tmp.y=size/2;
	snake.push_back(tmp);
	tmp.x=size/2-1;
	snake.push_back(tmp);
	tmp.x=size/2-2;
	snake.push_back(tmp);
	for (int i=0;i<size;i++){
		for (int j=0;j<size;j++){
			if (i==0||i==size-1||j==0||j==size-1) screen[i][j]="―";
			else screen[i][j]="  ";
			cout <<screen[i][j];
		}
		cout <<endl;
	}
	food();
	menu();
	while (1){
		
		if (cmd==int('w')){
			tmp.y=(snake[0].y)-1;
			tmp.x=(snake[0].x);
		}
		else if (cmd==int('s')){
			tmp.y=(snake[0].y)+1;
			tmp.x=snake[0].x;
		}
		else if (cmd==int('a')){
			tmp.x=(snake[0].x)-1;
			tmp.y=snake[0].y;
		}
		else if (cmd==int('d')){
			tmp.x=(snake[0].x)+1;
			tmp.y=snake[0].y;
		}
		
		
		for (int i=lng;i>0;i--){
			snake[i]=snake[i-1];
		}
		snake[0]=tmp;
		for (int i=1;i<=lng;i++){
			if (snake[i].x==snake[0].x&&snake[i].y==snake[0].y)kill();
		}
		update();
		show();
		if (_kbhit()){
			char k=_getch();
			if ((k==int('w')&&cmd==int('s'))||(k==int('s')&&cmd==int('w'))||(k==int('a')&&cmd==int('d'))||(k==int('d')&&cmd==int('a'))){
				continue;
			}
			else if (k==int('w')||k==int('s')||k==int('a')||k==int('d'))cmd=k;
		}
	}
	
	
} 
