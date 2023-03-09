# código que apaga um sequencia de String em um aquivo .txt
with open('arquivo.txt', 'r') as f:
    linhas = f.readlines()

linhas_sem_repeticao = []
for linha in linhas:
    if linha not in linhas_sem_repeticao:
        linhas_sem_repeticao.append(linha)

with open('arquivo_sem_repeticao.txt', 'w') as f:
    f.writelines(linhas_sem_repeticao)
