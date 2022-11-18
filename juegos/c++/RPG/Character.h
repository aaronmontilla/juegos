#pragma once

class Character{
    
public:

    Character();
    virtual ~Character();


    //Function

    void initialize(int level, string name);
    const string getAsString();

    //Accesors

    inline const string& getName (){return this->name;};
    inline const int& getRole (){return this->role;};
    inline const int& getLevel (){return this->level;};
    inline const int& getAttack (){return this->attack;};
    inline const int& getDefence (){return this->defence;};
    inline const int& getExp (){return this->exp;};
    inline const int& getExpNext (){return this->expNext;};
    inline const double& getXPos (){return this->xPos;};
    inline const double& getYPos (){return this->yPos;};
    inline const int& getHp (){return this->hp;};
    inline const int& getHpMax (){return this->hpMax;};
    inline const int& getDamageMin (){return this->damageMin;};
    inline const int& getDamageMax (){return this->damageMax;};

private:

    string name;
    double money;
    int role;
    int level;
    int attack;
    int defence;
    int exp;
    int expNext;
    double xPos;
    double yPos;
    int hp;
    int hpMax;
    int damageMin;
    int damageMax;
    
};
