from uuid import uuid4
from .fila.pedido import salvar_pedido_fila
def efetuarPedido(event, context):
    dados_pedido = event.get('dados_pedido', {})

    if not dados_pedido:
        return {
            'statusCode': 400,
            'body': 'Dados do pedido inválidos.'
        }
    
    pedido_id = str(uuid4()) 
    dados_pedido['pedido_id'] = pedido_id
    salvar_pedido_fila(dados_pedido)
    return {
        'statusCode': 200,
        'body': {
            'mensagem': 'Pedido efetuado com sucesso.',
            'pedido_id': pedido_id
        }
    }