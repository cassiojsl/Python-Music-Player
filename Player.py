# -*- coding: utf-8 -*-

#Bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
import pygame
import os


i = Tk()
i.geometry('800x520+300+100')
i.title('Player')



fundo = PhotoImage(file="imagens/fundo.png")
janela = Label(i, image=fundo)
janela.pack(side='bottom', fill='both', expand=True)


#Frame

#Frame da Barra Topo
frame1 = Frame(janela)
frame1.pack()

#Frame da listbox
frame2 = Frame(janela, bg='',width=100)
frame2.pack()

#Frame dos botoes e barra de volume
frame4 = Frame(janela, bg='')
frame4.pack(side=BOTTOM)



selecionar = ()
selecionardir = ()
indice = 0
pausado = False
listamusicas = []


#Funções
def escolher(event=None):
    global selecionar,total_musicas,listamusicas
    selecionar = askopenfilenames(initialdir="/",
    filetypes=(("Formatos suportados", "*.mp3;*.ogg;*.wav"),("WAV", "*.wav"),("MP3", "*.mp3"),
    ("OGG", "*.ogg")),title="Selecione as suas músicas")

    if selecionar == (''):
        pass
    else:
        for a in selecionar:
            listamusicas.append(a)
    if selecionar:
        listbox.delete(0, last=END)
    for item in listamusicas:
        listbox.insert(END, item)


def escolherdir(evento=None):
    global selecionardir,total_musicas,listamusicas
    selecionardir = askdirectory(initialdir="/",
    title="Selecione as suas músicas")
    if selecionardir == (''):
        pass
    else:
        for arquivo in os.listdir(selecionardir):
            if arquivo.endswith(".mp3") or arquivo.endswith(".ogg") or arquivo.endswith(".wav"):
                dir_arq = os.path.join(selecionardir, arquivo)
                listamusicas.append(dir_arq)
    if selecionardir:
        listbox.delete(0, last=END)
    for item in listamusicas:
       listbox.insert(END, item)
       listbox.select_set(0)


def play(event=None):
    global selecionar,pausado,listamusicas,indice,listbox
    pygame.init()
    if listamusicas == []:
        pass
    else:
        if pausado == True:
            pygame.mixer.music.unpause()
            barratopo["text"] = 'REPRODUZINDO'
            pausado = False
        else:
            pygame.mixer.music.load(listamusicas[0])
            pygame.mixer.music.play()
            listbox.select_clear(0, last=END) #Remove o item anterior da seleção
            listbox.select_set(0) #seleciona o item atual para seleção
            barratopo["text"] = 'REPRODUZINDO'


def prox(event=None):
    global listamusicas,indice,listbox
    listbox.select_clear(0,last=END)
    indice += 1
    if indice == len(listamusicas):
        indice = 0
    pygame.mixer.music.load(listamusicas[indice])
    pygame.mixer.music.play()
    listbox.select_set(indice)
    barratopo["text"] = 'REPRODUZINDO'
    listbox.see(indice)

def ant(event=None):
    global listamusicas,indice
    listbox.select_clear(0,last=END)
    indice -= 1
    if indice == -1:
        indice = len(listamusicas)-1
    pygame.mixer.music.load(listamusicas[indice])
    pygame.mixer.music.play()
    listbox.select_set(indice)
    barratopo["text"] = 'REPRODUZINDO'
    listbox.see(indice)


def para(event=None):
    global indice
    listbox.select_clear(0,last=END)
    pygame.mixer.music.stop()
    barratopo["text"] = '...'
    indice = 0
    listbox.select_set(indice)


def pause(event=None):
    global pausado
    if pausado == False:
        pygame.mixer.music.pause()
        barratopo["text"] = 'PAUSA'
        pausado = True
    else:
        pygame.mixer.music.unpause()
        barratopo["text"] = 'REPRODUZINDO'
        pausado = False
        if selecionar == () or selecionardir == ():
            barratopo['text'] = '...'


def pergunta_sair(event=None):
    pergunta = messagebox.askyesno("Sair", 'Fechar o Player?', icon='info')
    if pergunta == 1:
        i.quit()



def atalhos(event=None):
    messagebox.showinfo("Atalhos", '"Enter" - Tocar\n\n"." - Avançar\n\n"," - Retroceder\n\n"Espaço" - Pausar\n\n"s" '
                                   '- ''Selecionar músicas\n\n"d" - Selecionar diretório\n\n"l" - Limpar\n\n""q" - Fechar\n\n',
                        icon='info')

def excluir(event=None):
    global listamusicas
    listamusicas = []
    listbox.delete(0, last=END)
    pygame.mixer.music.stop()
    barratopo["text"] = '...'

def salvar_playlist():
    global listamusicas
    playlist = asksaveasfile(mode='w',defaultextension='.txt',title="Salvar Playlist",filetypes=[("TXT","*.txt")],initialdir="/")
    if playlist == None:
        pass
    else:
        for i in listamusicas:
            playlist.write('{0}\n'.format(i))
        playlist.close()

def abrir_playlist():
    global listamusicas
    playlist = askopenfile(initialdir="Playlists/",title="Abrir Playlist",defaultextension='.txt')
    for i in playlist.read().splitlines():
        listamusicas.append(i)
    for item in listamusicas:
       listbox.insert(END, item)
    playlist.close()

    

#Ícones
anterior_icone = PhotoImage(file='imagens/musica_ant.gif',width="24",height="24")
pausa_icone = PhotoImage(file='imagens/pausa.gif',width="24",height="24")
tocar_icone = PhotoImage(file='imagens/tocar.gif',width="24",height="24")
proxima_icone = PhotoImage(file='imagens/prox_musica.gif',width="24",height="24")
parar_icone = PhotoImage(file='imagens/parar.gif',width="24",height="24")
abrir_icone = PhotoImage(file='imagens/add.gif',width="24",height="24")
salvarp = PhotoImage(file='imagens/salvarp.gif',width='24',height='24')
excluir_icone = PhotoImage(file='imagens/limpar.gif',width="24",height="24")


