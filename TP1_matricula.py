# =============================================================================
# INSTRUÇÕES
# =============================================================================
# 1. Preencha as informações de identificação abaixo.
# 2. Escreva o código SQL para cada uma das 18 consultas nas variáveis designadas.
#    - As consultas de A1 a A5 são baseadas nas expressões em Álgebra Relacional.
#    - As consultas de B1 a B10 são baseadas nas perguntas em Linguagem Natural.
#    - As consultas de C1 a C3 são desafios em Linguagem Natural e valem
#      1 ponto extra no total.
# 3. Caso você não consiga resolver alguma das consultas, deixe a variável
#    correspondente em branco. O script gerará um arquivo de saída vazio para
#    essa consulta, sem interromper a execução das demais.
# 4. Salve o arquivo e o envie no Moodle.
# 5. NÃO altere o nome das funções, das variáveis de consulta ou dos arquivos de saída.
# =============================================================================

# DADOS DO ALUNO
NOME_ALUNO = "SEU NOME COMPLETO AQUI"
MATRICULA_ALUNO = "SUA MATRÍCULA AQUI"


# =============================================================================
# CÓDIGO DE PREPARAÇÃO DO AMBIENTE (NÃO ALTERAR)
# =============================================================================
import sqlite3
import pandas as pd

def salvar_consulta(query, filename):
    """Função auxiliar para executar a consulta e salvar o resultado em um arquivo de texto.
    Se a consulta estiver em branco (não preenchida), gera um arquivo de saída vazio."""

    # Verifica se a consulta foi preenchida. Remove comentários SQL (linhas com --),
    # espaços em branco e quebras de linha para checar se há de fato algum código SQL.
    linhas_sql = [
        linha.strip() for linha in query.split('\n')
        if linha.strip() and not linha.strip().startswith('--')
    ]
    if not linhas_sql:
        # Consulta em branco: gera arquivo vazio
        open(filename, 'w').close()
        print(f"Consulta para '{filename}' está em branco. Arquivo vazio gerado.")
        return

    try:
        # Conexão com o banco de dados
        con = sqlite3.connect('database.db')

        df = pd.read_sql_query(query, con)
        df.to_csv(filename, sep='|', index=False)
        print(f"Resultado para '{filename}' salvo com sucesso.")
        con.close()
    except Exception as e:
        # Garante que a conexão seja fechada mesmo em caso de erro
        if 'con' in locals() and con:
            con.close()
        # Em caso de erro, ainda gera um arquivo vazio para não interromper o fluxo
        open(filename, 'w').close()
        print(f"Ocorreu um erro na consulta para '{filename}': {e}")
        print(f"Arquivo vazio gerado para '{filename}'.")


# =============================================================================
# EXEMPLO DE PREENCHIMENTO (NÃO ALTERAR)
# =============================================================================
# A consulta abaixo serve apenas como exemplo de como preencher as variáveis de
# consulta. Ela não faz parte da avaliação. Note que o SQL é escrito entre as
# aspas triplas (""" ... """) e pode ocupar várias linhas.
#
# Pergunta de exemplo: Liste o nome e o estado dos 5 primeiros municípios
# cadastrados, em ordem alfabética por nome.
query_exemplo = """
SELECT nome, estado
FROM municipios
ORDER BY nome
LIMIT 5;
"""

# =============================================================================
# Consultas baseadas em Álgebra Relacional
# =============================================================================

# A1
query_a1 = """SELECT CD_DESCRICAO FROM cid10 WHERE CID = 'A15';
"""

# A2
query_a2 = """SELECT latitude, longitude
FROM municipios
WHERE nome = 'Porto Alegre'"""

# A3
query_a3 = """SELECT NOME_PROC
FROM procedimentos
where PROC_REA = '101010010';"""

# A4
query_a4 = """SELECT N_AIH, CD_DESCRICAO
FROM internacoes
JOIN cid10 ON DIAG_PRINC = CID
WHERE CNES = '2234416';"""

# A5
query_a5 = """SELECT nome, populacao
FROM municipios
JOIN dado_ibge on codigo_ibge = codigo_municipio_completo
WHERE estado = 'RS';"""

# =============================================================================
# Consultas baseadas em Linguagem Natural
# =============================================================================

# B1. Quantas internações foram registradas no total?
query_b1 = """SELECT COUNT(*)
FROM internacoes"""


