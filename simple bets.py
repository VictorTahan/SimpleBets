import random
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

root = Tk()
class App():
    def __init__(self):
        self.times = ['Palmeiras','Corinthians','São Paulo','Santos']
        self.root = root
        self.saldo_=0
        self.tela()
        self.frame_game()
        self.saldo()
        self.botao_sair()
        self.images()
        root.mainloop()
    def sortear_placar(self):
        self.placar_mandante = random.randint(0,5)
        self.placar_visitante = random.randint(0,5)
    def sortear_times(self):
        self.time_mandante, self.time_visitante = random.sample(self.times, 2)
    def saldo(self):
        if hasattr(self, 'bt_jgnovamente'):
            self.bt_jgnovamente.place_forget()
        self.label_saldo = Label(self.framegame,text='Insira seu saldo:',font=('verdana',8,'bold'),bg='#6ae845')
        self.label_saldo.place(relx=0.05,rely=0.1,relwidth=0.5)
        self.spinbox_saldo = ttk.Spinbox(self.framegame,from_=0,to=float('Inf'),increment=0.01)
        self.spinbox_saldo.place(relx=0.45,rely=0.1,relwidth=0.15)
        self.bt_inserir = Button(self.framegame,text='Inserir',bd=2,font=('verdana',8,'bold'),command=self.update_saldo)
        self.bt_inserir.place(relx=0.62,rely=0.1,relwidth=0.2)
    def aposta(self):
        self.label_aposta = Label(self.framegame,text='Valor da sua aposta:',font=('verdana',8,'bold'),bg='#6ae845')
        self.label_aposta.place(relx=0.12,rely=0.15,relwidth=0.4)
        self.spinbox_aposta = ttk.Spinbox(self.framegame,from_=0.01,to=float(self.saldo_),increment=0.01)
        self.spinbox_aposta.place(relx=0.5,rely=0.15,relwidth=0.15)
        self.bt_apostar = Button(self.framegame,text='Apostar!',bd=2,font=('verdana',8,'bold'),command=self.startbutton)
        self.bt_apostar.place(relx=0.7,rely=0.15,relwidth=0.2)
    def update_saldo(self):
        self.saldo_upd = float(self.spinbox_saldo.get())
        if self.saldo_upd <= 0:
            messagebox.showerror('ERRO', 'seu saldo deve ser de no mínimo $0.01.')
            return
        self.spinbox_saldo.config(state='disable')
        self.bt_inserir.config(state='disable')
        self.score()
        self.aposta()
    def tela(self):
        self.root.title('Faça suas apostas!')
        self.root.configure(background='#6ae845')
        self.root.geometry('375x667')
        self.root.resizable(False,False)
    def score(self):
        self.saldo_ += self.saldo_upd
        self.label_score = Label(self.framegame,text='Saldo:',font=('verdana',8,'bold'),bg='#6ae845')
        self.label_score.place(relx=0.1,rely=0.2,relwidth=0.25)
        saldo_string = f'{self.saldo_:.2f}'
        self.label_score_value = Label(self.framegame,text=saldo_string,font=('verdana',8,'bold'))
        self.label_score_value.place(relx=0.3,rely=0.2,relwidth=0.25)
    def partida(self):
        self.limpar_partida()
        self.botao_start.place_forget()
        self.label_partida=Label(self.framegame,text=f'A partida será entre {self.time_mandante} e {self.time_visitante}',font=('verdana',8,'bold'),bg='#6ae845')
        self.label_partida.place(relx=0,rely=0.25,relwidth=1)
        self.label_bet_mandante = Label(self.framegame,text=f'Quantos gols marcará o {self.time_mandante}?',font=('verdana',8,'bold'),bg='#6ae845')
        self.label_bet_mandante.place(relx=0.02,rely=0.3,relwidth=1)
        self.spinbox_bet_mandante = Spinbox(self.framegame, from_=0, to=5, increment=1)
        self.spinbox_bet_mandante.place(relx=0.18,rely=0.35,relwidth=0.1)
        self.label_bet_visitante = Label(self.framegame,text=f'Quantos gols marcará o {self.time_visitante}?',font=('verdana',8,'bold'),bg='#6ae845')
        self.label_bet_visitante.place(relx=0.02,rely=0.4,relwidth=1)
        self.spinbox_bet_visitante = Spinbox(self.framegame, from_=0, to=5, increment=1)
        self.spinbox_bet_visitante.place(relx=0.18,rely=0.45,relwidth=0.1)
        self.show_images()
        self.submitbutton()
    def startbutton(self):
        self.sortear_placar()
        self.sortear_times()
        self.aposta_valor = float(self.spinbox_aposta.get())
        if self.aposta_valor > self.saldo_:
            messagebox.showerror('Erro', 'A aposta não pode ser maior que o saldo disponível.')
            return
        elif self.aposta_valor <= 0:
            messagebox.showerror('ERRO','Sua aposta deve ser de no mínimo $0.01')
            return
        self.saldo_ -= self.aposta_valor
        self.label_score_value.config(text=f'{self.saldo_:.2f}')
        self.spinbox_aposta.config(state='disable')
        self.bt_apostar.config(state='disable')
        self.label_suaaposta = Label(self.framegame,text=f'Aposta:{self.aposta_valor:.2f}',font=('verdana',8,'bold'),bg='#6ae845')
        self.label_suaaposta.place(relx=0.6,rely=0.2,relwidth=0.25)
        self.label_premiacao = Label(self.framegame,text='Prêmio:',font=('verdana',8,'bold'),bg='#6ae845')
        self.label_premiacao.place(relx=0.1,rely=0.01,relwidth=0.2)
        self.label_acertarplacar = Label(self.framegame,text=f'Acertar o placar = {(self.aposta_valor * 35.0):.2f}',font=('verdana',8,'bold'),fg='#11ab03')
        self.label_acertarplacar.place(relx=0.3,rely=0.01,relwidth=0.5)
        self.label_acertarempate = Label(self.framegame,text=f'Acertar um empate sem acertar o placar = {(self.aposta_valor*5.0):.2f}',font=('verdana',8,'bold'),fg='#0722ed')
        self.label_acertarempate.place(relx=0.1,rely=0.04,relwidth=0.9)
        self.label_acertarvencedor = Label(self.framegame,text=f'Acertar o vencedor sem acertar o placar = {(self.aposta_valor*1.2):.2f}',font=('verdana',8,'bold'),fg='#8c8c0d')
        self.label_acertarvencedor.place(relx=0.1,rely=0.07,relwidth=0.9)
        self.botao_start = Button(self.framegame,text='Aperte aqui para sortear uma partida',bd=2,font=('verdana',8,'bold'),command=self.partida)
        self.botao_start.place(relx=0,rely=0.8,relwidth=1)
    def resultado(self):
        self.submitbt.place_forget()
        self.label_resultado = Label(self.framegame,text=f'O resultado da partida foi: {self.time_mandante} {self.placar_mandante}-{self.placar_visitante} {self.time_visitante}',
                                font=('verdana',8,'bold'),bg='#6ae845')
        self.label_resultado.place(relx=0.02,rely=0.7,relwidth=1)
        self.label_resultado2 = Label(self.framegame,text=f'{self.placar_mandante} - {self.placar_visitante}',font=('verdana',12,'bold'),bg='#6ae845')
        self.label_resultado2.place(relx=0.45,rely=0.56)
        bet_mandante = int(self.spinbox_bet_mandante.get())
        bet_visitante = int(self.spinbox_bet_visitante.get())
        if bet_mandante == self.placar_mandante and bet_visitante == self.placar_visitante:
            self.saldo_ = self.saldo_ + self.aposta_valor * 35
            self.label_score_value.config(text=f'{self.saldo_:.2f}')
            self.label_score_3pt = Label(self.framegame,text=f'+${(self.aposta_valor * 35.0):.2f}',font=('verdana',12,'bold'),bg='#6ae845',fg='#11ab03')
            self.label_score_3pt.place(relx=0.4,rely=0.5)
        elif self.placar_mandante > self.placar_visitante and bet_mandante > bet_visitante:
            self.saldo_ = self.saldo_ + self.aposta_valor * 1.2
            self.label_score_value.config(text=f'{self.saldo_:.2f}')
            self.label_score_1pt = Label(self.framegame,text=f'+${(self.aposta_valor * 1.2):.2f}',font=('verdana',12,'bold'),bg='#6ae845',fg='#8c8c0d')
            self.label_score_1pt.place(relx=0.4,rely=0.5)
        elif self.placar_mandante < self.placar_visitante and bet_mandante < bet_visitante:
            self.saldo_ = self.saldo_ + self.aposta_valor * 1.2
            self.label_score_value.config(text=f'{self.saldo_:.2f}')
            self.label_score_1pt = Label(self.framegame,text=f'+${(self.aposta_valor * 1.2):.2f}',font=('verdana',12,'bold'),bg='#6ae845',fg='#8c8c0d')
            self.label_score_1pt.place(relx=0.4,rely=0.5)
        elif self.placar_mandante == self.placar_visitante and bet_mandante == bet_visitante:
            self.saldo_ = self.saldo_ + self.aposta_valor * 5
            self.label_score_value.config(text=f'{self.saldo_:.2f}')
            self.label_score_1pt = Label(self.framegame,text=f'+${(self.aposta_valor * 5.0):.2f}',font=('verdana',12,'bold'),bg='#6ae845',fg='#0722ed')
            self.label_score_1pt.place(relx=0.4,rely=0.5)
        else:
            self.label_score_value.config(text=f'{self.saldo_:.2f}')
            self.label_0pt = Label(self.framegame,text=f'-${(self.aposta_valor):.2f}',font=('verdana',12,'bold'),bg='#6ae845',fg='#e60000')
            self.label_0pt.place(relx=0.29,rely=0.5)
        self.jogar_novamente()
        self.inserir_mais_saldo()
    def submitbutton(self):
        self.submitbt = Button(self.framegame,text='Submit',font=('verdana',8,'bold'),command=self.resultado)
        self.submitbt.place(relx=0,rely=0.8,relwidth=1)
    def jogar_novamente(self):
        self.bt_jgnovamente = Button(self.framegame,text='Jogar novamente',font=('verdana',8,'bold'),command=self.novo_jogo)
        self.bt_jgnovamente.place(relx=0,rely=0.75,relwidth=1)
    def inserir_mais_saldo(self):
        self.bt_inserirmaissaldo = Button(self.framegame,text='Inserir novo saldo',font=('verdana',8,'bold'),command=self.saldo)
        self.bt_inserirmaissaldo.place(relx=0,rely=0.8,relwidth=1)
    def botao_sair(self):
        self.bt_exit = Button(self.framegame,text='Sacar saldo e sair',font=('verdana',8,'bold'),command=self.exit)
        self.bt_exit.place(relx=0,rely=0.85,relwidth=1)
    def novo_jogo(self):
        self.limpar_partida()
        self.aposta()
        self.inserir_mais_saldo()
    def limpar_partida(self):
        if hasattr(self, 'label_partida'):
            self.label_partida.destroy()
        if hasattr(self, 'label_bet_mandante'):
            self.label_bet_mandante.destroy()
        if hasattr(self, 'spinbox_bet_mandante'):
            self.spinbox_bet_mandante.destroy()
        if hasattr(self, 'label_bet_visitante'):
            self.label_bet_visitante.destroy()
        if hasattr(self, 'spinbox_bet_visitante'):
            self.spinbox_bet_visitante.destroy()
        if hasattr(self, 'img_mandante_label'):
            self.img_mandante_label.destroy()
        if hasattr(self, 'img_visitante_label'):
            self.img_visitante_label.destroy()
        if hasattr(self, 'label_resultado'):
            self.label_resultado.destroy()
        if hasattr(self, 'label_resultado2'):
            self.label_resultado2.destroy()
        if hasattr(self, 'label_score_3pt'):
            self.label_score_3pt.destroy()
        if hasattr(self, 'label_score_1pt'):
            self.label_score_1pt.destroy()
        if hasattr(self, 'label_0pt'):
            self.label_0pt.destroy()
        if hasattr(self, 'submitbt'):
            self.submitbt.place_forget()
        if hasattr(self, 'bt_jgnovamente'):
            self.bt_jgnovamente.place_forget()
        if hasattr(self, 'bt_inserirmaissaldo'):
            self.bt_inserirmaissaldo.place_forget()
    def images(self):
        self.palmeiras_path = os.path.join(BASE_DIR, 'images', 'palmeiras 50px.png')
        self.pil_palmeiras = Image.open(self.palmeiras_path)
        self.tk_palmeiras = ImageTk.PhotoImage(self.pil_palmeiras)
        self.corinthians_path = os.path.join(BASE_DIR, 'images', 'corinthians 50px.png')
        self.pil_corinthians_path = Image.open(self.corinthians_path)
        self.tk_corinthians = ImageTk.PhotoImage(self.pil_corinthians_path)
        self.saopaulo_path = os.path.join(BASE_DIR, 'images', 'sao paulo 50px.png')
        self.pil_saopaulo = Image.open(self.saopaulo_path)
        self.tk_saopaulo = ImageTk.PhotoImage(self.pil_saopaulo)
        self.santos_path = os.path.join(BASE_DIR, 'images', 'santos 50px.png')
        self.pil_santos = Image.open(self.santos_path)
        self.tk_santos = ImageTk.PhotoImage(self.pil_santos)
    def show_images(self):
        time_imagem = {'Palmeiras': self.tk_palmeiras, 'Corinthians': self.tk_corinthians, 'São Paulo': self.tk_saopaulo, 'Santos': self.tk_santos}
        if self.time_mandante in time_imagem:
            self.img_mandante_label = Label(self.framegame,image=time_imagem[self.time_mandante], bg='#6ae845')
            self.img_mandante_label.place(relx=0.3, rely=0.5, relwidth=0.15, relheight=0.15)
        if self.time_visitante in time_imagem:
            self.img_visitante_label = Label(self.framegame, image=time_imagem[self.time_visitante], bg='#6ae845')
            self.img_visitante_label.place(relx=0.56, rely=0.5, relwidth=0.15, relheight=0.15)
    def frame_game(self):
        self.framegame = Frame(self.root,bg='#6ae845')
        self.framegame.place(relx=0,rely=0,relwidth=1,relheight=1)
    def exit(self):
        self.root.quit()
App()