#janela
#titulo
#campos para selecionar as moedas de origem e destino
#botão para converter
#lista de exibição com os nomes das moedas 

#importar a biblioteca que vai fazer a janela

import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_cotacao_moeda


#criar e configurar a janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

janela = customtkinter.CTk()
janela.geometry("400x600")
janela.title("calculadora.ico")

dic_conversoes_disponiveis = conversoes_disponiveis()

#criar os botões, textos e demais elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de moedas", font=("", 28))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem", font=("", 18))
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino", font=("", 18))

def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destino)
    campo_moeda_destino.set(lista_moedas_destino[0])

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()), command=carregar_moedas_destino, font=("", 14))
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values= ["selecione uma moeda de origem"])

def converter_moeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    if moeda_origem and moeda_destino:
        cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)
        texto_cotacao_moeda.configure(text=f"1 {moeda_origem} = {cotacao} {moeda_destino}")


botão_converter = customtkinter.CTkButton(janela, text= "Converter", command=converter_moeda, font=("", 20), hover_color="#00A6AD")

lista_moedas = customtkinter.CTkScrollableFrame(janela)

texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="", font=("", 20))

moedas_disponiveis = nomes_moedas()

for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moeda}: {nome_moeda}", font=("", 14)) 
    texto_moeda.pack()



#colocar os elementos criados na tela
titulo.pack()
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10, pady=10)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10, pady=10)
botão_converter.pack(padx=10, pady=10)
texto_cotacao_moeda.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)

#rodar a janela
janela.mainloop()