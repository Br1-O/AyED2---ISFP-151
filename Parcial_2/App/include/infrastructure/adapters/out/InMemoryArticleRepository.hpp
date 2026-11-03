#ifndef IN_MEMORY_ARTICLE_REPOSITORY_HPP
#define IN_MEMORY_ARTICLE_REPOSITORY_HPP

#include <vector>
#include <optional>
#include <memory>
#include "domain/ports/out/IArticleRepository.hpp"

class InMemoryArticleRepository : public IArticleRepository {
private:
    std::vector<std::shared_ptr<Article>> articles;
    InMemoryArticleRepository();

public:
    static InMemoryArticleRepository& getInstance();

    void save(std::shared_ptr<Article> article) override;
    std::optional<std::shared_ptr<Article>> findById(int id) const override;
    std::vector<std::shared_ptr<Article>> findAll() const override;
};

#endif