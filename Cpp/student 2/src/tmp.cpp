#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <array>
#include <limits.h>
#include <vector>
using namespace std;
enum SPOT_STATE
{
    EMPTY = 0,
    BLACK = 1,
    WHITE = 2
};

int player;
const int SIZE = 15;
array<array<int, SIZE + 1>, SIZE + 1> board;
struct position
{
    vector<int> x;
    vector<int> y;
};
struct position is_EMPTY;
struct position is_player;
struct position is_enemy;
int enemy;
void read_board(std::ifstream &fin)
{
    fin >> player;
    enemy = 2 - ((player + 1) % 2);
    for (int i = 0; i < SIZE; i++)
    {
        for (int j = 0; j < SIZE; j++)
        {
            fin >> board[i][j];
            if (board[i][j] == EMPTY)
            {
                for (int k=-2;k<3;k++)
                    for (int l=-2;l<3;l++)
                        if (i+k>=0&&j+l>=0&&board[i+k][j+l]!=EMPTY){
                            is_EMPTY.x.push_back(i);
                            is_EMPTY.y.push_back(j);
                            goto a;            
                        }
                a:continue;
            }
            else if (board[i][j] == player)
            {
                is_player.x.push_back(i);
                is_player.y.push_back(j);
            }
            else
            {
                is_enemy.x.push_back(i);
                is_enemy.y.push_back(j);
            }
        }
    }

}

