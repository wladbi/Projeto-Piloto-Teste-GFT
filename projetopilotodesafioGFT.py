from tkinter import Tk, DoubleVar, Label, Entry, Button, StringVar

class FluxoCaixa:
    def __init__(self):
        self.root = Tk()
        self.despesas = []
        self.receitas = []
        self.configurar_janela()
        self.criar_campos()
        self.root.mainloop()

    def configurar_janela(self):
        self.root.title("Fluxo de caixa - Simples")
        self.root.configure(background='#B0C4DE')
        self.root.geometry("350x150")
        self.root.resizable(False, False)

    def criar_campos(self):
        self.entrada_receita = self.criar_campo('Receita:', 0.05)
        self.entrada_despesa = self.criar_campo('Despesa:', 0.2)

        self.bt_calcular = Button(self.root, text='Adicionar', font=("verdana", 10, "bold"), command=self.calcular)
        self.bt_calcular.place(relx=0.3, rely=0.35, relwidth=0.4, relheight=0.17)

        self.resultado_final = StringVar()
        self.resultado_final_label = Label(self.root, textvariable=self.resultado_final)
        self.resultado_final_label.place(relx=0.1, rely=0.55, relwidth=0.8, relheight=0.35)

    def criar_campo(self, texto, posicao):
        label = Label(self.root, text=texto, font=('Verdana', '8', 'bold'), bg='#D3D3D3', fg='#000000')
        label.place(relx=0.15, rely=posicao, relwidth=0.25, relheight=0.1)
        entrada = DoubleVar()
        campo = Entry(self.root, textvariable=entrada)
        campo.place(relx=0.45, rely=posicao, relwidth=0.15, relheight=0.1)
        return entrada

    def calcular(self):
        receita = self.entrada_receita.get()
        despesa = self.entrada_despesa.get()
        self.receitas.append(receita)
        self.despesas.append(despesa)
        saldo = sum(self.receitas) - sum(self.despesas)
        total_receitas = sum(self.receitas)
        total_despesas = sum(self.despesas)
        texto = f'O saldo atual é de {saldo}.\nO total das receitas é de {total_receitas}.' \
                f'\nO total das despesas é de {total_despesas}.'
        self.resultado_final.set(texto)

if __name__ == "__main__":
    FluxoCaixa()
