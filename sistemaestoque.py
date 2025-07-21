import tkinter as tk
from tkinter import messagebox


cardapio = {
    'X- Vieri': 30.00,
    'X- Emerson': 35.00,
    'MEGA-MARCÃO': 50.00,
    'FRAPOTINO': 10.00,
    'Refrigerante': 5.00,
    'Batata' : 8.00
}


def calcular_pedido():
    total = 0 
    tempo_entrega = 0
    
   
    for item, var in itens_vars.items():
        if var.get() == 1:
            total += cardapio[item]
            tempo_entrega += 10  
    
    if total == 0:
        messagebox.showwarning("Aviso", "Selecione ao menos um item.")
        return
    
   
    messagebox.showinfo("Resumo do Pedido", f"Total: R$ {total:.2f}\nTempo estimado de entrega: {tempo_entrega} minutos")


def finalizar_pedido():
    endereco = entrada_endereco.get()
    pagamento = pagamento_var.get()
    
    if not endereco or pagamento == "Selecione":
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
        return
    

    messagebox.showinfo("Pedido Concluído", f"Pedido finalizado!\nEndereço: {endereco}\nForma de pagamento: {pagamento}")
    
   
    for var in itens_vars.values():
        var.set(0)
    entrada_endereco.delete(0, tk.END)
    pagamento_var.set("Selecione")


root = tk.Tk()
root.title("Venâncio Delivery <3" )
root.iconbitmap('s.ico') 

frame_cardapio = tk.Frame(root)
frame_cardapio.pack(padx=10, pady=10)

tk.Label(frame_cardapio, text="Cardápio", font=("Arial", 14)).pack()


itens_vars = {}
for item in cardapio:
    var = tk.IntVar()
    tk.Checkbutton(frame_cardapio, text=f"{item} - R$ {cardapio[item]:.2f}", variable=var).pack(anchor='w')
    itens_vars[item] = var


frame_endereco = tk.Frame(root)
frame_endereco.pack(padx=10, pady=10)
tk.Label(frame_endereco, text="Endereço de entrega:").pack(anchor='w')
entrada_endereco = tk.Entry(frame_endereco, width=50)
entrada_endereco.pack()


frame_pagamento = tk.Frame(root)
frame_pagamento.pack(padx=10, pady=10)
tk.Label(frame_pagamento, text="Forma de pagamento:").pack(anchor='w')

pagamento_var = tk.StringVar(value="Selecione")
pagamento_menu = tk.OptionMenu(frame_pagamento, pagamento_var, "Selecione", "Cartão de Crédito", "Pix", "Dinheiro")
pagamento_menu.pack()


frame_botoes = tk.Frame(root)
frame_botoes.pack(padx=10, pady=10)

botao_calcular = tk.Button(frame_botoes, text="Calcular Pedido", command=calcular_pedido)
botao_calcular.pack(side="left", padx=5)

botao_finalizar = tk.Button(frame_botoes, text="Finalizar Pedido", command=finalizar_pedido)
botao_finalizar.pack(side="left", padx=5)

root.mainloop()
