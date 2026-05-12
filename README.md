# Trabalho Prático 1 - Introdução a Bancos de Dados (TP1 - IBD)

Este repositório contém a resolução do Trabalho Prático 1, focado no uso de Bancos de Dados Relacionais (SQLite) e na construção de consultas SQL a partir de especificações em Álgebra Relacional e Linguagem Natural.

O tema principal do banco de dados abrange dados da área da saúde, incluindo hospitais, diagnósticos (CID-10), municípios, dados do IBGE, internações e mortalidades.

## Estrutura do Repositório

- **`tp1.ipynb`**: Notebook Jupyter utilizado para prototipação e testes. Contém os passos para a criação das tabelas e comandos de inserção de dados fictícios para testar as consultas localmente.
- **`TP1_matricula.py`**: Arquivo Python principal que deve ser preenchido com as resoluções finais. Contém as variáveis de consultas (Blocos A, B e C), scripts para execução no banco e salvamento dos resultados em arquivos.
- **`database.db`**: Banco de dados SQLite criado dinamicamente ao executar o notebook para validação e testes.

## Como Executar

### 1. Criando e testando o Banco de Dados (Ambiente de Testes)
Abra e execute as células do arquivo `tp1.ipynb`:
1. Instalação de dependências e configuração;
2. Script de `CREATE TABLE` (salva automativamente o `database.db`);
3. Inserção de dados (`INSERT OR IGNORE`) para verificar fisicamente como as tabelas interagem.
4. Experimentação das consultas com banco integrado via `pandas`.

### 2. Rodando o Script de Entrega
Após testar as _queries_ no Jupyter, insira as respostas nas respectivas variáveis no arquivo `TP1_matricula.py`.

Ao rodar esse arquivo Python interativo, ele lerá o banco local (`database.db`) e exportará todos os arquivos txt resultantes das respostas SQL.
```bash
python TP1_matricula.py
```
*(Isso validará os resultados gerando arquivos individuais de `output_A1.txt` até `output_C3.txt`)*

## Sobre as Consultas

As consultas do trabalho estão divididas em:
- **Parte A (A1 a A5):** Expressões de Álgebra Relacional para conversão em linguagem SQL (Projeção e Seleção).
- **Parte B (B1 a B10):** Consultas baseadas na Linguagem Natural, envolvendo junções (JOIN), agregações matemáticas (COUNT, AVG, GROUP BY) e condições de filtragem.
- **Parte C (Desafios C1 a C3):** Consultas complexas usando dados de diferentes domínios e cruzamentos avançados.

## Tecnologias Utilizadas
- **Linguagem:** Python
- **Banco de Dados:** SQLite (`sqlite3`)
- **Visualização de Testes:** Pandas
- **Ambiente:** Jupyter Notebook / Visual Studio Code