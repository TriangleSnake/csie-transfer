#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <array>
#include <bits/stdc++.h>
using namespace std;
enum SPOT_STATE {
    EMPTY = 0,
    BLACK = 1,
    WHITE = 2
};

int player, opp;
const int SIZE = 15;
std::array<std::array<int, SIZE>, SIZE> board;
string player_type[3];
bitset<15> chess_place[4][15];

int calculate_score(string input, int left, int right, int valid_range){
    int current_score = 1;
    string compare; compare.push_back(input[4]); 
    int defense = (compare != "o"), len = left - right + 1;
    if (defense) current_score*= -3;
    char op = (input[4] == 'o')? 'x' : 'o';
    bool left_three = false, right_three = false;
    if (len >= 5){
        if (defense) current_score = -100000000; 
        else current_score = 1900000;
    }
    else {
        if (valid_range <= 4){
            current_score = 0;
        }
    }
    if (len == 4){
        bool left_is_empty = (input[left+1] == '.'), right_is_empty = (input[right-1] == '.');
        if (left_is_empty && right_is_empty){
            if (defense) current_score = -210000;
            else current_score = 50000;
        }
        else if (valid_range > 4){
            if (defense) current_score = -180000;
            else current_score = 1000;
        }
    }
    else if (len == 3){
        bool left_is_empty = (input[left+1] == '.'), right_is_empty = (input[right-1] == '.'); 
        if (left_is_empty){
            if (input[left+2] == input[4]){
                if (defense) current_score = -180000; //ooo.o
                else current_score = 1000;
            }
        }
        if (right_is_empty){
            if (input[left-2] == input[4]){         //o.ooo
                if (defense) current_score = -180000;
                else current_score = 1000;
            }
        }
        if (left_is_empty && right_is_empty){
            if (valid_range > 5){               //.ooo..
                if (defense) current_score = -18000;
                else current_score = 1000;
            }
            else {                            //.ooo.x
                if (defense) current_score = -60;
                else current_score = 25;
            }
        }
        else if (valid_range > 4){                              
            if (defense) current_score = -60;
            else current_score = 25;
        }
    }
    else if (len == 2){
	    left_three = right_three = false;
        bool left_is_empty = (input[left+1] == '.'), right_is_empty = (input[right-1] == '.'); 
        if (right_is_empty){
            if (input[right-2] == input[4]){
                if (input[right-3] == '.'){
                    if (input[left+1] == '.'){ // .o.oo.
                        if (defense) current_score = -18000;
                        else current_score = 1000;
                    }
                    else{           // .o.oox
                        if (defense) current_score = -60;
                        else current_score = 25;
                    }
                    right_three = true;
                }
                else if (input[right-3] == op){ // xo.oo.
                    if (input[left+1] == '.'){
                        if (defense) current_score = -60;
                        else current_score = 25;
                        left_three = true;
                    }
                }
            }
        }
        if (left_is_empty){
            if (input[left+2] == input[4]){
                if (input[left+3] == input[4]){  // oo.oo
                    if (defense) current_score = -180000;
                    else current_score = 1000;
                    left_three = true;
                }
                else if (input[left+3] == '.'){
                    if (right_is_empty){  //.oo.o.
                        if (defense) current_score = -18000;
                        else current_score = 1000;
                    }
                    else{ // xoo.o.
                        if (defense) current_score = -60;
                        else current_score = 25;
                    }
                    left_three = true;
                }
                else if (left_is_empty){ // .oo.ox
                    if (defense) current_score = -60;
                    else current_score = 25;
                    left_three = true;
                }
            }
        }
        if (left_three || right_three){}
        else if (left_is_empty && right_is_empty){ // .oo.
            if (defense) current_score = -60;
            else current_score = 25;
        }
        else if ((left_is_empty && input[right-2] == op)|| (right_is_empty && input[left+2] == op)){ //xoo., .oox
            if (defense) current_score = -3;
            else current_score = 1;
        }
    }
    else if (len == 1) {
        bool left_is_empty = (input[left+1] == '.'), right_is_empty = (input[right-1] == '.');
        if (right_is_empty){
            if (input[right-2] == input[4]){
                if (input[right-3] == '.'){
                    if (input[left+1] == op){  // .o.ox
                        if (defense) current_score = -3;
                        else current_score = 1;
                    }
                }
            }
        }
        if (left_is_empty){
            if (input[left+2] == input[4]){
                if (input[left+3] == '.'){
                    if (right_is_empty){// .o.o.
                        if (defense) current_score = -60;
                        else current_score = 25;
                    }
                    else if (valid_range > 4){// xo.o.
                        if (defense) current_score = -3;
                        else current_score = 1; 
                    }
                }
            }
            else if(input[left+2] == '.'){
                if (input[left+3] == input[4] && input[left+4] == '.'){  //.o..o.
                    if (defense) current_score = -60;
                    else current_score = 25;
                }
            }
        }
    }
    //cout << current_score << ' ';
    return current_score;
}

