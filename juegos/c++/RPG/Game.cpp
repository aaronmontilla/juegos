#include "Game.h"

using namespace std;

Game::Game(){
    playing = true;
    InitializeShop();
}

Game::~Game(){

}

void Game::viewShop(){
    int option;
    while(option != 3){
        system("clear");
        cout << "Bienvenido a la tienda" << endl;
        cout << "En que te podemos ayudar hoy" << endl;
        cout << "1. Comprar" << endl;
        cout << "2. Vender" << endl;
        cout << "3. Salir" << endl;
        cin >> option;

        switch (option)
        {
        case 1:
            PrintShop();
            break;
        case 2:
            cout << "Opening the store";
            break;
        case 3:
            return;
        default:
            break;
        }
    }
}

void Game::InitGame(){

    string name;
    cout << "Welcome new traveller what is your name?\n Name:";
    cin >> name;
    system("clear");
    cout << name << "? it is the first time I hear that name\n";
    _Character.initialize(1,name);
    cout <<"Well, what do you want to do now?\n";
    int option;
    while(option != 3){
        cout << "1. Ver tienda" << endl;
        cout << "2. Ver estadísticas de personaje" << endl;
        cout << "3. Salir" << endl;

        cin >> option;

        switch (option)
        {
        case 1:
            viewShop();
            break;
        case 2:
            cout << _Character.getAsString();
            break;
        case 3:
            return;
        default:
            break;
        }
    }
}

void Game::InitializeShop(){
    Shop.push_back(new GoldenSword);
    Shop.push_back(new HolySword);
    Shop.push_back(new Wood_Sword);
}

void Game::PrintShop(){
    cout << "Item\tPrice\tAttack\tMagic Power" << endl;
    for(auto &item : Shop){
        item->printAttributes();
    }
}