# B2. Qual a idade média dos pacientes internados?
query_b2 = """SELECT AVG(IDADE)
FROM internacoes"""

# B3. Quantos municípios estão no estado do RS?
query_b3 = """SELECT COUNT(*)
FROM municipios
WHERE estado = 'RS'"""

# B4. Quantos casos de VDRL positivo foram registrados?
query_b4 = """SELECT COUNT(*)
FROM condicoes_especificas
WHERE IND_VDRL = '1'"""

# B5. Quantas internações duraram mais de 30 dias?
query_b5 = """SELECT COUNT(*)
FROM internacoes
WHERE QT_DIARIAS > 30"""

# B6. Qual a natureza, gestão e natureza jurídica do hospital com CNES '2234416'?
query_b6 = """SELECT NATUREZA, GESTAO, NAT_JUR
FROM hospital
where CNES = '2234416';"""

# B7. Qual município tem a maior população segundo os dados do IBGE?
query_b7 = """SELECT nome_municipio
FROM dado_ibge
ORDER BY populacao DESC LIMIT 1"""

# B8. Qual o diagnóstico mais comum nas internações?
query_b8 = """SELECT DIAG_PRINC, count(*)
FROM internacoes
GROUP BY DIAG_PRINC
ORDER BY count(*) DESC LIMIT 1"""

# B9. Quantas internações resultaram em óbito?
query_b9 = """SELECT COUNT(*)
FROM mortes"""

# B10. Quais as 10 principais causas de morte (com descrição)?
query_b10 = """SELECT CID, CD_DESCRICAO, count(*)
FROM cid10
JOIN mortes ON CID_MORTE = CID
GROUP BY CID
ORDER BY count(*) DESC LIMIT 10"""

# =============================================================================
# Consultas baseadas em Linguagem Natural - Desafios (1 ponto extra no total)
# =============================================================================

# C1. Quantos hospitais ficam em municípios com mais de 100 mil habitantes?
query_c1 = """SELECT COUNT(DISTINCT i.CNES)
FROM internacoes i
JOIN municipios m ON i.MUNIC_RES = m.codigo_6d
JOIN dado_ibge d ON m.codigo_ibge = d.codigo_municipio_completo
WHERE d.populacao > 100;"""

# C2. Quais hospitais tiveram mais de 1000 internações registradas?
query_c2 = """SELECT CNES
FROM internacoes
GROUP BY CNES
HAVING COUNT(*) > 1000;"""

# C3. Quais são as três causas de morte mais frequentes entre mulheres?
query_c3 = """SELECT c.CID, c.CD_DESCRICAO, COUNT(*)
FROM internacoes i
JOIN mortes m ON i.N_AIH = m.N_AIH
JOIN cid10 c ON m.CID_MORTE = c.CID
WHERE i.SEXO = 3
GROUP BY c.CID, c.CD_DESCRICAO
ORDER BY COUNT(*) DESC
LIMIT 3;"""


# =============================================================================
# EXECUÇÃO E SALVAMENTO (NÃO ALTERAR)
# =============================================================================
print("\nIniciando a execução e salvamento das consultas...")
salvar_consulta(query_exemplo, "output_exemplo.txt")
salvar_consulta(query_a1, "output_A1.txt")
salvar_consulta(query_a2, "output_A2.txt")
salvar_consulta(query_a3, "output_A3.txt")
salvar_consulta(query_a4, "output_A4.txt")
salvar_consulta(query_a5, "output_A5.txt")
salvar_consulta(query_b1, "output_B1.txt")
salvar_consulta(query_b2, "output_B2.txt")
salvar_consulta(query_b3, "output_B3.txt")
salvar_consulta(query_b4, "output_B4.txt")
salvar_consulta(query_b5, "output_B5.txt")
salvar_consulta(query_b6, "output_B6.txt")
salvar_consulta(query_b7, "output_B7.txt")
salvar_consulta(query_b8, "output_B8.txt")
salvar_consulta(query_b9, "output_B9.txt")
salvar_consulta(query_b10, "output_B10.txt")
salvar_consulta(query_c1, "output_C1.txt")
salvar_consulta(query_c2, "output_C2.txt")
salvar_consulta(query_c3, "output_C3.txt")
print("\nProcesso concluído.")
