#ifndef SUPPLIER_HPP
#define SUPPLIER_HPP

#include <string>

class Supplier {
private:
    int id;
    std::string name;
    std::string cuit;
    std::string email;
public:
    Supplier(int id, std::string name, std::string cuit, std::string email);

    int getId() const;
    std::string getName() const;
    std::string getCuit() const;
    std::string getEmail() const;

    void setId(int id);
    void setName(const std::string& name);
    void setCuit(const std::string& cuit);
    void setEmail(const std::string& email);
};

#endif