int min(int a, int b)
{
    if (a > b)
        return b;
    else
        return a;
}
int max(int a, int b)
{
    if (a > b)
        return a;
    else
        return b;
}
int cont(int x, int y, int dir, int turn)
{
    int sum=0;
    switch (dir)
    {
    case (0):
        for (int i = x; i < SIZE; i++)
        {
            if (board[i][y] == turn)
            {
                sum++;
            }
            else
                break;
        }
        break;
    case (1):
        for (int i = y; i < SIZE; i++)
        {
            if (board[x][i] == turn)
            {
                sum++;
            }
            else
                break;
        }
        break;
    case (2):
        for (int i = 0; i < min(SIZE - x, SIZE - y); i++)
        {
            if (board[x + i][y + i] == turn)
            {
                sum++;
            }
            else
                break;
        }
        break;
    case (3):
        for (int i = 0; i < min(SIZE - i, y); i++)
        {
            if (board[x + i][y - i] == turn)
            {
                sum++;
            }
            else
                break;
        }
        break;
    }
    return sum;
}
int contpoint(int x, int y, int cont, int dir)
{
    int point = 0, sum=0;
    if (cont == 5)
        return 50000000;
    switch (dir)
    {
    case (0):
        for (int i = x + cont; i < SIZE; i++)
        {
            if (board[i][y] == EMPTY)
            {
                sum++;
                if ((sum + cont) >= 5)
                    break;
            }
            else
                break;
        }
        if ((sum + cont) >= 5)
        {
            point += cont * cont ;
            sum=0;
        }
        for (int i = x - 1; i >= 0; i--)
        {
            if (board[i][y] == EMPTY)
            {
                sum++;
                if ((sum + cont) >= 5)
                    break;
            }
            else
                break;
        }
        if ((sum + cont) >= 5)
        {
            point += cont * cont ;
            sum=0;
        }
    case (1):
        for (int i = y + cont; i < SIZE; i++)
        {
            if (board[x][i] == EMPTY)
            {
                sum++;
                if ((sum + cont) >= 5)
                    break;
            }
            else
                break;
        }
        if ((sum + cont) >= 5)
        {
            point += cont * cont ;
            sum=0;
        }
        for (int i = y - 1; i >= 0; i--)
        {
            if (board[x][i] == EMPTY)
            {
                sum++;
                if ((sum + cont) >= 5)
                    break;
            }
            else
                break;
        }
        if ((sum + cont) >= 5)
        {
            point += cont * cont ;
        }
        break;
    case (2):
        for (int i = cont; i <= min(SIZE - x, SIZE - y); i++)
        {
            if (board[x + i][y + i] == EMPTY)
            {
                sum++;
                if ((sum + cont) >= 5)
                    break;
            }
            else
                break;
        }
        if ((sum + cont) >= 5)
        {
            point += cont * cont ;
            sum=0;
        }
        for (int i = 1; i <= min(x, y); i++)
        {
            if (board[x - i][y - i] == EMPTY)
            {
                sum++;
                if ((sum + cont) >= 5)
                    break;
            }
            else
                break;
        }
        if ((sum + cont) >= 5)
        {
            point += cont * cont ;
        }
        break;
    case (3):
        for (int i = cont; i <= min(SIZE - x - 1, y); i++)
        {
            if (board[x + i][y - i] == EMPTY)
            {
                sum++;
                if ((sum + cont) >= 5)
                    break;
            }
            else
                break;
        }
        if ((sum + cont) >= 5)
        {
            point += cont * cont ;
            sum=0;
        }
        for (int i = 1; i <= min(x, SIZE - y - 1); i++)
        {
            if (board[x - i][y + i] == EMPTY)
            {
                sum++;
                if ((sum + cont) >= 5)
                    break;
            }
            else
                break;
        }
        if ((sum + cont) >= 5)
        {
            point += cont * cont ;
        }
        break;
    }

    if (point == 32)//活四
        point=2000000;
    else if(point == 16)//四
        point = 150000;
    else if (point==18)//活三
        point=40000;
    return point;
}
int check()
{
    long long int point = 0;
    int x, y;
    for (long unsigned int i = 0; i < is_player.x.size(); i++)
    {
        x = is_player.x[i];
        y = is_player.y[i];
        for (int k = 0; k < 4; k++)
            point += contpoint(x, y, cont(x, y, k, player), k);
        i+=cont(x, y, 0, player)-1;
    }
    for (int i = 0; i < is_enemy.x.size(); i++)
    {
        x = is_enemy.x[i];
        y = is_enemy.y[i];
        for (long unsigned int k = 0; k < 4; k++)
            point -= 2*contpoint(x, y, cont(x, y, k, enemy), k);
        i+=cont(x, y, 0, enemy)-1;
    }
    return point;
}
int minimax(int depth, int PLAYER, int alpha, int beta)
{
    if (depth <= 0)
        return check();
    int x, y;
    long long int point;
    if (PLAYER == player)
    {
        point = INT_MIN;
        for (long unsigned int i = 0; i < is_EMPTY.x.size(); i++)
        {
            x = is_EMPTY.x[i];
            y = is_EMPTY.y[i];
            if (board[x][y] == EMPTY)
            {
                board[x][y] = player;
                is_player.x.push_back(x);
                is_player.y.push_back(y);
                point = max(point, minimax(depth - 1, enemy, alpha, beta));
                board[x][y] = EMPTY;
                is_player.x.pop_back();
                is_player.y.pop_back();
                alpha = max(alpha, point);
                if (alpha >= beta)
                    return point;
            }
        }
        return point;
    }
    else
    {
        point = INT_MAX;
        for (long unsigned int i = 0; i < is_EMPTY.x.size(); i++)
        {
            x = is_EMPTY.x[i];
            y = is_EMPTY.y[i];
            if (board[x][y] == EMPTY)
            {
                board[x][y] = enemy;
                is_enemy.x.push_back(x);
                is_enemy.y.push_back(y);
                point = min(point, minimax(depth - 1, player, alpha, beta));
                board[x][y] = EMPTY;
                is_enemy.x.pop_back();
                is_enemy.y.pop_back();
                beta = min(beta, point);
                if (alpha >= beta)
                    return point;
            }
        }
        return point;
    }
}

void put_board(std::ofstream &fout)
{
    int depth = 0, x, y,mxx=0,mxy=0;
    long long int point = INT_MIN, mx = INT_MIN;
    if (is_EMPTY.x.size()==0){
        fout << 7 << " " << 7 << endl;
        return;
    }
    while (true){
        for (long unsigned int i = 0; i < is_EMPTY.x.size(); i++)
        {
            x=is_EMPTY.x[i];
            y=is_EMPTY.y[i];
            if (board[x][y] == EMPTY)
            {
                board[x][y] = player;
                is_player.x.push_back(x);
                is_player.y.push_back(y);
                point = minimax(depth, enemy, INT_MIN, INT_MAX);
                board[x][y] = EMPTY;
                is_player.x.pop_back();
                is_player.y.pop_back();
                if (point > mx)
                {
                    mx = point;
                    mxx = x;
                    mxy = y;
                }
            }
        }
        fout << mxx << " " << mxy << endl;
        fout.flush();
        depth+=2;
    }
    
}
int main(int, char **argv)
{
    std::ifstream fin(argv[1]);
    std::ofstream fout(argv[2]);
    read_board(fin);
    put_board(fout);
    fin.close();
    fout.close();
    return 0;
}
