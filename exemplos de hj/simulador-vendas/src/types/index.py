# filepath: simulador-vendas/simulador-vendas/src/types/index.py

# Este arquivo contém definições de tipos e interfaces para o projeto.

from typing import Dict, Any

# Definição de tipo para produtos
Product = Dict[str, Any]

# Definição de tipo para pacotes
Package = Dict[str, Any]

# Definição de tipo para estratégias de marketing
MarketingStrategy = Dict[str, Any]

# Estrutura de dados para armazenar produtos
products: Dict[str, Product] = {
    "Produto Exemplo": {
        "preco": 0.0,
        "margem": 0.0
    }
}

# Estrutura de dados para armazenar pacotes
packages: Dict[str, Package] = {
    "Pacote Exemplo": {
        "itens": {},
        "desconto": 0.0,
        "marketing": ""
    }
}

# Estrutura de dados para armazenar estratégias de marketing
marketing_strategies: Dict[str, MarketingStrategy] = {
    "Estratégia Exemplo": {
        "descricao": "",
        "urgencia": False
    }
}