#include <stdio.h>
#include <iostream>
using namespace std;

int check(int arr[9][10])
{
	for (int i = 0; i < 6; i++) 
	{
		for (int j = 0; j < 7; j++)
		{
			if (arr[i][j] != 0) 
			{
				if (arr[i][j] == arr[i][j + 1] && arr[i][j] == arr[i][j + 2] && arr[i][j] == arr[i][j + 3]) return arr[i][j];
				else if (arr[i][j] == arr[i + 1][j] && arr[i][j] == arr[i + 2][j] && arr[i][j] == arr[i + 3][j]) return arr[i][j];
				else if (arr[i][j] == arr[i + 1][j + 1] && arr[i][j] == arr[i + 2][j + 2] && arr[i][j] == arr[i + 3][j + 3]) return arr[i][j];
			}
		}
	}
	for (int i = 5; i != 0; i--) 
	{
		for (int j = 0; j < 4; j++)
		{
			if (arr[i][j] != 0)
			{
				if (arr[i][j] == arr[i - 1][j + 1] && arr[i][j] == arr[i - 2][j + 2] && arr[i][j] == arr[i - 3][j + 3]) return arr[i][j];
			}
		}
	}
	return 0;
}
int main() 
{
	int arr[9][10] = { 0 };
	int tmp, player = 1;
	while (1)
	{
		cout << " 1 2 3 4 5 6 7" << endl;
		cout << "¢w ¢w ¢w ¢w ¢w¢w ¢w ¢w " << endl;
		for (int i = 0; i < 6; i++) 
		{
			for (int j = 0; j < 7; j++) 
			{
				cout << "|";
				if (arr[i][j] == 1) 
				{
					cout << "o";
				}
				else if (arr[i][j] == 2)
				{
					cout << "x";
				}
				else 
				{
					cout << " ";
				}
			}
			cout << "|" << endl;
			cout << "¢w ¢w ¢w ¢w ¢w¢w ¢w ¢w " << endl;
		}
		if (check(arr) != 0) 
		{
			cout << "player " << check(arr) << " WIN!";
			return 0;
		}
		cout << "player " << player << "'s turn" << endl;
		
		while (1)
		{
			cin >> tmp;
			if (arr[0][tmp - 1] != 0)
			{
				cout << "This column is full" << endl;
			}
			else if (tmp > 7 || tmp < 1)
			{
				cout << "Column choosed not exist" << endl;
			}
			else
				break;

		}
		for (int i = 0; i < 7; i++)
		{
			if (arr[i][tmp - 1] == 0 && i != 6)continue;
			else 
			{
				arr[i - 1][tmp - 1] = player;
				break;
			}
		}
		if (player == 2)player = 1;
		else player = 2;
	}
}
