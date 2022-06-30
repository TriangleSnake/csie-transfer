#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <array>
#include <limits.h>
using namespace std;
enum SPOT_STATE {
    EMPTY = 0,
    BLACK = 1,
    WHITE = 2
};

int player;
const int SIZE = 15;
array<array<int, SIZE+1>, SIZE+1> board;
array<array<int, 2>, SIZE> position_p;
array<array<int, 2>, SIZE> position_e;
int enemy;
void read_board(std::ifstream& fin) {
    fin >> player;
    enemy=2-((player+1)%2);
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            fin >> board[i][j];
        }
        board[i][SIZE+1]=enemy;
    }
    //最後一行
    for (int i=0;i<SIZE;i++){
        board[SIZE+1][i]=enemy;
    }
}

void write_valid_spot(std::ofstream& fout) {
    srand(time(NULL));
    //int x, y;
    // Keep updating the output until getting killed.
    while(true) {
        // Choose a random spot.
        int x = (rand() % SIZE);
        int y = (rand() % SIZE);
        if (board[x][y] == EMPTY) {
            fout << x << " " << y << std::endl;
            // Remember to flush the output to ensure the last action is written to file.
            fout.flush();
        }
    }
}
int min(int a,int b){
    if (a==0||b==0)return a+b;
    else if (a>b) return b;
    else return a;
}
int max(int a,int b){
    if (a==0||b==0)return a+b;
    else if (a>b) return a;
    else return b;
}
int cont(int x,int y,int dir,int turn){
    int sum=0;
    switch (dir){
        case (0):
            for (int i=x;i<SIZE;i++){
                if (board[i][y]==turn){
                    sum++;
                }
                else break;
            }
            break;
        case (1):
            for (int i=y;i<SIZE;i++){
                if (board[x][i]==turn){
                    sum++;
                }
                else break;
            }
            break;
        case (2):
            for (int i=0;i<min(SIZE-x,SIZE-y);i++){
                if (board[x+i][y+i]==turn){
                    sum++;
                }
                else break;
            }
            break;
        case (3):
            for (int i=0;i<min(SIZE-i,y);i++){
                if (board[x+i][y-i]==turn){
                    sum++;
                }
                else break;
            }
            break;
    }
    return sum;
}
int contpoint(int x,int y,int cont,int dir){
    int point=0,sum=0;
    switch (dir){
        case (0):
            for (int i=x+cont;i<SIZE;i++){
                if (board[i][y]==EMPTY){
                    sum++;
                    if ((sum+cont)>=5) break;
                }
                else break;
            }
            if ((sum+cont)>=5){
                point+=cont*cont;
                sum=0;
            }
            for (int i=x-1;i>=0;i--){
                if (board[i][y]==EMPTY){
                    sum++;
                    if ((sum+cont)>=5) break;
                }
                else break;
            }
            if ((sum+cont)>=5){
                point+=cont*cont;
            }
            break;
        case (1):
            for (int i=y+cont;i<SIZE;i++){
                if (board[x][i]==EMPTY){
                    sum++;
                    if ((sum+cont)>=5) break;
                }
                else break;
            }
            if ((sum+cont)>=5){
                point+=cont*cont;
                sum=0;
            }
            for (int i=y-1;i>=0;i--){
                if (board[x][i]==EMPTY){
                    sum++;
                    if ((sum+cont)>=5) break;
                }
                else break;
            }
            if ((sum+cont)>=5){
                point+=cont*cont;
            }
            break;
        case (2):
            for (int i=cont;i<min(SIZE-x,SIZE-y);i++){
                if (board[x+i][y+i]==EMPTY){
                    sum++;
                    if ((sum+cont)>=5) break;
                }
                else break;
            }
            if ((sum+cont)>=5){
                point+=cont*cont;
                sum=0;
            }
            for (int i=1;i<min(x,y);i++){
                if (board[x-i][y-i]==EMPTY){
                    sum++;
                    if ((sum+cont)>=5) break;
                }
                else break;
            }
            if ((sum+cont)>=5){
                point+=cont*cont;
            }
            break;
        case (3):
            for (int i=cont;i<min(SIZE-x,y);i++){
                if (board[x+i][y-i]==EMPTY){
                    sum++;
                   if ((sum+cont)>=5) break;
                }
                else break;
            }
            if ((sum+cont)>=5){
                point+=cont*cont;
                sum=0;
            }
            for (int i=1;i<min(x,SIZE-y);i++){
                if (board[x-i][y+i]==EMPTY){
                    sum++;
                    if ((sum+cont)>=5) break;
                }
                else break;
            }
            if ((sum+cont)>=5){
                point+=cont*cont;
            }
            break;
    }
    if (point>=18) point*=100;
    return point;
}
int check(){
    int point=0;
    for (int i=0;i<SIZE;i++){
        for (int j=0;j<SIZE;j++){
            if (board[i][j]==player){
                for (int k=0;k<4;k++) point+=contpoint(i,j,cont(i,j,k,player),k);
            }
            else if (board[i][j]==enemy){
                for (int k=0;k<4;k++) point-=contpoint(i,j,cont(i,j,k,enemy),k);
            } 
        }
    }
    return point;
}
int mxx=0;
int mxy=0;
int minimax(int depth,int PLAYER){
    if (depth<=0){
        if (PLAYER==enemy)return INT_MIN;
        else return INT_MAX;
    }
    int point=0;
    int mx=INT_MIN,x,y;
    if (PLAYER==player){
        for (int i=0;i<sizeof(position_e)/sizeof(position_e[0]);i++){
            for (int j=0;j<sizeof(position_e)/sizeof(position_e[0]);j++){
                if (board[i][j]==EMPTY){
                    board[i][j]=PLAYER;
                    point=check();
                    if (point>mx){
                        mx=point;
                        mxx=i;
                        mxy=j;
                        x=i;
                        y=j;
                    }
                    point=max(mx,minimax(depth-1,enemy));
                    board[i][j]=EMPTY;
                }
            }
        }
        mxx=x;
        mxy=y;
        return point;
    }
    else {
        int mn=INT_MAX,x,y;
        for (int i=0;i<sizeof(position_e)/sizeof(position_e[0]);i++){
            for (int j=0;j<sizeof(position_e)/sizeof(position_e[0]);j++){
                if (board[i][j]==EMPTY){
                    board[i][j]=PLAYER;
                    point=check();
                    if (point<mn){
                        mn=point;
                        mxx=i;
                        mxy=j;
                        x=i;
                        y=j;
                    }
                    point=min(mn,minimax(depth-1,enemy));
                    board[i][j]=EMPTY;
                }
            }
        }
        mxx=x;
        mxy=y;
        return point;
    }

}


void put_board(std::ofstream& fout){
    int depth=1;
    while (true){
        minimax(depth,player);
        fout << mxx << " " << mxy << std::endl;
        fout.flush();
        depth+=2;
    }
}
int main(int, char** argv) {
    std::ifstream fin(argv[1]);
    std::ofstream fout(argv[2]);
    read_board(fin);
    put_board(fout);
    fin.close();
    fout.close();
    return 0;
}
