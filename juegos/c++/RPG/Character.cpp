#include "Character.h"
#include "Functions.h"


Character::Character(){
    this->name = "";
    this->level = 0;
    this->role = 0;
    this->level= 0;
    this->attack = 0;
    this->defence = 0;
    this->exp = 0;
    this->expNext = 0;
    this->hp = 0;
    this->hpMax = 0;
    this->damageMin = 0;
    this->damageMax = 0;
}

Character::~Character(){
}

void Character::initialize(int level, const string name){
    this->name = name;
    this->level = level;
    this->role = 1;
    this->attack = 1;
    this->defence = 1;
    this->exp = 0;
    this->expNext = level*100;
    this->hp = 10;
    this->hpMax = 10;
    this->damageMin = 2;
    this->damageMax = 4;
}

const string Character::getAsString (){
    cout << "-------------------" << endl;
    cout << "Stats of this Character" << endl;
    cout << "Name: " << this->name << endl;
    cout << "Level: " << this->level << endl;
    cout << "Role: " << this->role << endl;
    cout << "Attack: " << this->attack << endl;
    cout << "Defence: " << this->defence << endl;
    cout << "Exp: " << this->exp << "/" << this->expNext << endl;
    cout << "HP: " << this->hp << "/" << this->hpMax << endl;
    cout << "-------------------" << endl;
}