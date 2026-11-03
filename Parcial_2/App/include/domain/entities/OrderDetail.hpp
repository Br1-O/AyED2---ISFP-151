#ifndef ORDER_DETAIL_HPP
#define ORDER_DETAIL_HPP

#include <memory>
#include "Article.hpp"

class OrderDetail {
private:
    std::shared_ptr<Article> article;
    int quantity;
public:
    OrderDetail(std::shared_ptr<Article> article, int quantity);
    double calculateSubtotal() const;
    std::shared_ptr<Article> getArticle() const;
    int getQuantity() const;
};

#endif