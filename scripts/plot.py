import math
import csv
import pandas as pd
import matplotlib.pyplot as plt


def calculate_complexities(n: int) -> dict:
        
    log_n = math.log2(n)
    n_log_n = n * log_n
    n_squared = n ** 2
    #n_cubed = n ** 3
    #two_to_n = 2 ** n
    #n_factorial = math.factorial(n)

    return {
        "O(log n)": log_n,
        "O(n)": n,
        "O(n log n)": n_log_n,
        "O(n^2)": n_squared,
        #"O(n^3)": n_cubed,
        #"O(2^n)": two_to_n,
        #"O(n!)": n_factorial
    }


#--------------------------------------------------------------

def plot_complexities_from_csv(file_name: str = "complexidades.csv"):
  
    try:
        # Carrega os dados do arquivo CSV
        df = pd.read_csv(file_name)
        
        print(f"Dados do arquivo '{file_name}' carregados com sucesso.")
        print("\nInformações do DataFrame:")
        df.info()
        
        # Criar uma figura e um subplot
        fig, ax1 = plt.subplots(figsize=(12, 8))

        # Plot das complexidades
        ax1.plot(df['n'], df['O(log n)'], label=r'$O(\log n)$')
        ax1.plot(df['n'], df['O(n)'], label=r'$O(n)$')
        ax1.plot(df['n'], df['O(n log n)'], label=r'$O(n \log n)$')
        ax1.plot(df['n'], df['O(n^2)'], label=r'$O(n^2)$')
        #ax1.plot(df['n'], df['O(n^3)'], label=r'$O(n^3)$') # Para n > 5, as próximas linhas tornão o gráfico ilegível
        #ax1.plot(df['n'], df['O(2^n)'], label=r'$O(2^n)$')
        #ax1.plot(df['n'], df['O(n!)'], label=r'$O(n!)$')
        ax1.set_xlabel(r'Tamanho da Entrada ($n$)')
        ax1.set_ylabel('Número de Operações (Escala)')
        ax1.set_title(r'Comparação de Complexidade de Algoritmos', fontsize=16)
        ax1.grid(True)
        ax1.legend()       
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        
        # Salva o gráfico em um arquivo PNG
        plot_file_name = 'complexity_plot_from_csv.png'
        plt.savefig(plot_file_name)
        print(f"\nGráfico salvo com sucesso em '{plot_file_name}'")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
        print("Certifique-se de que o arquivo CSV esteja no mesmo diretório do script.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# -------------------------------------------------------------------------------

# Define o nome do arquivo CSV e os cabeçalhos
file_name = "complexidades.csv"
headers = ['n', 'O(log n)', 'O(n)', 'O(n log n)', 'O(n^2)', 'O(n^3)', 'O(2^n)', 'O(n!)']

# Define o intervalo de valores de n
n_values = range(1, 11) 

# Abre o arquivo CSV no modo de escrita ('w')
with open(file_name, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    
    # Escreve o cabeçalho no arquivo
    writer.writeheader()
    
    # Itera sobre cada valor de n no intervalo
    for n in n_values:
        # Calcula as complexidades para o n atual
        complexities = calculate_complexities(n)
        print(f"\n{complexities}")
        
        # Cria um dicionário para a linha do CSV, incluindo o valor de n
        row_data = {'n': n, **complexities}
        
        # Escreve a linha no arquivo
        writer.writerow(row_data)

print(f"Dados de complexidade salvos com sucesso em '{file_name}'")

plot_complexities_from_csv()
