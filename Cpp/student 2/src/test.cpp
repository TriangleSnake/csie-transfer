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
void read_board()
{
    player = 1;
    enemy = 2 - ((player + 1) % 2);
    for (int i = 0; i < SIZE; i++)
    {
        for (int j = 0; j < SIZE; j++)
        {
            board[i][j] = 0;
            board[5][5]=2;
            board[5][6]=2;
            board[5][7]=2;
            if (board[i][j] == EMPTY)
            {
                is_EMPTY.x.push_back(i);
                is_EMPTY.y.push_back(j);
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
    int sum = 0;
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
    int point = 0, sum = 0;
    if (cont == 5)
        return 10000;
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
            point += cont * cont * cont;
            sum = 0;
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
            point += cont * cont * cont;
        }
        break;
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
            point += cont * cont * cont;
            sum = 0;
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
            point += cont * cont * cont;
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
            point += cont * cont * cont;
            sum = 0;
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
            point += cont * cont * cont;
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
            point += cont * cont * cont;
            sum = 0;
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
            point += cont * cont * cont;
        }
        break;
    }

    if (point == 128)
        point = 800;
    return point;
}
int check()
{
    int point = 0, x, y;
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
            point -= contpoint(x, y, cont(x, y, k, enemy), k);
    }
    return point;
}
int minimax(int depth, int PLAYER, int alpha, int beta)
{
    
    if (depth <= 0)
        return check();
    int point, x, y;
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
                    break;
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
                alpha = min(alpha, point);
                if (alpha >= beta)
                    break;
            }
        }
        return point;
    }
}

void put_board()
{
    int depth = 0, x, y, mxx, mxy;
    int point = INT_MIN, mx = INT_MIN;
    while (true)
    {
        for (long unsigned int i = 0; i < is_EMPTY.x.size(); i++)
        {
            x = is_EMPTY.x[i];
            y = is_EMPTY.y[i];
            if (board[x][y] == EMPTY)
            {
                board[x][y] = player;
                is_player.x.push_back(x);
                is_player.y.push_back(y);
                point = minimax(depth, enemy, INT_MIN, INT_MAX);
                cout <<"x:" <<x <<" y:" <<y <<" point:" <<point <<endl;
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
        cout << mxx << " " << mxy << std::endl;
        depth += 2;
        mx = INT_MIN;
    }
}
int main(int, char **argv)
{
    read_board();
    put_board();
    return 0;
}
