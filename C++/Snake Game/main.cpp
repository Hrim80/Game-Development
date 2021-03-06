#include <iostream>
#include <stdio.h>
#include <termios.h>
#include <unistd.h>
#include <fcntl.h>
using namespace std;
bool gameOver;   //Global variable
//Constant values are the dimensions of the map
const int width = 20;
const int height = 20;
//X, Y are the cordinates of head position, fruitX,Y variable of fruit position
int x,y, fruitX, fruitY, score;
enum eDirection {STOP = 0, LEFT, RIGHT, UP, DOWN};
eDirection dir;

//Every Game should Have These Functions Setup, Draw, Input, Logic
void Setup()
{
    gameOver = false;
    dir = STOP;
    x = width / 2;
    y = height / 2;
    fruitX = rand() % width;
    fruitY = rand() % height;
    score = 0;
}
void Draw()
{
    system("clear");
    for(int i = 0; i < width; i++)
        cout << "#";
    cout << endl;

    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            if (j==0)
                cout << "#";

            else if (j == width-1)
                cout << "#";

            else if (i == y && j == x)
                cout << "0";

            else if (i == fruitY && j == fruitX)
                cout << "F";

            else
                cout << " ";
        }
        cout << endl;
    }

    for(int i = 0; i < width; i++)
        cout << "#";
    cout << endl;
}
void Input()
{
    if (_kbhit())
    {
        switch (_getch())
        {
            case "a":
                dir = LEFT;
                break;

            case "d":
                dir = RIGHT;
                break;

            case "w":
                dir = UP;
                break;

            case "s":
                dir = DOWN;
                break;

            case  "x":
                gameOver = true;
                break;
        }
    }
}
void Logic()
{
    switch (dir)
    {
        case LEFT:
            x--;
            break;

        case RIGHT:
            x++;
            break;

        case UP:
            y--;
            break;

        case DOWN:
            y++;
            break;
    }
}
int main() {
    Setup();
    while(!gameOver)
    {
        Draw();
        Input();
        Logic();
        //sleep(10);
    }
    return 0;
}
