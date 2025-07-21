"""
🍔 Venâncio Delivery - Sistema de Pedidos v2.0
==============================================

Sistema completo de delivery com interface gráfica desenvolvido em Python/Tkinter.
Inclui funcionalidades avançadas como histórico de pedidos, sistema de desconto
automático e interface moderna.

Autor: Venâncio Wallysson
Curso: Análise e Desenvolvimento de Sistemas
Data: Janeiro 2025
Versão: 2.0.0
"""

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# 📋 CONFIGURAÇÕES E DADOS
# ========================

# Cardápio com preços (em Reais)
cardapio = {
    'X- Vieri': 30.00,
    'X- Emerson': 35.00,
    'MEGA-MARCÃO': 50.00,
    'FRAPOTINO': 10.00,
    'Refrigerante': 5.00,
    'Batata': 8.00
}

# Lista para armazenar histórico de pedidos (persistente durante a sessão)
historico_pedidos = []

# 🔧 FUNÇÕES PRINCIPAIS
# ====================

def calcular_pedido():
    """
    Calcula o total do pedido, aplica desconto se aplicável e exibe resumo.
    
    Funcionalidades:
    - Coleta itens selecionados
    - Calcula total e tempo estimado
    - Aplica desconto de 10% para pedidos > R$ 50
    - Exibe resumo detalhado
    """
    total = 0 
    tempo_entrega = 0
    itens_selecionados = []
    
    # Calcula total e coleta itens selecionados
    for item, var in itens_vars.items():
        if var.get() == 1:
            total += cardapio[item]
            tempo_entrega += 10
            itens_selecionados.append(f"{item} - R$ {cardapio[item]:.2f}")
    
    if total == 0:
        messagebox.showwarning("Aviso", "Selecione ao menos um item.")
        return
    
    # Aplica desconto para pedidos acima de R$ 50
    desconto = 0
    if total > 50:
        desconto = total * 0.10
        total_com_desconto = total - desconto
        mensagem = f"Itens selecionados:\n" + "\n".join(itens_selecionados)
        mensagem += f"\n\nSubtotal: R$ {total:.2f}"
        mensagem += f"\nDesconto (10%): R$ {desconto:.2f}"
        mensagem += f"\nTotal: R$ {total_com_desconto:.2f}"
        mensagem += f"\nTempo estimado: {tempo_entrega} minutos"
    else:
        mensagem = f"Itens selecionados:\n" + "\n".join(itens_selecionados)
        mensagem += f"\n\nTotal: R$ {total:.2f}"
        mensagem += f"\nTempo estimado: {tempo_entrega} minutos"
    
    messagebox.showinfo("Resumo do Pedido", mensagem)


def finalizar_pedido():
    """
    Finaliza o pedido e salva no histórico com todas as informações.
    
    Funcionalidades:
    - Valida preenchimento dos campos obrigatórios
    - Calcula total com desconto (se aplicável)
    - Salva pedido no histórico com timestamp
    - Exibe confirmação detalhada
    - Limpa formulário para próximo pedido
    """
    endereco = entrada_endereco.get()
    pagamento = pagamento_var.get()
    
    if not endereco or pagamento == "Selecione":
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
        return
    
    # Coleta itens selecionados e calcula total
    itens_pedido = []
    total = 0
    for item, var in itens_vars.items():
        if var.get() == 1:
            itens_pedido.append(item)
            total += cardapio[item]
    
    if not itens_pedido:
        messagebox.showwarning("Aviso", "Selecione ao menos um item antes de finalizar.")
        return
    
    # Aplica desconto se necessário
    desconto = 0
    if total > 50:
        desconto = total * 0.10
        total_final = total - desconto
    else:
        total_final = total
    
    # Salva no histórico
    pedido = {
        'data': datetime.now().strftime("%d/%m/%Y %H:%M"),
        'itens': itens_pedido.copy(),
        'endereco': endereco,
        'pagamento': pagamento,
        'total': total_final,
        'desconto': desconto
    }
    historico_pedidos.append(pedido)
    
    # Mensagem de confirmação
    mensagem = f"Pedido #{len(historico_pedidos):03d} finalizado com sucesso!"
    mensagem += f"\nEndereço: {endereco}"
    mensagem += f"\nForma de pagamento: {pagamento}"
    mensagem += f"\nTotal: R$ {total_final:.2f}"
    if desconto > 0:
        mensagem += f"\nDesconto aplicado: R$ {desconto:.2f}"
    
    messagebox.showinfo("Pedido Concluído", mensagem)
    
    # Limpa os campos
    for var in itens_vars.values():
        var.set(0)
    entrada_endereco.delete(0, tk.END)
    pagamento_var.set("Selecione")


