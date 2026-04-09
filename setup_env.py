import shutil
import os

def setup_env():
    source = '.env.exemplo'
    target = '.env'

    if not os.path.exists(source):
        print(f"Erro: O arquivo {source} não foi encontrado.")
        return

    if os.path.exists(target):
        confirm = input(f"O arquivo {target} já existe. Deseja sobrescrever? (s/N): ").strip().lower()
        if confirm != 's':
            print("Operação cancelada.")
            return

    shutil.copy(source, target)
    print(f"Sucesso: {source} copiado para {target}!")
    print("Agora, abra o arquivo .env e coloque sua GEMINI_KAY.")

if __name__ == "__main__":
    setup_env()
