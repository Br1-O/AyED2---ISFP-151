#include "domain/entities/Article.hpp"

Article::Article(int id, std::string name, double unitPrice, int stock)
    : id(id), name(name), unitPrice(unitPrice), stock(stock) {}

int Article::getId() const 
{ 
    return id; 
}

std::string Article::getName() const 
{ 
    return name; 
}

double Article::getUnitPrice() const 
{ 
    return unitPrice; 
}

int Article::getStock() const 
{ 
    return stock; 
}