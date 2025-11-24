# Benchmark: Subset Sum (Python vs Java)

Este projeto compara a performance de execução do algoritmo **Subset Sum** (Soma de Subconjuntos) utilizando uma abordagem de _Backtracking_ (Árvore de Decisão + Poda). O comparativo é realizado entre **Python** e **Java**, salvando os tempos de execução em uma única planilha Excel para análise posterior.

## 📂 Estrutura do Projeto

```text
/
├── Input/              # Arquivos de texto com os casos de teste (.txt)
├── Java/               # Código fonte Java (SubsetSum.java) e configurações
├── Python/             # Código fonte Python (subsetsum.py)
├── Results/            # Planilha de saída (results.xlsx)
├── .gitignore          # Arquivos ignorados pelo Git
├── LICENSE             # Licença MIT
├── pom.xml             # Configuração Maven (Dependências Java)
└── README.md           # Este arquivo

🚀 Pré-requisitos🐍 PythonPython 3.8+ instalado.Bibliotecas necessárias para manipulação de Excel:

pip install pandas openpyxl

☕ JavaJDK 8 ou superior instalado.VS Code com o Extension Pack for Java (recomendado).O arquivo pom.xml na raiz garante o download automático da biblioteca Apache POI (necessária para escrever no Excel).

1️⃣ Criando ou Editando Entradas (Inputs)Os arquivos de entrada devem estar na pasta Input/ (ex: small_input.txt).Cada caso de teste dentro do arquivo segue estritamente este formato de 3 linhas:

ALVO (Inteiro)
NUMEROS (Separados por espaço)
--- (Separador)

Exemplo de conteúdo:
10
2 3 5 6 8 10
---
50
10 20 30 40 50
---

2️⃣ Executando a Versão em PythonA partir da raiz do projeto, execute o comando:Bashpython Python/subsetsum.py
O script processará os arquivos definidos (small, med, big) na pasta Input.Criará (ou atualizará) o arquivo Results/results.xlsx.Os tempos são calculados e salvos em milissegundos (ms).

3️⃣ Executando a Versão em JavaO projeto está configurado como um projeto Maven. Certifique-se de que o VS Code tenha baixado as dependências do pom.xml antes de rodar.Via VS Code (Recomendado)Abra a pasta raiz do projeto no VS Code.Abra o arquivo Java/SubsetSum.java.Pressione F5 (ou clique em "Run").Via Terminal (Maven)Se preferir rodar via linha de comando:

mvn clean install
mvn exec:java -Dexec.mainClass="Java.SubsetSum"

O código Java lerá os mesmos inputs.
Adicionará novas linhas na planilha results.xlsx identificando a linguagem como Java.

📊 Analisando os Resultados
Os resultados são consolidados em Results/results.xlsx.
As colunas são:
language - Linguagem utilizada (Python ou Java)
input_size - Quantidade de elementos no conjunto
target - O valor alvo da soma
execution_time - Tempo de execução em milissegundos

⚠️ Importante: Mantenha o arquivo Excel fechado enquanto executa os programas. Se o arquivo estiver aberto no Excel, os scripts falharão ao tentar salvar os dados (Erro de Permissão de Arquivo).

📝 Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
```
