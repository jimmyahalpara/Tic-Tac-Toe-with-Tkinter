# Tic-Tac-Toe-with-Tkinter
Tic tac toe with fantastic gui made with **Tkinter**. Really good example for learning **Tkinter** with **Python**. If you can't figureout anything you can contact *jimmyahalpara123@gmail.com*



# Tic Tac Toe

Hello, Guys in this notebook I'll be explaining you step by step the makeing of my tic-tac-toe game which is made using python and tkinter. So Lets get started by importing some important modules.
I recommend that you first play the game, know its all features and then continue reading this notebook. 
Some initial knowledge of tkinter is required!!!


Hello, Guys in this notebook I'll be explaining you step by step the makeing of my tic-tac-toe game which is made using python and tkinter. So Lets get started by importing some important modules.
I recommend that you first play the game, know its all features and then continue reading this notebook. 
Some initial knowledge of tkinter is required!!!


```python
import pickle 
from Tkiniter import *
import tkMessageBox
import tkColorChooser
```

In the above code we have imported many modules. let's see it one by one what it does:-
1. pickle - this module is used to saved serialized player highscore data
2. Tkinter - this module will be use to create GUI for the game.
3. tkMessageBox - this is the helper module which will help in making message box for warning, or errors.
3. tkColorChooser - this is a module that will help you to choose color.

Now Let's see Class named Maingamemodule which will help for running the game and creating GUI


