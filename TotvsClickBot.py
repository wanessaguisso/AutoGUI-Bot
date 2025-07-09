# Importação das bibliotecas necessárias
import pyautogui                      # Para automação de teclado e mouse
import time                           # Para controle de tempo (pausas)
import logging                        # Para registro de logs
from tkinter import messagebox, Tk    # Para exibição de mensagens de erro em pop-up

# Oculta a janela principal do Tkinter (usado apenas para exibir a mensagem de erro)
Tk().withdraw()

# Configuração básica do sistema de log para mostrar data, nível e mensagem
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Função genérica que localiza uma imagem na tela e realiza cliques
def localizar_e_clicar(imagem, descricao, cliques=2, tempo_espera=5, confidence=0.85):
    try:
        logging.info(f"🔍 Procurando {descricao} na tela...")  # Log de início da busca
        posicao = pyautogui.locateCenterOnScreen(imagem, confidence=confidence)  # Busca pela imagem na tela

        if posicao is None:
            raise FileNotFoundError(f"{descricao} não encontrado na tela.")  # Se não encontrou, lança erro

        logging.info(f"✅ {descricao} encontrado em {posicao}, clicando...")  # Log de sucesso

        for _ in range(cliques):  # Realiza os cliques conforme o número informado
            pyautogui.click(posicao)
            time.sleep(0.2)  # Pequeno intervalo entre os cliques

        time.sleep(tempo_espera)  # Aguarda um tempo após o clique
        logging.info(f"🟢 Ação concluída: {descricao}")  # Log de conclusão
    except Exception as e:
        logging.error(f"Erro ao processar {descricao}: {e}")  # Log do erro
        messagebox.showerror("Erro", f"Erro ao processar {descricao}: {e}")  # Mostra erro em pop-up
        raise  # Interrompe a execução (remova se quiser que o programa continue)

# 🔽 Trecho principal do código com chamadas à função criada
try:
    # Localiza e clica duas vezes no ícone do TOTVS RM
    localizar_e_clicar(
        imagem=r"totvsRM_icon.png", #ajuste o caminho da imagem conforme necessário        
        descricao="ícone do TOTVS RM"
    )
    time.sleep(20)  # Aguarda 20 segundos para o sistema abrir

    # Localiza o campo de senha do sistema e clica
    localizar_e_clicar(
        imagem=r"camposenha_icon.png",        
        descricao="Campo de senha do TOTVS RM"
    )
    # Digita a senha no campo com intervalo entre as teclas
    pyautogui.typewrite("SUA SENHA DO TOTVS", interval=0.1)

    # Clica no botão "Entrar" para logar no sistema
    localizar_e_clicar(
        imagem=r"botaoEntrar_icon.png",
        descricao="Botão Entrar do TOTVS RM"
    )
    time.sleep(60)  # Aguarda 1 minuto para o sistema carregar completamente

    # Abre os módulos disponíveis no TOTVS (1 clique apenas)
    localizar_e_clicar(
        imagem=r"botaoModulo_icon.png",
        descricao="Botão de módulos do TOTVS RM",
        cliques=1
    )
    time.sleep(3)  # Espera o menu de módulos carregar

    # Clica no módulo "Educacional Módulo"
    localizar_e_clicar(
        imagem=r"botaoEducacionalModulo_icon.png",
        descricao="Botão do Educacional Módulo do TOTVS RM",
        cliques=1
    )

    # Clica no submenu "Módulo Educacional"
    localizar_e_clicar(
        imagem=r"botaoModuloEducacional_icon.png",
        descricao="Botão do Módulo Educacional do TOTVS RM",
        cliques=1
    )

    time.sleep(10)  # Tempo extra para garantir que o módulo carregue por completo

except Exception:
    # Caso qualquer etapa acima falhe, esse bloco será acionado
    logging.error("Execução encerrada devido a erro.")
