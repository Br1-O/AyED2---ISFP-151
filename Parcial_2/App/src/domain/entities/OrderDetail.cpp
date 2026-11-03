#include "domain/entities/OrderDetail.hpp"

OrderDetail::OrderDetail(std::shared_ptr<Article> article, int quantity)
    : article(article), quantity(quantity) {}

double OrderDetail::calculateSubtotal() const {
    if (!article) return 0.0;
    return article->getUnitPrice() * quantity;
}

std::shared_ptr<Article> OrderDetail::getArticle() const { return article; }
int OrderDetail::getQuantity() const { return quantity; }