```python
class Maingamemodule:
    
    #this method will be executed when we initializes or we can say create the object for the class
    #this method will initialize all the required variable and other data
    def __init__(self):
        #this codeblock below will check if fill named "highscore.dtt" is present or not, if not then upper "try" codeblock will be terminated and "except" codeblock will be executed which will create highscore.dtt file.
        #this two codeblock generally will check if previous and data is available for the high score, if not then it creates new empty data
        try:
            s=open('highscore.dtt','rb+')
            s.close()
        except:
            s=open('highscore.dtt','wb+')
            pickle.dump(['',0,''],s) #in that file data is saved in form of list where at index 0, index 2 will have player 1 name, player name 2 respectively which will be string and in index 1 there will be the highscore in form of integer, which will be of player with player name 1
            s.close()
        self.history=[] #this will store the history of all the moves made by the players
        self.position={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '} #stores the tic-tac-toe position
        self.panelhistory='' #right side panel history will be saved here
        self.turn=0 #will determine whose turn is this
        self.player1score=0 #player 1 score
        self.player2score=0 #player 2 score
        self.state='off' #is game can be played or paused can be determined by this, is this is off some playing widgets will be disabled
        self.normal_button='SystembuttonFace' #normal button color
        self.normal_clickedbutton='grey' #normal clicked butten color
        self.initial_playpad='pink' #initial playpad color
        self.gamestarted_playpad='green' #when game starts, pad color will be converted to this
        self.x_playpad='yellow' #is x clicked, that button will turn to this color
        self.o_playpad='cyan' #if o clicked, that button will turn to this color
        self.won_playpad='red' #if anyone won, those group of three buttons will turn into this color
        self.background='SystemButtonFace' #background color

    def exxit(self): #game will close
        self.mainwindow.destroy()
        exit()

    def appendpanel(self,s): #used if we want to insert data in pane or box on right side which shows gamme history
        self.panelhistory+='\n'+s #new string will be added to panelhistory
        self.textbox.insert('1.0','\n'+s) #text box on right will be updated
        
    def returnthebox(self): #this method will return a string, if printed will form box containing the tic tac toe at that instance, and can be used when we are goint to update the textbox
        st='+---+---+---+\n| '+self.position[1]+' | '+self.position[2]+' | '+self.position[3]+' |\n+---+---+---+\n| '+self.position[4]+' | '+self.position[5]+' | '+self.position[6]+' |\n+---+---+---+\n| '+self.position[7]+' | '+self.position[8]+' | '+self.position[9]+' |\n+---+---+---+\n'
        self.appendpanel(st)
    
    def createwindow(self): #after __init__ method this method will be executed, this will create the main frame, and insert all its widgets
        self.mainwindow=Tk(screenName='Tic-Tac-Toe',baseName='Tic_tac_toe',className='Maingame_menu') #create main window object and save it into a variable
        self.menubar=Menu(self.mainwindow) #creates menubar widget object and save its instance
        self.gamemenu=Menu(self.menubar,tearoff=0) #creates menu widget object and save its instance, this will be gamemenu
        self.gamemenu.add_command(label='New game',command=self.gamerestart) #add commands in gamemenu using its instance and add their respective function which will be executed when we cluch that option or command
        self.gamemenu.add_command(label='Restart Game',command=self.restart) #adding commands
        self.gamemenu.add_separator() #adding seperator in that menu, that is draw slight line
        self.gamemenu.add_command(label='exit',command=self.exxit) #adding command for exit
        self.menubar.add_cascade(label='Game',menu=self.gamemenu) #all the data of gamemenu should be added to menubar
        self.historymenu=Menu(self.menubar,tearoff=0) #creating historymenu
        self.historymenu.add_command(label='Show History',command=self.showhistory) #adding commands
        self.historymenu.add_command(label='Show Highscore',command=self.showhighscore) #adding commands
        self.historymenu.add_command(label='Show Panel History',command=self.showpanel) #adding commands
        self.historymenu.entryconfig(0,state=DISABLED) #initial state of some command should be disabled
        self.historymenu.entryconfig(1,state=DISABLED) #same as above
        self.historymenu.entryconfig(2,state=DISABLED) #same as above
        self.gamemenu.entryconfig(1,state=DISABLED) #same as above
        self.menubar.add_cascade(label='History',menu=self.historymenu) #adding history menu to menubar
        self.helpmenu=Menu(self.menubar,tearoff=0) 
        self.helpmenu.add_command(label='Info',command=self.printinfo)
        self.helpmenu.add_command(label='Credits',command=self.showcredits)
        self.menubar.add_cascade(label='Help',menu=self.helpmenu)
        self.colormenu=Menu(self.menubar,tearoff=0)
        self.colormenu.add_command(label='Choosecolor',command=self.choosecolor)
        self.menubar.add_cascade(label='Colours',menu=self.colormenu)
        self.mainwindow.config(menu=self.menubar) #adding the menubar into mainwindow
        
        #creating two frames left containing game pad and right containing history test box
        self.frame1=Frame(self.mainwindow,bg=self.background,width=500,height=210) #creating frame widget object and saving its instance
        self.frame1.pack(side=LEFT) #packing the previous widget
        self.frame2=Frame(self.mainwindow,bg=self.background,width=100,height=210) #right frame
        self.frame2.place(x=320,y=10) #place method same as pack but uses coordinates
        
        #add all main widgets for taking player information
        Label(self.frame1,text='Player 1 name:').place(x=6,y=5) #label for planyer name 1
        self.player1name=StringVar() #Special Variable for storing player name 1
        self.enterplayer1name=Entry(self.frame1,textvariable=self.player1name,width=10) #creating text-box
        self.enterplayer1name.place(x=90,y=5) #placing the widget 
        Label(self.frame1,text='Player 2 name:').place(x=150,y=5) #label for player name 2
        self.player2name=StringVar() #special variable for storing player name 2
        self.enterplayer2name=Entry(self.frame1,textvariable=self.player2name,width=10) #test box for player number two
        self.enterplayer2name.place(x=235,y=5) #placing the above widget
        self.startbutton=Button(self.frame1,text='Start',command=self.startframe1) #button widget for starting the game
        self.startbutton.place(x=50,y=30) #placing that button
        
        #now creating the gampad with 9 buttonsand placing them 
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

        self.restartbutton=Button(self.frame1,text='Restart',state=DISABLED,command=self.restart) #restart button will restart the game while keeping the playername same
        self.restartbutton.place(x=170,y=100) #placing that button
        self.gamerestartbutton=Button(self.frame1,text='Restart Game',state=DISABLED,command=self.gamerestart) #whole game will restart with this button while keeping the player name same
        self.gamerestartbutton.place(x=170,y=140) #placing above button
        
        self.scrollbar=Scrollbar(self.frame2) #creating scrollbar widget and saving its instance, scroll bar will be used for the text box
        self.scrollbar.pack(side=RIGHT,fill=Y) #packing that scrollbar
        self.textbox=Text(self.frame2,yscrollcommand=self.scrollbar.set,width=19,height=10,state=DISABLED) #creating the textbox widget which will show history
        self.textbox.pack(fill=BOTH) #packing that widget
        self.scrollbar.config(command=self.textbox.yview) #connecting the scroll bar with text box

        #these are some event handlera for our button
        #here method connected with the respective button will be executed whenever the avent as specified will occure
        #here "<Enter>" event means whenevr our cursor will come above that button but not click it
        #"<Leave>" event event means whenever our cursor will come leave that button
        #all the bello code lines will make our button change color as specified whenwver under the cursor and will turn into normal whenever cursor goes away
        self.startbutton.bind('<Enter>',self.startbuttonin) 
        self.startbutton.bind('<Leave>',self.startbuttonout)
        self.restartbutton.bind('<Enter>',self.restartbuttonin)
        self.restartbutton.bind('<Leave>',self.restartbuttonout)
        self.gamerestartbutton.bind('<Enter>',self.gamerestartbuttonin)
        self.gamerestartbutton.bind('<Leave>',self.gamerestartbuttonout)
        self.mainwindow.mainloop() #will start the mainloop which will start our GUI
        
    def startframe1(self): #this method will be executed when we click start button after entering the player names
        l=self.player1name.get() #this will save player name in form of string
        m=self.player2name.get() # same as above
       
        if (l not in ['',' ']) and (m not in ['',' ']):  #all the disabled widget will be turned into abled if and if only player enters valid playername
            self.button1.config(state=NORMAL,bg=self.gamestarted_playpad) #changing the gamebad or playpad color
            self.button2.config(state=NORMAL,bg=self.gamestarted_playpad)
            self.button3.config(state=NORMAL,bg=self.gamestarted_playpad)
            self.button4.config(state=NORMAL,bg=self.gamestarted_playpad)
            self.button5.config(state=NORMAL,bg=self.gamestarted_playpad)
            self.button6.config(state=NORMAL,bg=self.gamestarted_playpad)
            self.button7.config(state=NORMAL,bg=self.gamestarted_playpad)
            self.button8.config(state=NORMAL,bg=self.gamestarted_playpad)
            self.button9.config(state=NORMAL,bg=self.gamestarted_playpad)
            self.restartbutton.config(state=NORMAL) #changing the state of the buttons
            self.gamerestartbutton.config(state=NORMAL)
            self.textbox.config(state=NORMAL)
            self.historymenu.entryconfig(0,state=NORMAL)
            self.historymenu.entryconfig(1,state=NORMAL)
            self.historymenu.entryconfig(2,state=NORMAL)
            self.gamemenu.entryconfig(1,state=NORMAL)
            self.enterplayer1name.config(state=DISABLED) #disabling the widgets which we used to enter the name
            self.enterplayer2name.config(state=DISABLED) #
            self.startbutton.config(state=DISABLED) #
            self.state='on' #changing the state of the game
            
            
        else:
            tkMessageBox.showerror(title='Insert name',message='Entering both name is compulsory') #if name not enterd or entered blank space then error message will be shown 

    def play(self,pos): #this method will be executed if we click anyne of the nine play button, this method will take a number-> pos as the position of that button
        if self.position[pos]==' ': #if that positio is blank then only the change will take place
            if self.turn%2==0: #checking the turn, self.turn variable will increase with every move, if the number is even then player 1 or "X" will play or player 2 that is "O". So the alternate turns will take place
                if pos==1:  #checking the position
                    self.position[pos]='X' #updating the main storing dictionary
                    self.button1.config(bg=self.x_playpad,text='X',state=DISABLED) #updating that button test to respective player annd changing the button state to DISABLED so that no one can click it again
                    self.history.append('1---X') #updating the history
                    self.returnthebox() #updating the right textbox
                    self.appendpanel('X inserted at 1 \n -------') #updating the right text box with move discription
                #after all all the if statement will do same job as above but just changing the position of the changes
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

            elif self.turn%2!=0: #all the chenges will take place for player 2 or "O"
                if pos==1: #same as above all statements just, button text will change to O
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
            
    def restart(self): #will restart only the current game while keeping the highscore and name same
        self.history=[] #but history will be deleted
        self.position={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '} #restarting the game dictionary
        self.turn=0 #initial turn of player 1
        self.button1.config(bg=self.gamestarted_playpad,text=' ',state=NORMAL) #changing the button color to initial 
        self.button2.config(bg=self.gamestarted_playpad,text=' ',state=NORMAL) #
        self.button3.config(bg=self.gamestarted_playpad,text=' ',state=NORMAL) #
        self.button4.config(bg=self.gamestarted_playpad,text=' ',state=NORMAL) #
        self.button5.config(bg=self.gamestarted_playpad,text=' ',state=NORMAL) #
        self.button6.config(bg=self.gamestarted_playpad,text=' ',state=NORMAL) #
        self.button7.config(bg=self.gamestarted_playpad,text=' ',state=NORMAL) #
        self.button8.config(bg=self.gamestarted_playpad,text=' ',state=NORMAL) #
        self.button9.config(bg=self.gamestarted_playpad,text=' ',state=NORMAL) #
        self.appendpanel('------\nGame restarted\n--------') # appending the right side text box but not clearing whole text
        
    def gamerestart(self): #will restart whole new game with new game and restart the scoreboard
        self.history=[] #restarting the history
        self.position={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '} #restarting the saving dictionary
        self.panelhistory='' #all the right side history will be cleared
        self.turn=0 #initial player 1 turn
        self.player1score=0 #restarting the player score
        self.player2score=0 #
        self.enterplayer1name.config(state=NORMAL) #now the game state will become off so all the playing related widget will be disabled
        self.enterplayer2name.config(state=NORMAL) #and ableing the widgets which will be used to take the player names
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
        self.appendpanel('--------\nWhole Game Restarted\n----------') #restart the whole right side text box

    def gamecheck(self): #this method will be called after every player move and will chek if any player woon or not
        if self.position[1]==self.position[2]==self.position[3]=='X': #if any three boxes are same then 
            self.button1.config(bg=self.won_playpad,state=DISABLED) #all buttons will be disabled with winning buttons of different color
            self.button2.config(bg=self.won_playpad,state=DISABLED)
            self.button3.config(bg=self.won_playpad,state=DISABLED)
            self.button4.config(state=DISABLED)
            self.button5.config(state=DISABLED)
            self.button6.config(state=DISABLED)
            self.button7.config(state=DISABLED)
            self.button8.config(state=DISABLED)
            self.button9.config(state=DISABLED)
            self.appendpanel('------\nX won \n-------') #appending the right text box with the details
            self.player1score+=10 #add the score on scoreboard
        #some of the following codblock will do same job job by just changing the boxes
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


        elif self.position[1]==self.position[2]==self.position[3]=='O': #if player 2 won
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
        
    def greator(self,ok=True): # this method will be used to check the largest score
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
                
    def comparescore(self): # this method will check if current largest score is all time highscore 
        fil=open('highscore.dtt','rb+') #opening the file
        dd=pickle.load(fil)
        fil.close()
        if self.greator()!=None:
            if self.greator()>dd[1]:
                del dd
                dd=self. greator(False)
                fil=open('highscore.dtt','wb+')
                pickle.dump(dd,fil) #will add highscore it it is largest
                fil.close()
                
    def showhistory(self): # will show the current game highscore in a textbox dialog
        s=''
        for a in self.history:
            s+=a+'\n'
        tkMessageBox.showinfo('History',s)
        
    def showpanel(self): #will show right side text box history in a dialogue box
        self.tp=Toplevel(self.mainwindow,bg=self.background,width=100,height=210)
        self.scrollbar1=Scrollbar(self.tp)
        self.scrollbar1.pack(side=RIGHT,fill=Y)
        self.textbox1=Text(self.tp,yscrollcommand=self.scrollbar1.set,width=19,height=10)
        self.textbox1.insert('1.0',self.panelhistory)
        self.textbox1.pack(fill=BOTH)
        self.scrollbar1.config(command=self.textbox1.yview)
        
    def showhighscore(self): #hill show highscore from the file
        fil=open('highscore.dtt','rb+')
        dd=pickle.load(fil)
        fil.close()
        s='Highscore is by:'+dd[0]+' and his score is '+str(dd[1])+'\nMatch::'+dd[0]+'--VS--'+dd[2]
        tkMessageBox.showinfo('HIGHSCORE',s) #in a message box
        
    def printinfo(self): #will be used to show the help or info of how to play
        s='HELLO GUYS\nThis is the simple game of cross and zero. you already know how to play that game but let me explain\nthe working of this game\nFirst of all you will you have to enter both the players name or game will not start\nAfter you enter the you can start the game, while you are playing your \nhistory is being recorded which you can see using the history menu\n'
        s+='if game draws then nothing will happen and you can restart the \ngame with same players name or restart the whole sessionbg=self.won_playpad of the playing. If anyone wins followinf things will happen, if the\ntotal score of thet player if greator with the present highscore the your name will replace them else not.\nYour highscore will be the total or sum of the all the score you \nrecived. you will recive 10 point if you win or else not if game is draw\n'
        s+='player 1 is X and player 2 is O\nTHANK YOU'
        tkMessageBox.showinfo('info',s)
        
    def showcredits(self): #will be used to show credits
        s='Game made by- jimmy kumar ahalpara and ayush singh\nGame based on cross and zero\nMade using python 2.7 and Tkinter GUI'
        tkMessageBox.showinfo('CREDITS',s)

    def startbuttonin(self,event): #this method is event method, will be executed is the related event will occure
        if self.startbutton['state']<>DISABLED:
            self.startbutton.config(bg=self.normal_clickedbutton)
            
    def startbuttonout(self,event): #event related method for start button
        self.startbutton.config(bg=self.normal_button)
        
    def restartbuttonin(self,event): #event related method for restart button
        if self.restartbutton['state']<>DISABLED:
            self.restartbutton.config(bg=self.normal_clickedbutton)
            
    def restartbuttonout(self,event): #event related method for restart button
        self.restartbutton.config(bg=self.normal_button)

    def gamerestartbuttonin(self,event): #event related method for restart button
        if self.gamerestartbutton['state']<>DISABLED:
            self.gamerestartbutton.config(bg=self.normal_clickedbutton)
            
    def gamerestartbuttonout(self,event): #event related method for restart button
        self.gamerestartbutton.config(bg=self.normal_button)
        
    def choosecolor(self): #this method will help in changing the game color
        self.colorchooser=Toplevel(self.mainwindow,bg=self.background,height=310,width=230) #creating the main widget
        Label(self.colorchooser,text='Buttons:').place(x=10,y=10) #creating the labels of different widgets
        Label(self.colorchooser,text='Buttons under cursor:').place(x=10,y=40)
        Label(self.colorchooser,text='Initial game pad:').place(x=10,y=70)
        Label(self.colorchooser,text='Game started:').place(x=10,y=100)
        Label(self.colorchooser,text='Game pad when x clicked:').place(x=10,y=130)
        Label(self.colorchooser,text='Game pad when o clicked:').place(x=10,y=160)
        Label(self.colorchooser,text='When anyone won:').place(x=10,y=190)
        Label(self.colorchooser,text='Background:').place(x=10,y=220)
        
        self.b1=Button(self.colorchooser,bg=self.normal_button,text='Change',command=lambda:self.changecolor(1)) #buttons to choose color
        self.b1.place(x=170,y=10) #placing the color
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
        Button(self.colorchooser,bg=self.normal_button,text='OK',command=self.ok_function).place(x=20,y=270) #this button will exit the toplevel and apply the changes
        Button(self.colorchooser,bg=self.normal_button,text='Apply',command=self.startchange).place(x=70,y=270) #this will only apply the chanages
        Button(self.colorchooser,bg=self.normal_button,text='Reset default',command=self.resetdefault).place(x=130,y=270) #this will resest all the colors to normal of default
        
    def changecolor(self,num): #will be used to choose color
        if num==1:
            self.normal_button=tkColorChooser.askcolor(parent=self.colorchooser)[1] #will use module tkColorChooser to return the hexadecimel code to the choosed color
            self.b1.config(bg=self.normal_button) #respective button color changed to the choosed color
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
            
    def startchange(self): #this method will apply the color change
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
        
    def ok_function(self): #this function will be called when ok button is clicked and this will apply channges and destory the box 
        self.colorchooser.destroy()
        self.startchange()
    def resetdefault(self): #resetting all the color to default
        self.normal_button='SystembuttonFace'
        self.normal_clickedbutton='grey'
        self.initial_playpad='pink'
        self.gamestarted_playpad='green'
        self.x_playpad='yellow'
        self.o_playpad='cyan'
        self.won_playpad='red'
        self.background='SystemButtonFace'
        self.startchange()
```

Uptill now we have defined the game playing class, which will manage the game.
Now Lets start the game...


```python
Maingamemodule().createwindow()
```

We can also use this to start the game


```python
obj = Maingamemodule()
obj.createwindow
```




**Following is the image showing how this game works with some basic level working (but not much technical and codeing related).**
![Chart](https://github.com/jimmyahalpara/Tic-Tac-Toe-with-Tkinter/blob/master/CHART%20-%20Copy.png)

The chart looks somewhat fancy, i believe, but it was made by me as a pary of high school peoject.
