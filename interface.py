#Importando bibliotecas
import tkinter as tk
from tkinter import messagebox
from imc import classificar_imc, calcular_imc

#Função que calcula
def calcular(): 
    try: 
        peso = float(entrada_peso.get()) 
        altura = float(entrada_altura.get()) 
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc) 
        messagebox.showinfo("Resultado", f"Seu IMC é: {imc:.2f}\nClassificação: {classificacao}") 
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para peso e altura.")

#Criação da janela
janela = tk.Tk()
janela.title("Calculadora IMC")

label_peso = tk.Label(janela, font=("", 15), text="Digite peso (Kg):")
label_peso.grid(column=0, row=0, padx=10, pady=10)

entrada_peso = tk.Entry(janela, font=("", 15))
entrada_peso.grid(column=1, row=0, padx=10, pady=10)

label_altura = tk.Label(janela, font=("", 15), text="Digite altura (m):")
label_altura.grid(column=0, row=1, padx=10, pady=10)

entrada_altura = tk.Entry(janela, font=("", 15))
entrada_altura.grid(column=1, row=1, padx=10, pady=10)

botao_p_calcular = tk.Button(janela, text="Calcular IMC", command=calcular)
botao_p_calcular.grid(columnspan=2, row=3, padx=10, pady=10)

janela.mainloop()
