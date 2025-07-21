# 📝 Changelog - Venâncio Delivery

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

## [2.0.0] - 2025-01-21

### ✨ Adicionado
- **Sistema de Histórico Completo**
  - Visualização de todos os pedidos realizados
  - Janela dedicada com scroll para navegação
  - Informações detalhadas: data, itens, endereço, pagamento, total
  - Numeração automática de pedidos (#001, #002, etc.)

- **Sistema de Desconto Inteligente**
  - Desconto de 10% automático para pedidos acima de R$ 50,00
  - Exibição clara do desconto aplicado no resumo
  - Cálculo transparente: subtotal, desconto, total final

- **Interface Moderna v2.0**
  - Design atualizado com emojis e ícones
  - Cores diferenciadas para botões (verde, azul, laranja)
  - Layout mais organizado e intuitivo
  - Rodapé com branding da empresa

- **Funcionalidades Técnicas**
  - Timestamps automáticos para cada pedido
  - Persistência de dados durante toda a sessão
  - Limpeza automática de campos após finalização
  - Sistema robusto de validação

### 🔄 Modificado
- **Função `calcular_pedido()`**
  - Aplicação automática de desconto quando aplicável
  - Exibição mais detalhada do resumo
  - Melhor formatação das informações

- **Função `finalizar_pedido()`**
  - Salvamento completo no histórico
  - Cálculo correto com desconto
  - Mensagem de confirmação mais informativa
  - Limpeza automática da interface

- **Interface Gráfica**
  - Título atualizado: "Venâncio Delivery 🍔"
  - Seções bem definidas com labels claros
  - Botões com cores e ícones específicos
  - Melhor espaçamento e organização

### 🛠️ Melhorias Técnicas
- Estrutura de dados otimizada para histórico
- Tratamento de erros mais robusto
- Código mais limpo e bem documentado
- Separação clara de responsabilidades

---

## [1.0.0] - Versão Inicial

### ✨ Funcionalidades Base
- Cardápio com preços fixos
- Seleção de itens via checkbox
- Cálculo básico de total e tempo de entrega
- Formulário de endereço e pagamento
- Interface simples com Tkinter

### 🎯 Objetivo Original
Sistema básico de pedidos para restaurante, conforme especificação acadêmica da disciplina de Tópicos Integradores.
