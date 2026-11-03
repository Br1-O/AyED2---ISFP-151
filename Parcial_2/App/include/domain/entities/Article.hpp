#ifndef ARTICLE_HPP
#define ARTICLE_HPP

#include <string>

class Article {
private:
    int id;
    std::string name;
    double unitPrice;
    int stock;
public:
    Article(int id, std::string name, double unitPrice, int stock);

    int getId() const;
    std::string getName() const;
    double getUnitPrice() const;
    int getStock() const;
};

#endif