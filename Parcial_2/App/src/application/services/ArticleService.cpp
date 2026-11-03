#include "application/services/ArticleService.hpp"

ArticleService::ArticleService(std::shared_ptr<IArticleRepository> articleRepo) 
    : articleRepo(articleRepo) {}

void ArticleService::registerArticle(int id, const std::string& name, double price, int stock) {
    auto article = std::make_shared<Article>(id, name, price, stock);
    articleRepo->save(article);
}

std::vector<std::shared_ptr<Article>> ArticleService::getAllArticles() const {
    return articleRepo->findAll();
}

std::optional<std::shared_ptr<Article>> ArticleService::getArticleById(int id) const {
    return articleRepo->findById(id);
}