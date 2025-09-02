import pandas as pd
import matplotlib.pyplot as plt
import sys

nome_arquivo_entrada = '../result/resultado_filtrado.xlsx'
coluna_para_analise = 'Sigla_Partido'
coluna_do_projeto = 'Projano'


def criar_salvar_grafico(dataframe, titulo_grafico, nome_arquivo_saida):
    if dataframe.empty:
        print(f"AVISO: Nenhum dado para gerar o gráfico '{titulo_grafico}'.")
        return

    contagem_partidos = dataframe[coluna_para_analise].value_counts()

    plt.figure(figsize=(12, 7))
    contagem_partidos.plot(kind='bar', color='teal')

    plt.title(titulo_grafico, fontsize=16)
    plt.ylabel('Número de Votos', fontsize=12)
    plt.xlabel('Partido', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    caminho_de_saida = f'../result/{nome_arquivo_saida}'
    plt.savefig(caminho_de_saida)

    print(f"SUCESSO: O gráfico '{nome_arquivo_saida}' foi salvo na pasta 'result'.")
    plt.close()


try:
    print(f"Lendo o arquivo de dados: '{nome_arquivo_entrada}'...")
    df_geral = pd.read_excel(nome_arquivo_entrada)
    print("Arquivo lido com sucesso.\n")

    criar_salvar_grafico(df_geral,
                         'Contagem Geral de Votos por Partido',
                         'grafico_geral_partidos.png')

    df_mpv0571 = df_geral[df_geral[coluna_do_projeto] == 'MPV0571/12']
    criar_salvar_grafico(df_mpv0571,
                         'Contagem de Votos por Partido (MPV0571/12)',
                         'grafico_MPV0571_12_partidos.png')

    df_mpv0809 = df_geral[df_geral[coluna_do_projeto] == 'MPV0809/17']
    criar_salvar_grafico(df_mpv0809,
                         'Contagem de Votos por Partido (MPV0809/17)',
                         'grafico_MPV0809_17_partidos.png')

except FileNotFoundError:
    sys.exit(f"ERRO: O arquivo de entrada '{nome_arquivo_entrada}' não foi encontrado.")
except Exception as e:
    sys.exit(f"ERRO: Ocorreu um erro inesperado: {e}")