# Análise — Responsabilidades e Arquitetura

## Resumo
O sistema foi refatorado para que cada classe tenha uma única responsabilidade: o processador coordena o fluxo, as classes de pagamento tratam do pagamento e as de notificação enviam mensagens. A arquitetura favorece extensibilidade, substituibilidade e testabilidade.

## Organização por responsabilidade única (SRP)
- ProcessadorDePedidos: coordena o fluxo (recebe pedido, solicita pagamento, aciona notificação).
- Classes de pagamento (ex.: PagamentoPix): lógica exclusiva de pagamento.
- Classes de notificação (ex.: NotificacaoSMS): envio de mensagens.

## Extensibilidade (OCP)
- Novas formas de pagamento ou notificação são adicionadas criando-se novas classes que implementem as abstrações existentes, sem alterar código já existente.

## Substituibilidade (LSP)
- Subclasses podem substituir suas classes base sem quebrar o comportamento esperado do sistema (ex.: PagamentoPix substitui um contrato de pagamento).

## Segregação de interfaces (ISP)
- Interfaces separadas: MetodoDePagamento e Notificador.
- Evita que classes sejam forçadas a implementar métodos que não usam.

## Injeção de dependência e testabilidade (DIP)
- ProcessadorDePedidos depende de abstrações e recebe implementações externamente.
- Facilita testes unitários com mocks/stubs e aumenta a flexibilidade do sistema.

## Como estender
- Novo método de pagamento: implementar MetodoDePagamento e registrar no ponto de composição.
- Novo canal de notificação: implementar Notificador e injetar onde necessário.

## Conclusão
A refatoração aplica princípios SOLID (SRP, OCP, LSP, ISP, DIP), resultando em componentes mais coesos, desacoplados e fáceis de manter, estender e testar.