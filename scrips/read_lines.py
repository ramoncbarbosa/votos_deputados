import csv

nome_do_arquivo = '../datasets/votos_dep_fed_CEBRAP.csv'
total_de_linhas = 0

print(f"Contando as linhas no arquivo: {nome_do_arquivo}...")

try:
    with open(nome_do_arquivo, 'r', encoding='latin-1') as f:
        leitor_csv = csv.reader(f)
        for linha in leitor_csv:
            total_de_linhas += 1

    print("\n--- Resultado da Contagem com Python Puro ---")
    print(f"Contagem finalizada!")
    print(f"O arquivo tem um total de {total_de_linhas:,} linhas (incluindo o cabeçalho).")
    print(f"Isso corresponde a {total_de_linhas - 1:,} linhas de dados.")

except Exception as e:
    print(f"\nOcorreu um erro ao tentar ler o arquivo: {e}")