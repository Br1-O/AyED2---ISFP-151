#ifndef ARTICLE_SERVICE_HPP
#define ARTICLE_SERVICE_HPP

#include <memory>
#include <vector>
#include <optional>
#include "domain/entities/Article.hpp"
#include "domain/ports/out/IArticleRepository.hpp"

class ArticleService {
private:
    std::shared_ptr<IArticleRepository> articleRepo;
public:
    explicit ArticleService(std::shared_ptr<IArticleRepository> articleRepo);

    void registerArticle(int id, const std::string& name, double price, int stock);
    std::vector<std::shared_ptr<Article>> getAllArticles() const;
    std::optional<std::shared_ptr<Article>> getArticleById(int id) const;
};

#endif