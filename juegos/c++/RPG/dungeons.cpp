
#include "dungeons.h"
#include "Game.cpp"
#include "Character.cpp"
#include "Item.cpp"
#include "Functions.h"

using namespace std;



int main(){
    while(!__kbhit()){
        Inicio();
        usleep(20000);
    }
start:
    Game game;
    while(game.getPlaying()){
        MainMenu();
        switch (opc_pulsada)
        {
        case 1:
            break;
        case 2:
            View_credits();
            opc_pulsada = 0;
            goto start;
            break;
        case 3:
            goto end;
        default:
            break;
        }
        //InitIntro();
        game.InitGame();
        usleep(80000);
    }
    goto start;
end:
    system("clear");
    return 0;
}