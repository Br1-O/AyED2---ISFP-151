#ifndef I_ARTICLE_REPOSITORY_HPP
#define I_ARTICLE_REPOSITORY_HPP

#include <vector>
#include <optional>
#include <memory>
#include "domain/entities/Article.hpp"

class IArticleRepository {
public:
    virtual ~IArticleRepository() = default;
    virtual void save(std::shared_ptr<Article> article) = 0;
    virtual std::optional<std::shared_ptr<Article>> findById(int id) const = 0;
    virtual std::vector<std::shared_ptr<Article>> findAll() const = 0;
};

#endif