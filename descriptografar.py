import os
from cryptography.fernet import Fernet

# Le a chave que ficou salva
with open("chave.key", "rb") as f:
    chave = f.read()

fernet = Fernet(chave)

# Vai passar por cada arquivo e tentar reverter
for arquivo in os.listdir():
    if arquivo.endswith(".txt") and arquivo != "LEIA_ISSO.txt":
        with open(arquivo, "rb") as f:
            dados_cripto = f.read()
        
        # Aqui ele faz a magica de voltar ao normal
        dados_originais = fernet.decrypt(dados_cripto)
        
        with open(arquivo, "wb") as f:
            f.write(dados_originais)

print("Arquivos restaurados.")