vol_mudo = PhotoImage(file='imagens/mute.gif',width="20",height="19")
vol_normal = PhotoImage(file='imagens/unmute.gif',width="20",height="19")
vol_medio = PhotoImage(file='imagens/vol_medio.gif',width='20',height='19')
vol_baixo = PhotoImage(file='imagens/volume_baixo.gif',width='20',height='19')


#Botões
anterior = Button(frame4,image=anterior_icone,command=ant)
pausa = Button(frame4,image=pausa_icone,command=pause)
tocar = Button(frame4,command=play,image=tocar_icone)
proxima = Button(frame4,image=proxima_icone,command=prox)
parar = Button(frame4,image=parar_icone,command=para)
abrir = Menubutton(frame4,image=abrir_icone,relief=RAISED)
excluir = Button(frame4,command=excluir,image=excluir_icone)
salvar_pl = Button(frame4,command=salvar_playlist,image=salvarp)


anterior.grid(row=0,column=0,padx=10,pady=10)
tocar.grid(row=0,column=1,padx=10,pady=10)
pausa.grid(row=0,column=2,padx=10,pady=10)
proxima.grid(row=0,column=3,padx=10,pady=10)
parar.grid(row=0,column=4,padx=10,pady=10)
abrir.grid(row=0,column=5,padx=10,pady=10)
salvar_pl.grid(row=0,column=6,padx=10,pady=10)
excluir.grid(row=0,column=7,padx=10,pady=10)

#Menu do botão Abir
btabrirmenu = Menu (abrir,tearoff = 0)
abrir["menu"] = btabrirmenu
btabrirmenu.add_command (label="Pasta", command=escolherdir)
btabrirmenu.add_command (label="Arquivos", command=escolher)
btabrirmenu.add_command (label="Playlist", command=abrir_playlist)

#Barras Superiores
barratopo = Label(frame1,text='...',bg='black',bd=8,fg='white',width=110)
barratopo.pack(side=TOP,fill=X)

BarraPlaylist = Label(frame2,text='PLAYLIST',bg='white',fg='black',width=90)
BarraPlaylist.pack()


#Listbox
listbox = Listbox(frame2,width=102,bd=3)
rolagemv = Scrollbar(frame2)  #Barra de rolagem vertical
rolagemh = Scrollbar(frame2)  #Barra de rolagem horizontal
listbox['yscrollcommand'] = rolagemv.set #Vinculando a listbox a barra de rolagem vertical.
listbox['xscrollcommand'] = rolagemh.set
rolagemv.pack(side=RIGHT,fill=Y)
rolagemh.pack(side=BOTTOM,fill=X)
listbox.pack()
rolagemv.config(command=listbox.yview)  #Tornando a listbox verticalmente rolável utilizando o método .yview
rolagemh.config(command=listbox.xview,orient='horizontal')

def selecionado(event):
    global listamusicas,indice
    if listamusicas == []:
        janela.focus_set()
    else:
        listbox.select_clear(indice)
        selecao = listbox.curselection()
        if selecao == ():
            selecao = (0,)
            listbox.select_set(0)
        indice = selecao[0]
        pygame.mixer.music.load(listamusicas[indice])
        pygame.mixer.music.play()
        barratopo["text"] = 'REPRODUZINDO'
        janela.focus_set()


#Barra Volume
def valor_volume(event):
    pygame.init()
    pygame.mixer.music.set_volume(volume.get())

    if volume.get() == 0.0:
        volume_imagem.config(image=vol_mudo)
    elif volume.get() > 0.0 and volume.get() <= 0.5:
        volume_imagem.config(image=vol_baixo)
    elif volume.get() > 0.5 and volume.get() <= 0.9:
        volume_imagem.config(image=vol_medio)
    else:
        volume_imagem.config(image=vol_normal)

volume = Scale(frame4,from_=0.0,to=1.0,resolution=0.01,showvalue=0,command=valor_volume,orient='horizontal')
volume.set(1.0) #Iniciar sempre no máximo
volume.grid(row=0,column=8,pady=0,padx=0)

volume_imagem = Label(frame4)
volume_imagem.grid(row=0,column=9,padx=0,pady=10)
volume_imagem.config(image=vol_normal)


#Barra de Menu
barramenu = Menu(janela)

menuabrir = Menu(barramenu, tearoff=0)
barramenu.add_cascade(label="Abrir", menu=menuabrir)
menuabrir.add_command(label="Selecionar arquivos",command=escolher)
menuabrir.add_command(label="Selecionar pasta",command=escolherdir)
menuabrir.add_separator()
menuabrir.add_command(label="Sair",command=pergunta_sair)

menuajuda = Menu(barramenu, tearoff=0)
barramenu.add_cascade(label="Ajuda", menu=menuajuda)
menuajuda.add_command(label="Atalhos",command=atalhos)

i.config(menu=barramenu)



#Eventos do teclado
janela.focus_set()
janela.bind('<Return>', play)
janela.bind('.', prox)
janela.bind(',', ant)
janela.bind('s', escolher)
janela.bind('d', escolherdir)
janela.bind('q', pergunta_sair)
janela.bind('<space>',pause)
janela.bind('a',atalhos)
janela.bind('l',excluir)
listbox.bind('<ButtonRelease-1>',selecionado)


i.resizable(width=False, height=False)


i.mainloop()