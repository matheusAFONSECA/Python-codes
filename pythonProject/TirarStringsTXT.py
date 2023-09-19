# código que apaga um sequencia de String em um aquivo .txt com base em regex
import os
import re

# Pasta contendo os arquivos .txt
pasta = "C:\\Users\\mathe\\Downloads\\TXT"

# Padrão de expressão regular para encontrar linhas começando com "1"
padrao = r'^1.*'

# Listar arquivos na pasta
for nome_arquivo in os.listdir(pasta):
    # Verificar se o arquivo é um arquivo .txt
    if nome_arquivo.endswith(".txt"):
        # Caminho completo para o arquivo
        caminho_arquivo = os.path.join(pasta, nome_arquivo)

        # Abrir o arquivo e ler o conteúdo
        with open(caminho_arquivo, 'r') as f:
            linhas = f.readlines()

        # Filtrar as linhas que não correspondem ao padrão
        linhas_filtradas = [linha for linha in linhas if not re.match(padrao, linha)]

        # Escrever as linhas filtradas de volta no mesmo arquivo
        with open(caminho_arquivo, 'w') as f:
            f.writelines(linhas_filtradas)

# Mensagem de conclusão
print("Operação concluída.")
