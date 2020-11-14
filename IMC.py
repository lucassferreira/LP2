try:
    from Tkinter import*
except:
    from tkinter import*

class main:
    def __init__(self, master=None):

        self.tela = master
        self.tela.resizable(False, False)
        self.tela.title('Cálculo do IMC - Índice de Massa Corporal')
        largura = 500
        altura = 300

        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        posx = (largura_screen / 2) - (largura / 2)
        posy = (altura_screen / 2) - (altura / 2)
        self.tela.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

        self.lb_nome = Label(self.tela, text='Nome do Paciente: ')
        self.lb_nome.place(x=10, y=20)
        self.e_nome = Entry(self.tela)
        self.e_nome.place(x=140, y=20, width=280)
        self.e_nome.focus()

        self.lb_ender = Label(self.tela, text='Endereço Completo: ')
        self.lb_ender.place(x=10, y=50)
        self.e_ender = Entry(self.tela)
        self.e_ender.place(x=140, y=50, width=280)

        self.lb_alt = Label(self.tela, text='Altura(cm): ')
        self.lb_alt.place(x=10, y=80)
        self.e_alt = Entry(self.tela)
        self.e_alt.place(x=140, y=80, width=80)

        self.lb_peso = Label(self.tela, text='Peso(Kg): ')
        self.lb_peso.place(x=10, y=110)
        self.e_peso = Entry(self.tela)
        self.e_peso.place(x=140, y=110, width=80)

        self.t_resultado = Text(self.tela)
        self.t_resultado.configure(state='disabled', font=('', 9))
        self.t_resultado.place(x=240, y=80, width=180, height=100)

        self.bt_calc = Button(self.tela, text='Calcular', command=self.calcular)
        self.bt_calc.place(x=140, y=200, width=80)
        self.bt_rein = Button(self.tela, text='Reiniciar', command=self.reiniciar)
        self.bt_rein.place(x=230, y=200, width=80)
        self.bt_sair = Button(self.tela, text='Sair', command=self.sair)
        self.bt_sair.place(x=340, y=200, width=80)

    def calcular(self):
        try:
            altura = float(self.e_alt.get())
            peso = float(self.e_peso.get())
            resultado = peso / (altura / 100 * altura / 100)
            situacao = self.retorna_situacao(resultado)
            self.t_resultado.configure(state=NORMAL)
            self.t_resultado.delete('1.0', END)  # Limpar result anterior
            self.t_resultado.insert(END, '\nRESULTADO: %.2f\n' % resultado)
            self.t_resultado.insert(END, '\n%s' % situacao)
            self.t_resultado.configure(state=DISABLED)
        except:
            pass

    def retorna_situacao(self, valor):
        self.imc = valor
        if (self.imc < 17.00):
            return 'Situação:\n Muito abaixo do peso!'
        elif (self.imc >= 17.00) and (self.imc <= 18.49):
            return 'Situação:\n Abaixo do peso!'
        elif (self.imc >= 18.50) and (self.imc <= 24.99):
            return 'Situação:\n Peso normal!'
        elif (self.imc >= 25.00) and (self.imc <= 29.99):
            return 'Situação:\n Acima do peso!'
        elif (self.imc >= 30.00) and (self.imc <= 34.99):
            return 'Situação:\n Obesidade I!'
        elif (self.imc >= 35.00) and (self.imc <= 39.99):
            return 'Situação:\n Obesidade II (severa)!'
        elif (self.imc >= 40.00):
            return 'Situação:\n Obesidade III (mórbida)!'
        else:
            return 'Valores informados inválidos!'

    def reiniciar(self):
        self.e_nome.delete(0, END)
        self.e_ender.delete(0, END)
        self.e_peso.delete(0, END)
        self.e_alt.delete(0, END)
        self.t_resultado.configure(state=NORMAL)
        self.t_resultado.delete('1.0', END)  # Limpar result anterior
        self.t_resultado.configure(state=DISABLED)

    def sair(self):
        self.tela.destroy()


if __name__ == '__main__':
    root = Tk()
    application = main(root)
    root.mainloop()