def visualizar_historico():
    """
    Abre janela dedicada para visualização do histórico completo de pedidos.
    
    Funcionalidades:
    - Cria janela secundária com scroll
    - Lista todos os pedidos com detalhes completos
    - Numeração automática dos pedidos
    - Interface somente leitura para consulta
    """
    if not historico_pedidos:
        messagebox.showinfo("Histórico", "Nenhum pedido realizado ainda.")
        return
    
    # Cria janela do histórico
    janela_historico = tk.Toplevel(root)
    janela_historico.title("Histórico de Pedidos")
    janela_historico.geometry("600x400")
    
    # Frame com scrollbar
    frame_scroll = tk.Frame(janela_historico)
    frame_scroll.pack(fill="both", expand=True, padx=10, pady=10)
    
    # Scrollbar
    scrollbar = tk.Scrollbar(frame_scroll)
    scrollbar.pack(side="right", fill="y")
    
    # Text widget para exibir histórico
    texto_historico = tk.Text(frame_scroll, yscrollcommand=scrollbar.set, wrap="word")
    texto_historico.pack(side="left", fill="both", expand=True)
    
    scrollbar.config(command=texto_historico.yview)
    
    # Adiciona pedidos ao texto
    for i, pedido in enumerate(historico_pedidos, 1):
        texto_historico.insert(tk.END, f"📦 PEDIDO #{i:03d}\n")
        texto_historico.insert(tk.END, f"Data: {pedido['data']}\n")
        texto_historico.insert(tk.END, f"Itens: {', '.join(pedido['itens'])}\n")
        texto_historico.insert(tk.END, f"Endereço: {pedido['endereco']}\n")
        texto_historico.insert(tk.END, f"Pagamento: {pedido['pagamento']}\n")
        texto_historico.insert(tk.END, f"Total: R$ {pedido['total']:.2f}\n")
        if pedido['desconto'] > 0:
            texto_historico.insert(tk.END, f"Desconto: R$ {pedido['desconto']:.2f}\n")
        texto_historico.insert(tk.END, "-" * 50 + "\n\n")
    
    texto_historico.config(state="disabled")  # Torna somente leitura


# 🎨 INTERFACE GRÁFICA PRINCIPAL
# ===============================

# Configuração da janela principal
root = tk.Tk()
root.title("Venâncio Delivery 🍔")
root.geometry("500x600")
root.resizable(False, False)

# Tenta carregar o ícone personalizado, continua sem ícone se não encontrar
try:
    root.iconbitmap('s.ico')
except:
    pass  # Continua a execução sem ícone se o arquivo não for encontrado

# 📋 SEÇÃO DO CARDÁPIO
# ===================

frame_cardapio = tk.Frame(root)
frame_cardapio.pack(padx=10, pady=10)

tk.Label(frame_cardapio, text="🍔 CARDÁPIO", font=("Arial", 16, "bold"), fg="darkred").pack()

# Checkboxes para itens do cardápio
itens_vars = {}
for item in cardapio:
    var = tk.IntVar()
    checkbox = tk.Checkbutton(frame_cardapio, 
                            text=f"{item} - R$ {cardapio[item]:.2f}", 
                            variable=var,
                            font=("Arial", 11))
    checkbox.pack(anchor='w')
    itens_vars[item] = var


# 📍 SEÇÃO DE ENDEREÇO
# ===================
frame_endereco = tk.Frame(root)
frame_endereco.pack(padx=10, pady=10, fill='x')
tk.Label(frame_endereco, text="📍 Endereço de entrega:", font=("Arial", 12, "bold")).pack(anchor='w')
entrada_endereco = tk.Entry(frame_endereco, width=50, font=("Arial", 10))
entrada_endereco.pack(fill='x', pady=5)

# 💳 SEÇÃO DE PAGAMENTO
# ====================
frame_pagamento = tk.Frame(root)
frame_pagamento.pack(padx=10, pady=10)
tk.Label(frame_pagamento, text="💳 Forma de pagamento:", font=("Arial", 12, "bold")).pack(anchor='w')

pagamento_var = tk.StringVar(value="Selecione")
pagamento_menu = tk.OptionMenu(frame_pagamento, pagamento_var, 
                              "Selecione", "Cartão de Crédito", "Cartão de Débito", "Pix", "Dinheiro")
pagamento_menu.pack(pady=5)

# 🔲 SEÇÃO DE BOTÕES DE AÇÃO
# ==========================
frame_botoes = tk.Frame(root)
frame_botoes.pack(padx=10, pady=20)

# Design responsivo e cores diferenciadas para cada ação
botao_calcular = tk.Button(frame_botoes, text="💰 Calcular Pedido", 
                          command=calcular_pedido,
                          bg="#4CAF50", fg="white", 
                          font=("Arial", 10, "bold"),
                          padx=10, pady=5)
botao_calcular.pack(side="left", padx=5)

botao_finalizar = tk.Button(frame_botoes, text="✅ Finalizar Pedido", 
                           command=finalizar_pedido,
                           bg="#2196F3", fg="white",
                           font=("Arial", 10, "bold"),
                           padx=10, pady=5)
botao_finalizar.pack(side="left", padx=5)

botao_historico = tk.Button(frame_botoes, text="📋 Histórico", 
                           command=visualizar_historico,
                           bg="#FF9800", fg="white",
                           font=("Arial", 10, "bold"),
                           padx=10, pady=5)
botao_historico.pack(side="left", padx=5)

# 🏠 RODAPÉ COM BRANDING
# ======================
frame_rodape = tk.Frame(root)
frame_rodape.pack(side="bottom", pady=10)
tk.Label(frame_rodape, text="🍕 Venâncio Delivery - Sempre fresquinho! 🍕", 
         font=("Arial", 9, "italic"), fg="gray").pack()

# 🚀 INICIALIZAÇÃO DA APLICAÇÃO
# =============================

root.mainloop()
