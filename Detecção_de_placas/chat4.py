# código que lê uma lista em um arquivo .txt que contem o nome de vários arquivos que serão
# movidos de um diretório para outro

import os

# Define o caminho do diretório de origem e destino dos arquivos
diretorio_origem = "C:\\Users\\mathe\\Downloads\\IDENTIFICACAO DE PLACAS\\DATASETS\\antigos4\\plate detection02.v1i.yolov5pytorch\\test\\labels"
diretorio_destino = "C:\\Users\\mathe\\Downloads\\LABELS"

# Abre o arquivo de texto com a lista de nomes de arquivos
with open("C:\\Users\\mathe\\Downloads\\nomes_dos_arquivos - Copia.txt", 'r') as arquivo:
    # Lê cada linha do arquivo e remove possíveis quebras de linha
    nomes_arquivos = [linha.strip() for linha in arquivo.readlines()]

# Move cada arquivo da lista para o diretório de destino
for nome_arquivo in nomes_arquivos:
    caminho_origem = os.path.join(diretorio_origem, nome_arquivo)
    caminho_destino = os.path.join(diretorio_destino, nome_arquivo)
    os.rename(caminho_origem, caminho_destino)
