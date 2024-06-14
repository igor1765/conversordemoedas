#janela
#titulo
#campos para selecionar as moedas de origem e destino
#botão para converter
#lista de exibição com os nomes das moedas 
import customtkinter

#importar a biblioteca que vai fazer a janela

#criar e configurar a janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

janela = customtkinter.CTk()
janela.geometry("400x400")

#criar os botões, textos e demais elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de moedas", font=("", 28))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem", font=("", 18))
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino", font=("", 18))
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values= ["USD", "BRL" , "BTC"], font=("", 14), text_color="black" )
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values= ["USD", "BRL" , "BTC"])

def converter_moeda():
    print("Converter_moeda")


botão_converter = customtkinter.CTkButton(janela, text= "Converter", command=converter_moeda, font=("", 20), hover_color="#00A6AD")

lista_moedas = customtkinter.CTkScrollableFrame(janela)
moedas_disponiveis = ["USD: dólar americano", "EUR: euro", "BRL: real brasileiro","BTC: bitcoin"]

for moeda in moedas_disponiveis:
    texto_moeda = customtkinter.CTkLabel(lista_moedas, 
    text=moeda)
    texto_moeda.pack()



#colocar os elementos criados na tela
titulo.pack()
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10, pady=10)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10, pady=10)
botão_converter.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)

#rodar a janela
janela.mainloop()