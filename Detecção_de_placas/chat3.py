# código que apaga um sequencia de String em um aquivo .txt

# Abrir arquivo e ler conteúdo
with open("C:\\Users\\mathe\\Downloads\\nomes_dos_arquivos - Copia.txt", 'r') as f:
    conteudo = f.read()

# Remover sequência de string desejada
sequencia = ".jpg"
novo_conteudo = conteudo.replace(sequencia, '.txt')

# Escrever novo conteúdo no mesmo arquivo
with open("C:\\Users\\mathe\\Downloads\\nomes_dos_arquivos - Copia.txt", 'w') as f:
    f.write(novo_conteudo)
