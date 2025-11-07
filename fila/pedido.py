from queue import Queue


pedidos = Queue()

def salvar_pedido_fila(pedido):
    pedidos.put(pedido)

def processar_pedido_fila():
    while True:
        if not pedidos.empty():
            pedido = pedidos.get()
            print(f"Processando pedido: {pedido}")
            pedidos.task_done()