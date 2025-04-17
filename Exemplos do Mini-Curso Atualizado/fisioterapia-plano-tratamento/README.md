# Projeto de Recomendação de Tratamento em Fisioterapia

Este projeto tem como objetivo desenvolver um sistema que recomenda planos de tratamento em fisioterapia adaptados para diferentes pacientes, levando em consideração suas características individuais.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

```
fisioterapia-plano-tratamento
├── src
│   ├── main.py                # Ponto de entrada da aplicação
│   ├── services
│   │   ├── recomendacao.py    # Geração de planos de tratamento personalizados
│   │   └── calculos.py        # Funções de cálculos necessários
│   ├── models
│   │   └── paciente.py         # Definição da classe Paciente
│   └── utils
│       └── helpers.py         # Funções utilitárias
├── tests
│   ├── test_recomendacao.py   # Testes unitários para a classe Recomendacao
│   ├── test_calculos.py       # Testes unitários para funções de cálculo
│   └── test_paciente.py       # Testes unitários para a classe Paciente
├── requirements.txt            # Dependências do projeto
└── README.md                   # Documentação do projeto
```

## Instalação

Para instalar as dependências do projeto, execute o seguinte comando:

```
pip install -r requirements.txt
```

## Uso

Para executar o sistema, utilize o seguinte comando:

```
python src/main.py
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.