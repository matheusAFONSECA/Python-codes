# código que apaga um sequencia de String em um aquivo .txt

# Abrir arquivo e ler conteúdo
with open("D:\\Downloads\\resultadosEasyOCR .txt", 'r') as f:
    conteudo = f.read()

# Remover sequência de string desejada
sequencia = "-\n"
novo_conteudo = conteudo.replace(sequencia, '')

# Escrever novo conteúdo no mesmo arquivo
with open("D:\\Downloads\\resultadosEasyOCR .txt", 'w') as f:
    f.write(novo_conteudo)
