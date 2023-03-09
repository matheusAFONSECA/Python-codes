# movendo os aruqivos de uma pasta para outra usando um arquivo .txt com o nome dos arquivos
import os
import shutil

# Abrindo o arquivo com os nomes dos arquivos
with open('nomes.txt', 'r') as f:
    nomes_arquivos = f.read().splitlines()

# Percorrendo a lista de nomes de arquivos e movendo-os para a pasta de destino
for nome_arquivo in nomes_arquivos:
    origem = os.path.join('origem', nome_arquivo)
    destino = os.path.join('destino', nome_arquivo)
    shutil.move(origem, destino)