int heuristic(){
    string chess_road; 
    int score = 0;
    int dir[4][2] = {{1, 0}, {0, 1}, {1, 1}, {1, -1}};
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 15; j++)
            chess_place[i][j].reset();
    player_type[0] = ".", player_type[player] = "o", player_type[opp] = "x";
    for (int i = 0; i < SIZE; i++){
        for (int j = 0; j < SIZE; j++){
            if (board[i][j] == EMPTY) continue;
            for (int k = 0; k < 4; k++){
                string op = (player_type[board[i][j]] == "o")? "x" : "o";
                if (chess_place[k][i][j]) continue;
                chess_place[k][i][j] = true; 
                for (int l = -4; l <= 4; l++){
                    if (i+dir[k][0]*l >= 0 && i+dir[k][0]*l < SIZE && j+dir[k][1]*l >= 0 && j+dir[k][1]*l < SIZE)
                        chess_road += player_type[board[i+dir[k][0]*l][j+dir[k][1]*l]];
                    else
                        chess_road += op;
                }
                //cout << chess_road << '\n';
                int left = 5, right = 3, l = 5, r = 3;
                while (chess_road[left] == chess_road[4] && left <= 8){
                    chess_place[k][i+dir[k][0]*(left-4)][j+dir[k][1]*(left-4)] = true;
                    left++;
                }
                while (chess_road[right] == chess_road[4] && right >= 0){
                    chess_place[k][i+dir[k][0]*(right-4)][j+dir[k][1]*(right-4)] = true;
                    right--;
                }
                while ((chess_road[l] == chess_road[4] || chess_road[l] == '.') && l <= 8) l++;
                while ((chess_road[r] == chess_road[4] || chess_road[r] == '.') && r >= 0) r--;
                score += calculate_score(chess_road, left-1, right+1, l-r-1);
                chess_road.clear();
            }
        }
    }
    //cout << '\n';
    //cout << score << '\n';
    return score;
}
struct state{
    int score, new_x, new_y;
    int new_chess;
    int chess_left;
    state(){
        chess_left = new_x = new_y = score = new_chess = 0;
    }
    void set_on_board(int x, int y, int who){
        new_x = x, new_y = y, new_chess = who;
    }
};

vector<state> generate_all_move(int who){
    int dir[8][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}, {1, 1}, {1, -1}, {-1, 1}, {-1 ,-1}};
    vector<state> all_possible_move;
    for (int i = 0; i < SIZE; i++){
        for (int j = 0; j < SIZE; j++){
            //if (board[5][7]) cout << "g";
            if (board[i][j] == EMPTY){
                bool flag = false;
                for (int k = 0; k < 8; k++) if (dir[k][0]+i >= 0 && dir[k][0]+i < SIZE && dir[k][1]+j >= 0 && dir[k][1]+j < SIZE && board[dir[k][0]+i][dir[k][1]+j] != EMPTY) flag = true;
                if (flag) {
                    //if (board[5][7]) cout << "gggg\n";
                    state tmp;
                    tmp.set_on_board(i, j, who);
                    //cout << tmp.new_x << ' '<<tmp.new_y << '\n'; 
                    all_possible_move.emplace_back(tmp);
                }
            }
        }
    }
    return all_possible_move;
}

