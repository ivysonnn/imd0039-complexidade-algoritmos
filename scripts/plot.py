import sys
import pandas as pd
import matplotlib.pyplot as plt

def plot_analysis_from_csv(algorithm_name: str):
    """
    Plota os dados de análise de tempo de execução de um algoritmo a partir de um arquivo CSV.

    Args:
        algorithm_name (str): A sigla do algoritmo (ex: 'qs', 'bs', 'bb', 'ss').
    """
    file_path = f"../results/{algorithm_name}_result.csv"
    plot_file_name = f"../results/{algorithm_name}_plot.png"

    try:
        # Carrega os dados do arquivo CSV
        df = pd.read_csv(file_path)

        print(f"Dados do arquivo '{file_path}' carregados com sucesso.")
        
        # Renomeia as colunas para facilitar o acesso
        df.columns = ['n', 'time_measured', 'time_log_n', 'time_n', 'time_n_log_n', 'time_n_2', 'time_n_3']

        # --- Normalização das Curvas Teóricas ---
        # Para comparar visualmente, ajustamos a escala das curvas teóricas
        # para que o primeiro ponto delas coincida com o primeiro ponto do tempo medido.
        # Isso é feito calculando uma constante 'c' tal que: c * f(n_inicial) = T(n_inicial)
        if not df.empty:
            # Evita divisão por zero se o tempo medido for muito pequeno
            if df['time_log_n'].iloc[0] > 0:
                df['time_log_n'] *= (df['time_measured'].iloc[0] / df['time_log_n'].iloc[0])
            if df['time_n'].iloc[0] > 0:
                df['time_n'] *= (df['time_measured'].iloc[0] / df['time_n'].iloc[0])
            if df['time_n_log_n'].iloc[0] > 0:
                df['time_n_log_n'] *= (df['time_measured'].iloc[0] / df['time_n_log_n'].iloc[0])
            if df['time_n_2'].iloc[0] > 0:
                df['time_n_2'] *= (df['time_measured'].iloc[0] / df['time_n_2'].iloc[0])
            if df['time_n_3'].iloc[0] > 0:
                df['time_n_3'] *= (df['time_measured'].iloc[0] / df['time_n_3'].iloc[0])

        # Criar uma figura e um subplot
        fig, ax1 = plt.subplots(figsize=(12, 8))

        # Plot dos dados medidos e das curvas teóricas
        ax1.plot(df['n'], df['time_measured'], marker='o', linestyle='-', label=f'Tempo Medido ({algorithm_name.upper()})', zorder=10)
        ax1.plot(df['n'], df['time_log_n'], linestyle='--', label='Referência O(log n)')
        ax1.plot(df['n'], df['time_n'], linestyle='--', label='Referência O(n)')
        ax1.plot(df['n'], df['time_n_log_n'], linestyle='--', label='Referência O(n log n)')
        ax1.plot(df['n'], df['time_n_2'], linestyle='--', label='Referência O(n^2)')
        ax1.plot(df['n'], df['time_n_3'], linestyle='--', label='Referência O(n^3)')

        # >>> MELHORIA: Usar escala logarítmica para ambos os eixos <<<
        ax1.set_xscale('log')
        ax1.set_yscale('log')

        ax1.set_xlabel('Tamanho da Entrada (n)')
        ax1.set_ylabel('Tempo Médio de Execução (segundos)')
        ax1.set_title(f'Análise de Desempenho do Algoritmo: {algorithm_name.upper()}', fontsize=16)
        ax1.grid(True)
        ax1.legend()

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])

        # Salva o gráfico em um arquivo PNG
        plt.savefig(plot_file_name)
        print(f"\nGráfico salvo com sucesso em '{plot_file_name}'")
        plt.show()

    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
        print(f"Execute a análise para '{algorithm_name}' primeiro (ex: ./algorithms-complexity -{algorithm_name}).")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 plot.py <sigla_do_algoritmo>")
        print("Exemplo: python3 plot.py bb")
        sys.exit(1)

    algorithm_to_plot = sys.argv[1]
    plot_analysis_from_csv(algorithm_to_plot)
