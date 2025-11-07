from queue import Queue
from .notificacao import salvar_notificacao_fila, processar_notificacao_fila
from .database import save_database
pedidos = Queue()

def salvar_pedido_fila(pedido):
    pedidos.put(pedido)

def processar_pedido_fila():
    while True:
        if not pedidos.empty():
            pedido = pedidos.get()
            print(f"Processando pedido: {pedido}")
            pedidos.task_done()
            save_database(pedido)
            usuario = pedido.get('usuario')
            salvar_notificacao_fila(usuario)