//(score, (x, y))
state alpha_beta(state current, int depth, int alpha, int beta, int who){
    int op = (who == 1)?2:1; 
    if (!depth || !current.chess_left){
        current.score = heuristic();
        //cout << '\n';
        //cout <<current.new_x << ' ' << current.new_y << ' ' <<current.score << '\n';
        return current;
    }
    vector<state> all_moves = generate_all_move(who);
    //cout << '\n';
    if (who == player){ //1 is max
        state  max_evaluate;
        max_evaluate.score = INT_MIN;
        for (auto node:all_moves){
            state evaluate;
            board[node.new_x][node.new_y] = who;
            node.chess_left--;
            //cout << "board:" <<board[5][7] << '\n';
            evaluate = alpha_beta(node, depth-1, alpha, beta, op);
            //evaluate.new_x = node.new_x, evaluate.new_y = node.new_y;
            board[node.new_x][node.new_y] = EMPTY;
            node.chess_left++;
            if (max_evaluate.score < evaluate.score){
                max_evaluate.new_x = node.new_x;
                max_evaluate.new_y = node.new_y;
                max_evaluate.score = evaluate.score;
                max_evaluate.new_chess = evaluate.new_chess;
            }
            //cout << "a : " << node.new_x << ' ' << node.new_y << ' ' << evaluate.score << '\n';
            alpha = max(alpha, max_evaluate.score);
            if (alpha >= beta) break;
        }
        return max_evaluate;
    }
    else {
        state min_evaluate;
        min_evaluate.score = INT_MAX;
        for (auto node:all_moves){
            state evaluate;
            board[node.new_x][node.new_y] = who;
            node.chess_left--;
            //cout << "board:" <<board[5][7] << '\n';
            evaluate = alpha_beta(node, depth-1, alpha, beta, op);
            //evaluate.new_x = node.new_x, evaluate.new_y = node.new_y;
            board[node.new_x][node.new_y] = EMPTY;
            node.chess_left++;
            if (min_evaluate.score > evaluate.score){
                min_evaluate.new_x = node.new_x;
                min_evaluate.new_y = node.new_y;
                min_evaluate.score = evaluate.score;
                min_evaluate.new_chess = evaluate.new_chess;
            }
            //cout << "b : "<< node.new_x << ' ' << node.new_y << ' ' << evaluate.score << '\n';
            beta = min(beta, min_evaluate.score);
            if (alpha >= beta) break;
        }
        return min_evaluate;
    }
}

void read_board(std::ifstream& fin) {
    fin >> player;
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            fin >> board[i][j];
        }
    }
}

void write_valid_spot(std::ofstream& fout) {
    int x, y, good = INT_MIN;
    while (1){
        bool flag = false; //check whether the board is empty
        state initial;
        state now; 
        int depth = 2;
        opp = (player == 1)?2:1;
        for (int i = 0; i < SIZE; i++){
            for (int j = 0; j < SIZE; j++){
                if (board[i][j] != EMPTY){
                    flag = true;
                    initial.chess_left++;
                }
            }
        }
        if (!flag) x = y = 7; //if is empty，choose the middle
        else {
            now = alpha_beta(initial, depth, INT_MIN, INT_MAX, player);
            x = now.new_x;
            y = now.new_y;
        }
        depth+=2;
        if (good < now.score && board[x][y] == EMPTY){
            good = now.score;
            fout << x << " " << y << std::endl;
        }
        // Remember to flush the output to ensure the last action is written to file.
        fout.flush();
        if (good > 1000000 || !flag){
            break;
        }
    }
}
 
int main(int, char** argv) {
    std::ifstream fin(argv[1]);
    std::ofstream fout(argv[2]);
    read_board(fin);
    write_valid_spot(fout);
    fin.close();
    fout.close();
    return 0;
}