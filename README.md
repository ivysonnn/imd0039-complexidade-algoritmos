
# imd0039-complexidade-algoritmos
Projeto desenvolvido para a disciplina IMD0039 - Estrutura de Dados II, com o objetivo de implementar um programa capaz de avaliar empiricamente o tempo de execução de diferentes algoritmos.

## 📖 Sobre o Projeto

Este projeto consiste em um programa desenvolvido inteiramente em **C++** para analisar e comparar o desempenho de algoritmos. Ele executa os algoritmos com uma variedade de tamanhos de entrada, mede o tempo de execução para cada caso e, ao final, gera gráficos de visualização.

Para a plotagem dos gráficos, o projeto utiliza a biblioteca **[matplotlib-cpp](https://github.com/lava/matplotlib-cpp)**, um wrapper que permite ao C++ invocar a popular biblioteca `Matplotlib` do Python. Dessa forma, toda a lógica, medição e visualização são controladas a partir do código C++.


## ⚙️ Pré-requisitos

Para a execução do projeto, você deverá ter os seguintes componentes instalados no seu sistema:
 - **C++ versão 11 ou superior(compilador gcc/g++)** 
 - **CMake 3.16 ou superior**
 - **Python 3.11 ou superior**
 - Bibliotecas Python:
   - **Numpy**
   - **Matplotlib**

## 🚀 Como compilar

 - **Clone o repositório**
    
   ``` Bash 
       git clone https://github.com/seu-usuario/imd0039-complexidade-algoritmos.git 
       
       cd imd0039-complexidade-algoritmos
- **Compile o projeto com CMake**
     ```Bash
       # Crie o repositório para build do projeto
       mkdir build
       
       cd build
       
       # Configure o projeto
       cmake ..
       
       # Compile o projeto
       cmake --build .


## </> Modo de uso

|Argumentos|Descrição|
|--|--|
|`-h` |Mostra uma mensagem de ajuda com todos os comandos disponíveis.
|`-qs`|Executa a análise de desempenho do algoritmo de ordenação **QuickSort**
|`-bs`|Executa a análise de desempenho do algoritmo de ordenação **BubbleSort**
|`-bb`|Executa a análise de desempenho do algoritmo de **Busca Binária**
|`-ss`|Executa a análise de desempenho do algoritmo de **Busca Sequencial**
|`-pl <alvo>`| **Plota o gráfico** com dados de uma análise anterior. O `<alvo>` deve ser uma das siglas dos algoritmos de análise (ex: `qs`, `bs`, `bb`, `ss`).

Exemplos: 
```Bash
# 1. Análise do algoritmo QuickSort
# Gera um arquivo com os dados de tamanho de entrada e tempo para a execução do algoritmo
./algorithms-complexity -qs

# 2. Plotagem de gráfico com os resultados da Busca Sequencial
# O comando abaixo espera que a análise com -ss já tenha sido realizada
./algorithms-complexity -pl ss
```

## 👨‍💻 Alunos
Chistian Daniel - **[@ChistianDPSilva](https://github.com/ChistianDPSilva)**

Ivyson Lucas - **[@ivysonnn](https://github.com/ivysonnn)**

## Licença

MIT License - **[LICENSE](https://github.com/ivysonnn/imd0039-complexidade-algoritmos/blob/main/LICENSE)**
