from queue import Queue

notificacoes = Queue()

def salvar_notificacao_fila(notificacao):
    notificacoes.put(notificacao)

def processar_notificacao_fila():
    while True:
        if not notificacoes.empty():
            notificacao = notificacoes.get()
            usuario = notificacao.get('usuario')
            if usuario["tipo"] == "vendedor":
                print(f"Enviando notificação ao vendedor: {usuario['email']}")
                notificacoes.task_done()
            print(f"Enviando notificação ao comprador: {usuario['email']}")
            notificacoes.task_done()
