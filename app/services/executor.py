from app.drivers.arduino import enviar_comando

def executar_acoes(acoes):

    print("\n===== EXECUTANDO AÇÕES =====\n")

    for acao in acoes:

        dispositivo = acao["dispositivo"]
        comando = acao["acao"]
        valor = acao["valor"]

        mensagem = f"{dispositivo}:{comando}:{valor}"

        enviar_comando(mensagem)