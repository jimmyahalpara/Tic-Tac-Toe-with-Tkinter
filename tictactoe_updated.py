import pickle
from Tkinter import *
import tkMessageBox
import tkColorChooser
class Maingamemodule:
    def __init__(self):
        try:
            s=open('highscore.dtt','rb+')
            s.close()
        except:
            s=open('highscore.dtt','wb+')
            pickle.dump(['',0,''],s)
            s.close()
        self.history=[]
        self.position={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
        self.panelhistory=''
        self.turn=0
        self.player1score=0
        self.player2score=0
        self.state='off'
        self.normal_button='SystembuttonFace'
        self.normal_clickedbutton='grey'
        self.initial_playpad='pink'
        self.gamestarted_playpad='green'
        self.x_playpad='yellow'
        self.o_playpad='cyan'
        self.won_playpad='red'
        self.background='SystemButtonFace'

    def exxit(self):
        self.mainwindow.destroy()
        exit()

    def appendpanel(self,s):
        self.panelhistory+='\n'+s
        self.textbox.insert('1.0','\n'+s)
    def returnthebox(self):
        st='+---+---+---+\n| '+self.position[1]+' | '+self.position[2]+' | '+self.position[3]+' |\n+---+---+---+\n| '+self.position[4]+' | '+self.position[5]+' | '+self.position[6]+' |\n+---+---+---+\n| '+self.position[7]+' | '+self.position[8]+' | '+self.position[9]+' |\n+---+---+---+\n'
        self.appendpanel(st)
    
    def createwindow(self):
        self.mainwindow=Tk(screenName='Tic-Tac-Toe',baseName='Tic_tac_toe',className='Maingame_menu')
        self.menubar=Menu(self.mainwindow)
        self.gamemenu=Menu(self.menubar,tearoff=0)
        self.gamemenu.add_command(label='New game',command=self.gamerestart)
        self.gamemenu.add_command(label='Restart Game',command=self.restart)
        self.gamemenu.add_separator()
        self.gamemenu.add_command(label='exit',command=self.exxit)
        self.menubar.add_cascade(label='Game',menu=self.gamemenu)
        self.historymenu=Menu(self.menubar,tearoff=0)
        self.historymenu.add_command(label='Show History',command=self.showhistory)
        self.historymenu.add_command(label='Show Highscore',command=self.showhighscore)
        self.historymenu.add_command(label='Show Panel History',command=self.showpanel)
        self.historymenu.entryconfig(0,state=DISABLED)
        self.historymenu.entryconfig(1,state=DISABLED)
        self.historymenu.entryconfig(2,state=DISABLED)
        self.gamemenu.entryconfig(1,state=DISABLED)
        self.menubar.add_cascade(label='History',menu=self.historymenu)
        self.helpmenu=Menu(self.menubar,tearoff=0)
        self.helpmenu.add_command(label='Info',command=self.printinfo)
        self.helpmenu.add_command(label='Credits',command=self.showcredits)
        self.menubar.add_cascade(label='Help',menu=self.helpmenu)
        self.colormenu=Menu(self.menubar,tearoff=0)
        self.colormenu.add_command(label='Choosecolor',command=self.choosecolor)
        self.menubar.add_cascade(label='Colours',menu=self.colormenu)
        self.mainwindow.config(menu=self.menubar)
        
        self.frame1=Frame(self.mainwindow,bg=self.background,width=500,height=210)
        self.frame1.pack(side=LEFT)
        self.frame2=Frame(self.mainwindow,bg=self.background,width=100,height=210)
        self.frame2.place(x=320,y=10)
        
        Label(self.frame1,text='Player 1 name:').place(x=6,y=5)
        self.player1name=StringVar()
        self.enterplayer1name=Entry(self.frame1,textvariable=self.player1name,width=10)
        self.enterplayer1name.place(x=90,y=5)
        Label(self.frame1,text='Player 2 name:').place(x=150,y=5)
        self.player2name=StringVar()
        self.enterplayer2name=Entry(self.frame1,textvariable=self.player2name,width=10)
        self.enterplayer2name.place(x=235,y=5)
        self.startbutton=Button(self.frame1,text='Start',command=self.startframe1)
        self.startbutton.place(x=50,y=30)
        
        self.button1=Button(self.frame1,bg=self.initial_playpad,width=4,height=2,state=DISABLED,text=' ',command=lambda:self.play(1))
        self.button1.place(x=30,y=70)
        self.button2=Button(self.frame1,bg=self.initial_playpad,width=4,height=2,state=DISABLED,text=' ',command=lambda:self.play(2))
        self.button2.place(x=70,y=70)
        self.button3=Button(self.frame1,bg=self.initial_playpad,width=4,height=2,state=DISABLED,text=' ',command=lambda:self.play(3))
        self.button3.place(x=110,y=70)
        self.button4=Button(self.frame1,bg=self.initial_playpad,width=4,height=2,state=DISABLED,text=' ',command=lambda:self.play(4))
        self.button4.place(x=30,y=115)
        self.button5=Button(self.frame1,bg=self.initial_playpad,width=4,height=2,state=DISABLED,text=' ',command=lambda:self.play(5))
        self.button5.place(x=70,y=115)
        self.button6=Button(self.frame1,bg=self.initial_playpad,width=4,height=2,state=DISABLED,text=' ',command=lambda:self.play(6))
        self.button6.place(x=110,y=115)
        self.button7=Button(self.frame1,bg=self.initial_playpad,width=4,height=2,state=DISABLED,text=' ',command=lambda:self.play(7))
        self.button7.place(x=30,y=160)
        self.button8=Button(self.frame1,bg=self.initial_playpad,width=4,height=2,state=DISABLED,text=' ',command=lambda:self.play(8))
        self.button8.place(x=70,y=160)
        self.button9=Button(self.frame1,bg=self.initial_playpad,width=4,height=2,state=DISABLED,text=' ',command=lambda:self.play(9))
        self.button9.place(x=110,y=160)

        self.restartbutton=Button(self.frame1,text='Restart',state=DISABLED,command=self.restart)
        self.restartbutton.place(x=170,y=100)
        self.gamerestartbutton=Button(self.frame1,text='Restart Game',state=DISABLED,command=self.gamerestart)
        self.gamerestartbutton.place(x=170,y=140)
        
        self.scrollbar=Scrollbar(self.frame2)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.textbox=Text(self.frame2,yscrollcommand=self.scrollbar.set,width=19,height=10,state=DISABLED)
        self.textbox.pack(fill=BOTH)
        self.scrollbar.config(command=self.textbox.yview)

        self.startbutton.bind('<Enter>',self.startbuttonin)
        self.startbutton.bind('<Leave>',self.startbuttonout)
        self.restartbutton.bind('<Enter>',self.restartbuttonin)
        self.restartbutton.bind('<Leave>',self.restartbuttonout)
        self.gamerestartbutton.bind('<Enter>',self.gamerestartbuttonin)
        self.gamerestartbutton.bind('<Leave>',self.gamerestartbuttonout)
        self.mainwindow.mainloop()
        
    def startframe1(self):
        l=self.player1name.get()
        m=self.player2name.get()
       
        if (l not in ['',' ']) and (m not in ['',' ']):
            self.button1.config(state=NORMAL,bg=self.gamestarted_playpad)
            self.button2.config(state=NORMAL,bg=self.gamestarted_playpad)
            self.button3.config(state=NORMAL,bg=self.gamestarted_playpad)
            self.button4.config(state=NORMAL,bg=self.gamestarted_playpad)
            self.button5.config(state=NORMAL,bg=self.gamestarted_playpad)
            self.button6.config(state=NORMAL,bg=self.gamestarted_playpad)
            self.button7.config(state=NORMAL,bg=self.gamestarted_playpad)
            self.button8.config(state=NORMAL,bg=self.gamestarted_playpad)
            self.button9.config(state=NORMAL,bg=self.gamestarted_playpad)
            self.restartbutton.config(state=NORMAL)
            self.gamerestartbutton.config(state=NORMAL)
            self.textbox.config(state=NORMAL)
            self.historymenu.entryconfig(0,state=NORMAL)
            self.historymenu.entryconfig(1,state=NORMAL)
            self.historymenu.entryconfig(2,state=NORMAL)
            self.gamemenu.entryconfig(1,state=NORMAL)
            self.enterplayer1name.config(state=DISABLED)
            self.enterplayer2name.config(state=DISABLED)
            self.startbutton.config(state=DISABLED)
            self.state='on'
            
            
        else:
            tkMessageBox.showerror(title='Insert name',message='Entering both name is compulsory')

    def play(self,pos):
        if self.position[pos]==' ':
            if self.turn%2==0:
                if pos==1:
                    self.position[pos]='X'
                    self.button1.config(bg=self.x_playpad,text='X',state=DISABLED)
                    self.history.append('1---X')
                    self.returnthebox()
                    self.appendpanel('X inserted at 1 \n -------')
                elif pos==2:
                    self.position[pos]='X'
                    self.button2.config(bg=self.x_playpad,text='X',state=DISABLED)
                    self.history.append('2---X')
                    self.returnthebox()
                    self.appendpanel('X inserted at 2 \n -------')
                elif pos==3:
                    self.position[pos]='X'
                    self.button3.config(bg=self.x_playpad,text='X',state=DISABLED)
                    self.history.append('3---X')
                    self.returnthebox()
                    self.appendpanel('X inserted at 3 \n -------')
                elif pos==4:
                    self.position[pos]='X'
                    self.button4.config(bg=self.x_playpad,text='X',state=DISABLED)
                    self.history.append('4---X')
                    self.returnthebox()
                    self.appendpanel('X inserted at 4 \n -------')
                elif pos==5:
                    self.position[pos]='X'
                    self.button5.config(bg=self.x_playpad,text='X',state=DISABLED)
                    self.history.append('5---X')
                    self.returnthebox()
                    self.appendpanel('X inserted at 5 \n -------')
                elif pos==6:
                    self.position[pos]='X'
                    self.button6.config(bg=self.x_playpad,text='X',state=DISABLED)
                    self.history.append('6---X')
                    self.returnthebox()
                    self.appendpanel('X inserted at 6 \n -------')
                elif pos==7:
                    self.position[pos]='X'
                    self.button7.config(bg=self.x_playpad,text='X',state=DISABLED)
                    self.history.append('7---X')
                    self.returnthebox()
                    self.appendpanel('X inserted at 7 \n -------')
                elif pos==8:
                    self.position[pos]='X'
                    self.button8.config(bg=self.x_playpad,text='X',state=DISABLED)
                    self.history.append('8---X')
                    self.returnthebox()
                    self.appendpanel('X inserted at 8 \n -------')
                elif pos==9:
                    self.position[pos]='X'
                    self.button9.config(bg=self.x_playpad,text='X',state=DISABLED)
                    self.history.append('9---X')
                    self.returnthebox()
                    
                    self.appendpanel('X inserted at 9 \n -------')

            elif self.turn%2!=0:
                if pos==1:
                    self.position[pos]='O'
                    self.button1.config(bg=self.o_playpad,text='O',state=DISABLED)
                    self.history.append('1---O')
                    self.returnthebox()
                    self.appendpanel('O inserted at 1 \n -------')
                elif pos==2:
                    self.position[pos]='O'
                    self.button2.config(bg=self.o_playpad,text='O',state=DISABLED)
                    self.history.append('2---O')
                    self.returnthebox()
                    self.appendpanel('O inserted at 2 \n -------')
                elif pos==3:
                    self.position[pos]='O'
                    self.button3.config(bg=self.o_playpad,text='O',state=DISABLED)
                    self.history.append('3---O')
                    self.returnthebox()
                    self.appendpanel('O inserted at 3 \n -------')
                elif pos==4:
                    self.position[pos]='O'
                    self.button4.config(bg=self.o_playpad,text='O',state=DISABLED)
                    self.history.append('4---O')
                    self.returnthebox()
                    self.appendpanel('O inserted at 4 \n -------')
                elif pos==5:
                    self.position[pos]='O'
                    self.button5.config(bg=self.o_playpad,text='O',state=DISABLED)
                    self.history.append('5---O')
                    self.returnthebox()
                    self.appendpanel('O inserted at 5 \n -------')
                elif pos==6:
                    self.position[pos]='O'
                    self.button6.config(bg=self.o_playpad,text='O',state=DISABLED)
                    self.history.append('6---O')
                    self.returnthebox()
                    self.appendpanel('O inserted at 6 \n -------')
                elif pos==7:
                    self.position[pos]='O'
                    self.button7.config(bg=self.o_playpad,text='O',state=DISABLED)
                    self.history.append('7---O')
                    self.returnthebox()
                    self.appendpanel('O inserted at 7 \n -------')
                elif pos==8:
                    self.position[pos]='O'
                    self.button8.config(bg=self.o_playpad,text='O',state=DISABLED)
                    self.history.append('8---O')
                    self.returnthebox()
                    self.appendpanel('O inserted at 8 \n -------')
                elif pos==9:
                    self.position[pos]='O'
                    self.button9.config(bg=self.o_playpad,text='O',state=DISABLED)
                    self.history.append('9---O')
                    self.returnthebox()
                    self.appendpanel('O inserted at 9 \n -------')
            self.turn+=1
            self.gamecheck()
    def restart(self):
        self.history=[]
        self.position={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
        self.turn=0
        self.button1.config(bg=self.gamestarted_playpad,text=' ',state=NORMAL)
        self.button2.config(bg=self.gamestarted_playpad,text=' ',state=NORMAL)
        self.button3.config(bg=self.gamestarted_playpad,text=' ',state=NORMAL)
        self.button4.config(bg=self.gamestarted_playpad,text=' ',state=NORMAL)
        self.button5.config(bg=self.gamestarted_playpad,text=' ',state=NORMAL)
        self.button6.config(bg=self.gamestarted_playpad,text=' ',state=NORMAL)
        self.button7.config(bg=self.gamestarted_playpad,text=' ',state=NORMAL)
        self.button8.config(bg=self.gamestarted_playpad,text=' ',state=NORMAL)
        self.button9.config(bg=self.gamestarted_playpad,text=' ',state=NORMAL)
        self.appendpanel('------\nGame restarted\n--------')
    def gamerestart(self):
        self.history=[]
        self.position={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
        self.panelhistory=''
        self.turn=0
        self.player1score=0
        self.player2score=0
        self.enterplayer1name.config(state=NORMAL)
        self.enterplayer2name.config(state=NORMAL)
        self.startbutton.config(state=NORMAL)
        self.button1.config(bg=self.initial_playpad,state=DISABLED,text=' ')
        self.button2.config(bg=self.initial_playpad,state=DISABLED,text=' ')
        self.button3.config(bg=self.initial_playpad,state=DISABLED,text=' ')
        self.button4.config(bg=self.initial_playpad,state=DISABLED,text=' ')
        self.button5.config(bg=self.initial_playpad,state=DISABLED,text=' ')
        self.button5.config(bg=self.initial_playpad,state=DISABLED,text=' ')
        self.button6.config(bg=self.initial_playpad,state=DISABLED,text=' ')
        self.button7.config(bg=self.initial_playpad,state=DISABLED,text=' ')
        self.button8.config(bg=self.initial_playpad,state=DISABLED,text=' ')
        self.button9.config(bg=self.initial_playpad,state=DISABLED,text=' ')
        self.historymenu.entryconfig(0,state=DISABLED)
        self.historymenu.entryconfig(1,state=DISABLED)
        self.historymenu.entryconfig(2,state=DISABLED)
        self.gamemenu.entryconfig(1,state=DISABLED)
        self.restartbutton.config(state=DISABLED)
        self.gamerestartbutton.config(state=DISABLED)
        self.textbox.config(state=DISABLED)
        self.state='off'
        self.appendpanel('--------\nWhole Game Restarted\n----------')
    def gamecheck(self):
        if self.position[1]==self.position[2]==self.position[3]=='X':
            self.button1.config(bg=self.won_playpad,state=DISABLED)
            self.button2.config(bg=self.won_playpad,state=DISABLED)
            self.button3.config(bg=self.won_playpad,state=DISABLED)
            self.button4.config(state=DISABLED)
            self.button5.config(state=DISABLED)
            self.button6.config(state=DISABLED)
            self.button7.config(state=DISABLED)
            self.button8.config(state=DISABLED)
            self.button9.config(state=DISABLED)
            self.appendpanel('------\nX won \n-------')
            self.player1score+=10
        elif self.position[4]==self.position[5]==self.position[6]=='X':
            self.button4.config(bg=self.won_playpad,state=DISABLED)
            self.button5.config(bg=self.won_playpad,state=DISABLED)
            self.button6.config(bg=self.won_playpad,state=DISABLED)
            self.button1.config(state=DISABLED)
            self.button2.config(state=DISABLED)
            self.button3.config(state=DISABLED)
            self.button7.config(state=DISABLED)
            self.button8.config(state=DISABLED)
            self.button9.config(state=DISABLED)
            self.appendpanel('------\nX won \n-------')
            self.player1score+=10
        elif self.position[7]==self.position[8]==self.position[9]=='X':
            self.button7.config(bg=self.won_playpad,state=DISABLED)
            self.button8.config(bg=self.won_playpad,state=DISABLED)
            self.button9.config(bg=self.won_playpad,state=DISABLED)
            self.button1.config(state=DISABLED)
            self.button2.config(state=DISABLED)
            self.button3.config(state=DISABLED)
            self.button4.config(state=DISABLED)
            self.button5.config(state=DISABLED)
            self.button6.config(state=DISABLED)
            self.appendpanel('------\nX won \n-------')
            self.player1score+=10
        elif self.position[1]==self.position[4]==self.position[7]=='X':
            self.button7.config(bg=self.won_playpad,state=DISABLED)
            self.button1.config(bg=self.won_playpad,state=DISABLED)
            self.button4.config(bg=self.won_playpad,state=DISABLED)
            self.button8.config(state=DISABLED)
            self.button2.config(state=DISABLED)
            self.button3.config(state=DISABLED)
            self.button9.config(state=DISABLED)
            self.button5.config(state=DISABLED)
            self.button6.config(state=DISABLED)
            self.appendpanel('------\nX won \n-------')
            self.player1score+=10
        elif self.position[2]==self.position[5]==self.position[8]=='X':
            self.button2.config(bg=self.won_playpad,state=DISABLED)
            self.button5.config(bg=self.won_playpad,state=DISABLED)
            self.button8.config(bg=self.won_playpad,state=DISABLED)
            self.button1.config(state=DISABLED)
            self.button7.config(state=DISABLED)
            self.button3.config(state=DISABLED)
            self.button4.config(state=DISABLED)
            self.button9.config(state=DISABLED)
            self.button6.config(state=DISABLED)
            self.appendpanel('------\nX won \n-------')
            self.player1score+=10
        elif self.position[3]==self.position[6]==self.position[9]=='X':
            self.button3.config(bg=self.won_playpad,state=DISABLED)
            self.button6.config(bg=self.won_playpad,state=DISABLED)
            self.button9.config(bg=self.won_playpad,state=DISABLED)
            self.button1.config(state=DISABLED)
            self.button2.config(state=DISABLED)
            self.button7.config(state=DISABLED)
            self.button4.config(state=DISABLED)
            self.button5.config(state=DISABLED)
            self.button8.config(state=DISABLED)
            self.appendpanel('------\nX won \n-------')
            self.player1score+=10
        elif self.position[1]==self.position[5]==self.position[9]=='X':
            self.button1.config(bg=self.won_playpad,state=DISABLED)
            self.button5.config(bg=self.won_playpad,state=DISABLED)
            self.button9.config(bg=self.won_playpad,state=DISABLED)
            self.button6.config(state=DISABLED)
            self.button2.config(state=DISABLED)
            self.button7.config(state=DISABLED)
            self.button4.config(state=DISABLED)
            self.button3.config(state=DISABLED)
            self.button8.config(state=DISABLED)
            self.appendpanel('------\nX won \n-------')
            self.player1score+=10
        elif self.position[3]==self.position[5]==self.position[7]=='X':
            self.button3.config(bg=self.won_playpad,state=DISABLED)
            self.button5.config(bg=self.won_playpad,state=DISABLED)
            self.button7.config(bg=self.won_playpad,state=DISABLED)
            self.button1.config(state=DISABLED)
            self.button2.config(state=DISABLED)
            self.button9.config(state=DISABLED)
            self.button4.config(state=DISABLED)
            self.button6.config(state=DISABLED)
            self.button8.config(state=DISABLED)
            self.appendpanel('------\nX won \n-------')
            self.player1score+=10


        elif self.position[1]==self.position[2]==self.position[3]=='O':
            self.button1.config(bg=self.won_playpad,state=DISABLED)
            self.button2.config(bg=self.won_playpad,state=DISABLED)
            self.button3.config(bg=self.won_playpad,state=DISABLED)
            self.button4.config(state=DISABLED)
            self.button5.config(state=DISABLED)
            self.button6.config(state=DISABLED)
            self.button7.config(state=DISABLED)
            self.button8.config(state=DISABLED)
            self.button9.config(state=DISABLED)
            self.appendpanel('------\nO won \n-------')
            self.player2score+=10
        elif self.position[4]==self.position[5]==self.position[6]=='O':
            self.button4.config(bg=self.won_playpad,state=DISABLED)
            self.button5.config(bg=self.won_playpad,state=DISABLED)
            self.button6.config(bg=self.won_playpad,state=DISABLED)
            self.button1.config(state=DISABLED)
            self.button2.config(state=DISABLED)
            self.button3.config(state=DISABLED)
            self.button7.config(state=DISABLED)
            self.button8.config(state=DISABLED)
            self.button9.config(state=DISABLED)
            self.appendpanel('------\nO won \n-------')
            self.player2score+=10
        elif self.position[7]==self.position[8]==self.position[9]=='O':
            self.button7.config(bg=self.won_playpad,state=DISABLED)
            self.button8.config(bg=self.won_playpad,state=DISABLED)
            self.button9.config(bg=self.won_playpad,state=DISABLED)
            self.button1.config(state=DISABLED)
            self.button2.config(state=DISABLED)
            self.button3.config(state=DISABLED)
            self.button4.config(state=DISABLED)
            self.button5.config(state=DISABLED)
            self.button6.config(state=DISABLED)
            self.appendpanel('------\nO won \n-------')
            self.player2score+=10
        elif self.position[1]==self.position[4]==self.position[7]=='O':
            self.button7.config(bg=self.won_playpad,state=DISABLED)
            self.button1.config(bg=self.won_playpad,state=DISABLED)
            self.button4.config(bg=self.won_playpad,state=DISABLED)
            self.button8.config(state=DISABLED)
            self.button2.config(state=DISABLED)
            self.button3.config(state=DISABLED)
            self.button9.config(state=DISABLED)
            self.button5.config(state=DISABLED)
            self.button6.config(state=DISABLED)
            self.appendpanel('------\nO won \n-------')
            self.player2score+=10
        elif self.position[2]==self.position[5]==self.position[8]=='O':
            self.button2.config(bg=self.won_playpad,state=DISABLED)
            self.button5.config(bg=self.won_playpad,state=DISABLED)
            self.button8.config(bg=self.won_playpad,state=DISABLED)
            self.button1.config(state=DISABLED)
            self.button7.config(state=DISABLED)
            self.button3.config(state=DISABLED)
            self.button4.config(state=DISABLED)
            self.button9.config(state=DISABLED)
            self.button6.config(state=DISABLED)
            self.appendpanel('------\nO won \n-------')
            self.player2score+=10
        elif self.position[3]==self.position[6]==self.position[9]=='O':
            self.button3.config(bg=self.won_playpad,state=DISABLED)
            self.button6.config(bg=self.won_playpad,state=DISABLED)
            self.button9.config(bg=self.won_playpad,state=DISABLED)
            self.button1.config(state=DISABLED)
            self.button2.config(state=DISABLED)
            self.button7.config(state=DISABLED)
            self.button4.config(state=DISABLED)
            self.button5.config(state=DISABLED)
            self.button8.config(state=DISABLED)
            self.appendpanel('------\nO won \n-------')
            self.player2score+=10
        elif self.position[1]==self.position[5]==self.position[9]=='O':
            self.button1.config(bg=self.won_playpad,state=DISABLED)
            self.button5.config(bg=self.won_playpad,state=DISABLED)
            self.button9.config(bg=self.won_playpad,state=DISABLED)
            self.button6.config(state=DISABLED)
            self.button2.config(state=DISABLED)
            self.button7.config(state=DISABLED)
            self.button4.config(state=DISABLED)
            self.button3.config(state=DISABLED)
            self.button8.config(state=DISABLED)
            self.appendpanel('------\nO won \n-------')
            self.player2score+=10
        elif self.position[3]==self.position[5]==self.position[7]=='O':
            self.button3.config(bg=self.won_playpad,state=DISABLED)
            self.button5.config(bg=self.won_playpad,state=DISABLED)
            self.button7.config(bg=self.won_playpad,state=DISABLED)
            self.button1.config(state=DISABLED)
            self.button2.config(state=DISABLED)
            self.button9.config(state=DISABLED)
            self.button4.config(state=DISABLED)
            self.button6.config(state=DISABLED)
            self.button8.config(state=DISABLED)
            self.appendpanel('------\nO won \n-------')
            self.player2score+=10
        self.comparescore()
    def greator(self,ok=True):
        if ok:
            if self.player1score>self.player2score:
                return self.player1score
            elif self.player2score>self.player1score:
                return self.player2score
            else:
                return None
        else:
            if self.player1score>self.player2score:
                return [self.player1name.get(),self.player1score,self.player2name.get()]
            elif self.player2score>self.player1score:
                return [self.player2name.get(),self.player2score,self.player2name.get()]
                
    def comparescore(self):
        fil=open('highscore.dtt','rb+')
        dd=pickle.load(fil)
        fil.close()
        if self.greator()!=None:
            if self.greator()>dd[1]:
                del dd
                dd=self. greator(False)
                fil=open('highscore.dtt','wb+')
                pickle.dump(dd,fil)
                fil.close()
    def showhistory(self):
        s=''
        for a in self.history:
            s+=a+'\n'
        tkMessageBox.showinfo('History',s)
    def showpanel(self):
        self.tp=Toplevel(self.mainwindow,bg=self.background,width=100,height=210)
        self.scrollbar1=Scrollbar(self.tp)
        self.scrollbar1.pack(side=RIGHT,fill=Y)
        self.textbox1=Text(self.tp,yscrollcommand=self.scrollbar1.set,width=19,height=10)
        self.textbox1.insert('1.0',self.panelhistory)
        self.textbox1.pack(fill=BOTH)
        self.scrollbar1.config(command=self.textbox1.yview)
    def showhighscore(self):
        fil=open('highscore.dtt','rb+')
        dd=pickle.load(fil)
        fil.close()
        s='Highscore is by:'+dd[0]+' and his score is '+str(dd[1])+'\nMatch::'+dd[0]+'--VS--'+dd[2]
        tkMessageBox.showinfo('HIGHSCORE',s)
    def printinfo(self):
        s='HELLO GUYS\nThis is the simple game of cross and zero. you already know how to play that game but let me explain\nthe working of this game\nFirst of all you will you have to enter both the players name or game will not start\nAfter you enter the you can start the game, while you are playing your \nhistory is being recorded which you can see using the history menu\n'
        s+='if game draws then nothing will happen and you can restart the \ngame with same players name or restart the whole sessionbg=self.won_playpad of the playing. If anyone wins followinf things will happen, if the\ntotal score of thet player if greator with the present highscore the your name will replace them else not.\nYour highscore will be the total or sum of the all the score you \nrecived. you will recive 10 point if you win or else not if game is draw\n'
        s+='player 1 is X and player 2 is O\nTHANK YOU'
        tkMessageBox.showinfo('info',s)
    def showcredits(self):
        s='Game made by- jimmy kumar ahalpara and ayush singh\nGame based on cross and zero\nMade using python 2.7 and Tkinter GUI'
        tkMessageBox.showinfo('CREDITS',s)

    def startbuttonin(self,event):
        if self.startbutton['state']<>DISABLED:
            self.startbutton.config(bg=self.normal_clickedbutton)
    def startbuttonout(self,event):
        self.startbutton.config(bg=self.normal_button)
    def restartbuttonin(self,event):
        if self.restartbutton['state']<>DISABLED:
            self.restartbutton.config(bg=self.normal_clickedbutton)
    def restartbuttonout(self,event):
        self.restartbutton.config(bg=self.normal_button)
    def gamerestartbuttonin(self,event):
        if self.gamerestartbutton['state']<>DISABLED:
            self.gamerestartbutton.config(bg=self.normal_clickedbutton)
    def gamerestartbuttonout(self,event):
        self.gamerestartbutton.config(bg=self.normal_button)
    def choosecolor(self):
        self.colorchooser=Toplevel(self.mainwindow,bg=self.background,height=310,width=230)
        Label(self.colorchooser,text='Buttons:').place(x=10,y=10)
        Label(self.colorchooser,text='Buttons under cursor:').place(x=10,y=40)
        Label(self.colorchooser,text='Initial game pad:').place(x=10,y=70)
        Label(self.colorchooser,text='Game started:').place(x=10,y=100)
        Label(self.colorchooser,text='Game pad when x clicked:').place(x=10,y=130)
        Label(self.colorchooser,text='Game pad when o clicked:').place(x=10,y=160)
        Label(self.colorchooser,text='When anyone won:').place(x=10,y=190)
        Label(self.colorchooser,text='Background:').place(x=10,y=220)
        
        self.b1=Button(self.colorchooser,bg=self.normal_button,text='Change',command=lambda:self.changecolor(1))
        self.b1.place(x=170,y=10)
        self.b2=Button(self.colorchooser,bg=self.normal_clickedbutton,text='Change',command=lambda:self.changecolor(2))
        self.b2.place(x=170,y=40)
        self.b3=Button(self.colorchooser,bg=self.initial_playpad,text='Change',command=lambda:self.changecolor(3))
        self.b3.place(x=170,y=70)
        self.b4=Button(self.colorchooser,bg=self.gamestarted_playpad,text='Change',command=lambda:self.changecolor(4))
        self.b4.place(x=170,y=100)
        self.b5=Button(self.colorchooser,bg=self.x_playpad,text='Change',command=lambda:self.changecolor(5))
        self.b5.place(x=170,y=130)
        self.b6=Button(self.colorchooser,bg=self.o_playpad,text='Change',command=lambda:self.changecolor(6))
        self.b6.place(x=170,y=160)
        self.b7=Button(self.colorchooser,bg=self.won_playpad,text='Change',command=lambda:self.changecolor(7))
        self.b7.place(x=170,y=190)
        self.b8=Button(self.colorchooser,bg=self.background,text='Change',command=lambda:self.changecolor(8))
        self.b8.place(x=170,y=220)
        Button(self.colorchooser,bg=self.normal_button,text='OK',command=self.ok_function).place(x=20,y=270)
        Button(self.colorchooser,bg=self.normal_button,text='Apply',command=self.startchange).place(x=70,y=270)
        Button(self.colorchooser,bg=self.normal_button,text='Reset default',command=self.resetdefault).place(x=130,y=270)
    def changecolor(self,num):
        if num==1:
            self.normal_button=tkColorChooser.askcolor(parent=self.colorchooser)[1]
            self.b1.config(bg=self.normal_button)
        elif num==2:
            self.normal_clickedbutton=tkColorChooser.askcolor(parent=self.colorchooser)[1]
            self.b2.config(bg=self.normal_clickedbutton)
        elif num==3:
            self.initial_playpad=tkColorChooser.askcolor(parent=self.colorchooser)[1]
            self.b3.config(bg=self.initial_playpad)
        elif num==4:
            self.gamestarted_playpad=tkColorChooser.askcolor(parent=self.colorchooser)[1]
            self.b4.config(bg=self.gamestarted_playpad)
        elif num==5:
            self.x_playpad=tkColorChooser.askcolor(parent=self.colorchooser)[1]
            self.b5.config(bg=self.x_playpad)
        elif num==6:
            self.o_playpad=tkColorChooser.askcolor(parent=self.colorchooser)[1]
            self.b6.config(bg=self.o_playpad)
        elif num==7:
            self.won_playpad=tkColorChooser.askcolor(parent=self.colorchooser)[1]
            self.b7.config(bg=self.won_playpad)
        elif num==8:
            self.background=tkColorChooser.askcolor(parent=self.colorchooser)[1]
            self.b8.config(bg=self.background)
    def startchange(self):
        self.startbutton.config(bg=self.normal_button)
        self.gamerestartbutton.config(bg=self.normal_button)
        self.restartbutton.config(bg=self.normal_button)
        
        self.button1.config(bg=self.initial_playpad)
        self.button2.config(bg=self.initial_playpad)
        self.button3.config(bg=self.initial_playpad)
        self.button4.config(bg=self.initial_playpad)
        self.button5.config(bg=self.initial_playpad)
        self.button6.config(bg=self.initial_playpad)
        self.button7.config(bg=self.initial_playpad)
        self.button8.config(bg=self.initial_playpad)
        self.button9.config(bg=self.initial_playpad)
        self.frame1.config(bg=self.background)
        self.frame2.config(bg=self.background)
    def ok_function(self):
        self.colorchooser.destroy()
        self.startchange()
    def resetdefault(self):
        self.normal_button='SystembuttonFace'
        self.normal_clickedbutton='grey'
        self.initial_playpad='pink'
        self.gamestarted_playpad='green'
        self.x_playpad='yellow'
        self.o_playpad='cyan'
        self.won_playpad='red'
        self.background='SystemButtonFace'
        self.startchange()
        
Maingamemodule().createwindow()
