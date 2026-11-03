#include "infrastructure/adapters/out/InMemoryArticleRepository.hpp"

InMemoryArticleRepository::InMemoryArticleRepository() = default;

InMemoryArticleRepository& InMemoryArticleRepository::getInstance() {
    static InMemoryArticleRepository instance;
    return instance;
}

void InMemoryArticleRepository::save(std::shared_ptr<Article> article) {
    articles.push_back(article);
}

std::optional<std::shared_ptr<Article>> InMemoryArticleRepository::findById(int id) const {
    for (const auto& a : articles) {
        if (a->getId() == id) return a;
    }
    return std::nullopt;
}

std::vector<std::shared_ptr<Article>> InMemoryArticleRepository::findAll() const {
    return articles;
}