import os
import pandas as pd

nome_do_arquivo_entrada = 'votos_dep_fed_CEBRAP.csv'
nome_do_arquivo_saida = 'resultado_filtrado.xlsx'

print(f"--- Iniciando processo para o arquivo: {nome_do_arquivo_entrada} ---\n")

try:
    print("Carregando o arquivo, aguarde...")

    df = pd.read_csv(nome_do_arquivo_entrada, engine='python', encoding='latin-1')

    print(f"SUCESSO! O arquivo foi carregado por completo.")
    print(f"O DataFrame contém {df.shape[0]:,} linhas e {df.shape[1]} colunas.")

    print("\n--- Aplicando filtros em todos os 1,47 milhão de registros...")

    filtro_base = (df['Procedimento'] == 'DVS') & (df['Tipo_Projeto'] == 'MPV')
    filtro_projano = df['Projano'].isin(['MPV0571/12', 'MPV0809/17'])
    df_filtrado = df[filtro_base & filtro_projano]

    print(f"Filtro aplicado! Foram encontrados {len(df_filtrado)} registros que correspondem aos critérios.")

    if not df_filtrado.empty:
        print(f"\n--- Exportando o resultado para '{nome_do_arquivo_saida}'...")

        df_filtrado.to_excel(nome_do_arquivo_saida, index=False)

        print(f"SUCESSO! O arquivo '{nome_do_arquivo_saida}' foi criado.")
        print("  Ele contém o resultado exato do filtro e pode ser aberto no Excel sem problemas.")
    else:
        print("\nAVISO: Nenhum dado encontrado após o filtro. O arquivo de saída não foi criado.")

except FileNotFoundError:
    print(f"ERRO: O arquivo de entrada '{nome_do_arquivo_entrada}' não foi encontrado.")
except Exception as e:
    print(f"\n ERRO ao processar o arquivo: {e}")