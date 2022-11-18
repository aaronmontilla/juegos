#ifndef FUNCTIONS_H
#define FUNCTIONS_H
#pragma once
#include "stdio.h"
#include <iostream>
#include "unistd.h"
#include "conio.h"
#include <sys/ioctl.h>
#include <termios.h>


bool __kbhit()
{
    termios term;
    tcgetattr(0, &term);

    termios term2 = term;
    term2.c_lflag &= ~ICANON;
    tcsetattr(0, TCSANOW, &term2);

    int byteswaiting;
    ioctl(0, FIONREAD, &byteswaiting);

    tcsetattr(0, TCSANOW, &term);

    return byteswaiting > 0;
}

using namespace std;
int opc_sel = 1;
int opc_pulsada = 0;


void Inicio(){
    system("clear");
    cout <<"###############################" << endl;
    cout <<"#                             #" << endl;
    cout <<"#      WELCOME TO D&D         #" << endl;
    cout <<"#           AMV               #" << endl;
    cout <<"#                             #" << endl;
    cout <<"###############################" << endl;
}

void View_credits(){
    system("clear");
    cout <<"This game was directed and produced by AMV" << endl;
    sleep(2);
    return;
}

void InitIntro(){

        system("clear");
        cout << "Este es el comienzo de tu historia" << endl;
        sleep(2);
        cout << "Te encontrarás grandes enemigos por el camino" << endl;
        sleep(2);
        cout << "Deja que tu corazón te guíe hasta tú destino" << endl;
        sleep(2);
        cout << "Buena suerte" << endl;
        sleep(2);
        return;
}

void MainMenu(){
    opc_pulsada = 0;
    while(1){
        system("clear");
        if (opc_sel == 1)
            cout << "--> ";
        cout << "Iniciar juego" << endl;
        if (opc_sel == 2)
            cout << "--> ";
        cout << "Ver créditos" << endl;
        if (opc_sel == 3)
            cout << "--> ";
        cout << "Salir del juego" << endl;
        if(__kbhit()){
            switch (getch())
            {
            case 's':
                if (opc_sel == 3){
                    opc_sel = 1;
                } else{
                    opc_sel++;
                }
                break;
            case 'w':
                if (opc_sel == 1){
                    opc_sel = 3;
                } else{
                    opc_sel--;
                }
                break;
            case 'c':
                opc_pulsada = opc_sel;
                break;
            default:
                break;
            }
        }
        usleep(40000);
        if(opc_pulsada != 0){
            break;
        }
    }
}

#endif 
