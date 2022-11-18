#include "Item.h"

Item::Item(){

}
    
Item::~Item(){

}

Wood_Sword::Wood_Sword(){
    this->name = "Wood Sword";
    this->price = 30;
    this->rarity = 1;
    this->attributes.Attack = 30;
    this->attributes.MagicPower = 10;
}

HolySword::HolySword(){
    this->name = "Holy Sword";
    this->price = 200;
    this->rarity = 5;
    this->attributes.Attack = 150;
    this->attributes.MagicPower = 70;
}

GoldenSword::GoldenSword(){
    this->name = "Golden Sword";
    this->price = 5000;
    this->rarity = 10;
    this->attributes.Attack = 300;
    this->attributes.MagicPower = 250;
}