#pragma once
#include "Character.h"
#include "Item.h"
#include <stdlib.h>
#include <vector>

class Game{

    public:
    Game();
    virtual ~Game();

    inline bool getPlaying () const{return this->playing;}

    void InitGame();
    void MainMenu();
    void viewShop();
    void InitializeShop();
    void PrintShop();
    Character _Character;
    std::vector<Item*> _Shop;



    private:

    bool playing;
};