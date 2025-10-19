from abc import ABC, abstractmethod


# SRP e DIP: Abstrações


class MetodoDePagamento(ABC):
    @abstractmethod
    def pagar(self, pedido):
        pass


class Notificador(ABC):
    @abstractmethod
    def notificar(self, pedido):
        pass



#  OCP: Implementações que estendem sem modificar


class PagamentoCartaoCredito(MetodoDePagamento):
    def pagar(self, pedido):
        print(f"Pagando R$ {pedido['valor']:.2f} com cartão de crédito...")


class PagamentoBoleto(MetodoDePagamento):
    def pagar(self, pedido):
        print(f"Gerando boleto no valor de R$ {pedido['valor']:.2f}...")


class PagamentoPix(MetodoDePagamento):
    def pagar(self, pedido):
        print(f"Realizando pagamento via PIX de R$ {pedido['valor']:.2f}...")


class NotificacaoEmail(Notificador):
    def notificar(self, pedido):
        print(f"Enviando e-mail para {pedido['cliente_email']} confirmando o pedido #{pedido['id']}...")


class NotificacaoSMS(Notificador):
    def notificar(self, pedido):
        print(f"Enviando SMS para o cliente confirmando o pedido #{pedido['id']}...")



# SRP e DIP: Processador desacoplado


class ProcessadorDePedidos:
    def __init__(self, metodo_pagamento: MetodoDePagamento, notificador: Notificador):
        self.metodo_pagamento = metodo_pagamento
        self.notificador = notificador

    def processar(self, pedido):
        print(f"Processando o pedido #{pedido['id']} no valor de R$ {pedido['valor']:.2f}...")

        # Pagamento via abstração (DIP)
        self.metodo_pagamento.pagar(pedido)

        # Notificação via abstração (DIP)
        self.notificador.notificar(pedido)

        pedido['status'] = 'concluido'
        print("Pedido concluído!")



# Uso (Cliente)


if __name__ == "__main__":
    pedido1 = {
        'id': 123,
        'valor': 150.75,
        'cliente_email': 'cliente@exemplo.com',
        'status': 'pendente'
    }

    pedido2 = {
        'id': 456,
        'valor': 250.00,
        'cliente_email': 'cliente2@exemplo.com',
        'status': 'pendente'
    }

    # Pedido pago com cartão + notificação por e-mail
    processador1 = ProcessadorDePedidos(PagamentoCartaoCredito(), NotificacaoEmail())
    processador1.processar(pedido1)

    print("-" * 30)

    # Pedido pago com Pix + notificação por SMS
    processador2 = ProcessadorDePedidos(PagamentoPix(), NotificacaoSMS())
    processador2.processar(pedido2)
