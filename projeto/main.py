import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_cotacao_moeda

# Configurações iniciais da janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("600x600")

dic_conversoes_disponiveis = conversoes_disponiveis()

# criar elementos da interface
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("Arial", 30), text_color="white")
moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de Origem", font=("Arial", 15), text_color="white")
valor = customtkinter.CTkLabel(janela, text="Digite o valor a ser convertido", font=("Arial", 15), text_color="white")
moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de Destino", font=("Arial", 15), text_color="white")

def carregar_moedas_destino(moeda_selecionada):
     lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
     campo_moeda_destino.configure(values=lista_moedas_destino)
     campo_moeda_destino.set(lista_moedas_destino[0])  

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()), command=carregar_moedas_destino)
campo_valor = customtkinter.CTkEntry(janela, placeholder_text="Valor")
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["Selecione uma moeda"])
campo_valor_convertido = customtkinter.CTkLabel(janela, text="", font=("Arial", 15), text_color="white")

def converter_moeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    if moeda_origem and moeda_destino != "Selecione uma moeda":
        cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)

        valor_digitado = float(campo_valor.get().replace(",", "."))
        resultado = valor_digitado * float(cotacao)

        campo_valor_convertido.configure(text=f"{valor_digitado:.2f} {moeda_origem} = {resultado:.2f} {moeda_destino}", font=("Arial", 15), text_color="white")
    else:
        campo_valor_convertido.configure(text="Selecione a moeda de origem para liberar as de destino", font=("Arial", 15), text_color="white")

botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda)

lista_moedas = customtkinter.CTkScrollableFrame(janela, width=400, height=200)

moedas_disponiveis = nomes_moedas()
{"USD": "Dólar Americano", "EUR": "Euro", "BRL": "Real Brasileiro", "PYG": "Guarani Paraguaio", "JPY": "Iene Japonês", "GBP": "Libra Esterlina", "CHF": "Franco Suíço", "CAD": "Dólar Canadense", "CNY": "Yuan Chinês", "BTC": "Bitcoin"}
for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    label_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moeda}: {nome_moeda}", font=("Arial", 12), text_color="white")
    label_moeda.pack()

# organizar elementos na janela
titulo.pack(padx=10, pady=10)
moeda_origem.pack(padx=10)
campo_moeda_origem.pack(padx=10, pady=10)

valor.pack(padx=10)
campo_valor.pack(padx=10, pady=10)
campo_valor_convertido.pack(padx=10, pady=10)

moeda_destino.pack(padx=10)
campo_moeda_destino.pack(padx=10, pady=10)

botao_converter.pack(padx=10, pady=10)

lista_moedas.pack(padx=10, pady=10)

# roda a janela
janela.mainloop()