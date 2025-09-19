import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_analysis_from_csv(algorithm_name: str):
    file_path = f"../results/{algorithm_name}_result.csv"
    plot_file_name = f"../results/{algorithm_name}_plot_loglog.png" # Nome de arquivo diferente

    try:
        df = pd.read_csv(file_path, usecols=[0, 1], header=None, names=['n', 'time_measured'])
        print(f"Dados do arquivo '{file_path}' carregados com sucesso.")

        df['n'] = pd.to_numeric(df['n'], errors='coerce')
        df['time_measured'] = pd.to_numeric(df['time_measured'], errors='coerce')
        df.dropna(inplace=True)

        if df.empty:
            print("O arquivo não contém dados válidos para plotar.")
            return

        # --- Geração de Curvas Teóricas Ideais ---
        df['ref_log_n'] = np.log(df['n'] + 1e-9)
        df['ref_n'] = df['n'].astype(float)
        df['ref_n_log_n'] = df['n'] * np.log(df['n'] + 1e-9)
        df['ref_n_2'] = df['n']**2
        df['ref_n_3'] = df['n']**3

        if not df.empty:
            columns_to_normalize = [
                'time_measured', 'ref_log_n', 'ref_n',
                'ref_n_log_n', 'ref_n_2', 'ref_n_3'
            ]
            for col in columns_to_normalize:
                # Encontra o primeiro valor não nulo para normalizar
                first_valid_value = df[df[col] > 0][col].iloc[0] if not df[df[col] > 0].empty else 0
                if first_valid_value > 0:
                    df[col] = df[col] / first_valid_value
                else:
                    print(f"Aviso: Não foi possível normalizar a coluna '{col}'.")

        # Criar uma figura e um subplot
        fig, ax1 = plt.subplots(figsize=(12, 8))

        # Plot dos dados medidos e das curvas teóricas
        ax1.plot(df['n'], df['time_measured'], marker='o', linestyle='-', label=f'Tempo Medido ({algorithm_name.upper()})', zorder=10)
        ax1.plot(df['n'], df['ref_log_n'], linestyle='--', label=r'Referência $O(\log n)$')
        ax1.plot(df['n'], df['ref_n'], linestyle='--', label=r'Referência $O(n)$')
        ax1.plot(df['n'], df['ref_n_log_n'], linestyle='--', label=r'Referência $O(n \log n)$')
        ax1.plot(df['n'], df['ref_n_2'], linestyle='--', label=r'Referência $O(n^2)$')
        ax1.plot(df['n'], df['ref_n_3'], linestyle='--', label=r'Referência $O(n^3)$')

        # >>> MELHORIA: Usar escala logarítmica para ambos os eixos <<<
        ax1.set_xscale('log')
        ax1.set_yscale('log')

        ax1.set_xlabel('Tamanho da Entrada (n)')
        ax1.set_ylabel('Tempo de Execução Normalizado')
        ax1.set_title(f'Análise de Desempenho (Escala Log-Log): {algorithm_name.upper()}', fontsize=16)
        ax1.grid(True, which="both", ls="-", linewidth=1)
        ax1.legend()

        plt.tight_layout()

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
        sys.exit(1)
    algorithm_to_plot = sys.argv[1]
    plot_analysis_from_csv(algorithm_to_plot)