# Análise de Votos de Deputados Federais

<p align="center">
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Matplotlib-grey?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib">
  <img src="https://img.shields.io/badge/OpenPyXL-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white" alt="OpenPyXL">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  <img src="https://img.shields.io/badge/Git_LFS-000000?style=for-the-badge&logo=git-lfs&logoColor=white" alt="Git LFS">
</p>




Este projeto analisa o dataset de votações de deputados federais (CEBRAP) para filtrar dados e gerar visualizações gráficas sobre o posicionamento de partidos em votações específicas, como Medidas Provisórias.

---

## 📋 Índice

* [Sobre o Projeto](#-sobre-o-projeto)
* [Tecnologias Utilizadas](#-tecnologias-utilizadas)
* [Como Instalar e Executar](#-como-instalar-e-executar)
    * [Pré-requisitos](#pré-requisitos)
    * [Instalação](#instalação)
* [Uso](#-uso)
* [Estrutura do Projeto](#-estrutura-do-projeto)
* [Fonte dos Dados](#-fonte-dos-dados)
* [Licença](#-licença)

---

## 📊 Sobre o Projeto

A análise de dados políticos pode ser complexa devido ao grande volume de informações. Este projeto foi criado para simplificar esse processo, oferecendo scripts para:
* Filtrar a base de dados massiva de votos com base em critérios específicos.
* Gerar arquivos de saída limpos nos formatos `.csv` e `.xlsx`.
* Criar visualizações gráficas (`.png`) que demonstram o comportamento dos partidos em votações nominais importantes.

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando as seguintes tecnologias:

* **Linguagem:** Python 3.x
* **Bibliotecas Principais:** Pandas, Matplotlib, NumPy * **Versionamento:** Git & Git LFS

---

## ⚙️ Como Instalar e Executar

Siga os passos abaixo para ter uma cópia do projeto rodando localmente.

### Pré-requisitos

* [Python 3.8+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads)
* [Git LFS](https://git-lfs.github.com) (essencial para baixar o dataset)

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/ramoncbarbosa/votos_deputados_federais_cebrap.git](https://github.com/ramoncbarbosa/votos_deputados_federais_cebrap.git)
    cd votos_deputados_federais_cebrap
    ```
    2.  **Baixe o arquivo grande com Git LFS:**
    Após a clonagem, o arquivo `.csv` será apenas um ponteiro. Rode este comando para baixar o arquivo real:
    ```bash
    git lfs pull
    ```

3.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    # Criar o ambiente
    python -m venv .venv

    # Ativar no Windows (PowerShell)
    .\.venv\Scripts\Activate.ps1
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 Uso

O projeto é dividido em scripts principais localizados na pasta `scrips/`.

1.  **Filtrar os Dados:**
    Execute o script `filter.py` para processar o dataset bruto e gerar os arquivos `resultado_filtrado.csv` e `resultado_filtrado.xlsx` na pasta `result/`.
    ```bash
    python scrips/filter.py
    ```
    2.  **Gerar os Gráficos:**
    Após filtrar os dados, execute o script `graph.py` para gerar os gráficos de análise de votos na pasta `result/`.
    ```bash
    python scrips/graph.py
    ```
    ---

## 📁 Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
└── 📁votos_deputados_federais_cebrap
    ├── 📁datasets
    │   └── votos_dep_fed_CEBRAP.csv  # Dataset bruto (gerenciado pelo Git LFS)
    │
    ├── 📁result
    │   ├── grafico_geral_partidos.png    # Gráficos de saída gerados
    │   ├── grafico_MPV0571_12_partidos.png
    │   ├── grafico_MPV0809_17_partidos.png
    │   ├── resultado_filtrado.csv      # Dados filtrados em formato CSV
    │   └── resultado_filtrado.xlsx     # Dados filtrados em formato Excel
    │
    ├── 📁scrips
    │   ├── filter.py                   # Script para filtrar os dados
    │   ├── graph.py                    # Script para gerar os gráficos
    │   └── read_lines.py               # Script auxiliar de leitura
    │
    ├── .gitattributes                  # Arquivo de configuração do Git LFS
    ├── .gitignore                      # Arquivos e pastas a serem ignorados pelo Git
    ├── README.md                       # Descrição
    └── requirements.txt                # Lista de dependências Python
```

---

## 💾 Fonte dos Dados

O dataset principal, `votos_dep_fed_CEBRAP.csv`, foi obtido do **CEBRAP (Centro Brasileiro de Análise e Planejamento)**.

* **Link para os dados:** [[CEBRAP](https://bancodedadoslegislativos.com.br/downloads.php)]
* **Data da Extração:** Agosto de 2025

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---