#pragma once

class Item{
    
public:

    Item();
    virtual ~Item();

    int rarity;
    int price;
    string name;
    char owner[10];
    virtual void printAttributes(){
        cout<< "Print sin definir" << endl;
    }

};

struct WeaponsAttributes{
    int Attack;
    int MagicPower;
};

class Weapon: public Item
{
    
     
    public:
    struct WeaponsAttributes attributes;
    virtual void  printAttributes()override{
        cout << this->name << "\t" << this->price << "\t" << attributes.Attack << "\t" <<attributes.MagicPower << endl;
    };

};

class HolySword: public Weapon
{
    public:
    HolySword();
};

class GoldenSword: public Weapon
{
    public:
    GoldenSword();
};

class Wood_Sword : public Weapon
{
    
    public:
    Wood_Sword();
};