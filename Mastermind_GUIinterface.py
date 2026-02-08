from tkinter import *
from tkinter import messagebox

class medium:
    def user(self,color): # takes user' choice
        self.color=color
    def __init__(self): # generates random palette
        a=['#270101', '#F08B33', '#776B04', '#F1B848', '#8F715B', '#0486DB', '#C1403D', '#F3D4A0']
        import random
        self.b=[];n=4;
        while n!=0: 
            p=random.choice(a)
            if p not in self.b:
                self.b.append(p)
                n-=1
    def compare(self,g,l1):
        l=[] # hints           
        for x in range(4):
            if l1[x]==g[x]:
                l.append('red')
            elif l1[x]in g:
                l.append('gray')
        return l

class MasterMind():
    def __init__(self, root):
        self.root = root
        obj=medium()
        self.gen=obj.b  # generated color combo
        self.colors = ['#270101', '#F08B33', '#776B04', '#F1B848', '#8F715B', '#0486DB', '#C1403D', '#F3D4A0']
        root.geometry('390x600')
        root.title('Mastermind')
        
        for y in range(21):
            Grid.rowconfigure(root, y, weight=1)
        for x in range(8):
            Grid.columnconfigure(root, x, weight=1)
        
        # Help button
        help_btn = Button(root, text="How to Play", command=self.show_instructions, 
                         bg='#4CAF50', fg='white', font=('Arial', 10, 'bold'))
        help_btn.grid(row=0, column=0, columnspan=8, sticky='ew', padx=5, pady=5)
        
        self.palette = [] # display of palette
        n,c=0,0
        for i in self.colors:
            self.palette.append(Button(root, bg=i, height=1, width=5, relief=SUNKEN))
            self.palette[n].grid(row=21, column=c)
            n+=1;c+=1;
        self.palette[0].config(command=lambda: self.guess(root, self.palette[0]['bg'],obj))         # binding function to palette
        self.palette[1].config(command=lambda: self.guess(root, self.palette[1]['bg'],obj))
        self.palette[2].config(command=lambda: self.guess(root, self.palette[2]['bg'],obj))
        self.palette[3].config(command=lambda: self.guess(root, self.palette[3]['bg'],obj))
        self.palette[4].config(command=lambda: self.guess(root, self.palette[4]['bg'],obj))
        self.palette[5].config(command=lambda: self.guess(root, self.palette[5]['bg'],obj))
        self.palette[6].config(command=lambda: self.guess(root, self.palette[6]['bg'],obj))
        self.palette[7].config(command=lambda: self.guess(root, self.palette[7]['bg'],obj))
        self.user_choice = []  # stores the widget
        self.code = []  # stores the colors
        self.key = []  # stores the hints
        global ccol, cro
        ccol,cro = 2,20
    
    def show_instructions(self):
        instructions_window = Toplevel(self.root)
        instructions_window.title("How to Play Mastermind")
        instructions_window.geometry("450x500")
        instructions_window.resizable(False, False)
        
        # Title
        title_label = Label(instructions_window, text="MASTERMIND", 
                           font=('Arial', 18, 'bold'), fg='#C1403D')
        title_label.pack(pady=10)
        
        # Instructions frame
        frame = Frame(instructions_window, padx=20, pady=10)
        frame.pack(fill=BOTH, expand=True)
        
        instructions_text = """
OBJECTIVE:
Crack the secret 4-color code within 19 attempts.

HOW TO PLAY:
1. The computer generates a secret code of 4 different 
   colors from the 8 available colors.

2. Click on colors from the palette at the bottom to 
   make your guess (select 4 colors).

3. After each guess, you'll receive hints on the right:

   🔴 RED hint = Correct color in correct position
   
   ⚫ GRAY hint = Correct color but wrong position
   
   No hint = Color is not in the secret code

4. Use these hints to refine your next guess.

5. You win if you guess the exact code!
   You lose if you use all 19 attempts.

TIPS:
• Each color in the secret code is unique (no repeats)
• Pay attention to which colors get hints
• Start by identifying which colors are in the code
• Then work on positioning them correctly

COLORS AVAILABLE:
Dark Brown, Orange, Olive, Gold, 
Tan, Blue, Red, Cream
"""
        
        text_label = Label(frame, text=instructions_text, justify=LEFT, 
                          font=('Arial', 10), wraplength=400)
        text_label.pack(fill=BOTH, expand=True)
        
        # Color legend
        legend_frame = Frame(instructions_window)
        legend_frame.pack(pady=5)
        
        Label(legend_frame, text="Color Palette:", font=('Arial', 10, 'bold')).pack()
        
        colors_frame = Frame(legend_frame)
        colors_frame.pack(pady=5)
        
        color_names = ['Dark Brown', 'Orange', 'Olive', 'Gold', 'Tan', 'Blue', 'Red', 'Cream']
        for i, color in enumerate(self.colors):
            color_box = Label(colors_frame, bg=color, width=3, height=1, relief=RAISED)
            color_box.grid(row=0, column=i, padx=2)
        
        # Close button
        close_btn = Button(instructions_window, text="Got it! Let's Play", 
                          command=instructions_window.destroy,
                          bg='#4CAF50', fg='white', font=('Arial', 11, 'bold'),
                          padx=20, pady=5)
        close_btn.pack(pady=15)
        
    def guess(self, root, choice,obj):
            global ccol
            global cro
            f=True  # boolean flag
            if cro != 1:
                self.user_choice.append(Button(root, bg=choice, height=1, width=5, relief=RAISED))
                if len(self.user_choice) < 4:
                    self.user_choice[-1].grid(row=cro, column=ccol)
                    self.code.append(self.user_choice[-1]['bg'])
                    ccol += 1
                elif len(self.user_choice) == 4:
                    self.user_choice[-1].grid(row=cro, column=ccol)
                    self.code.append(self.user_choice[-1]['bg'])
                    ccol += 1
                    ccol = 2
                    cro = cro-1
                    obj.user(self.code) # send the user's choice
                    self.key=obj.compare(self.code,self.gen) #get the hints
                    if self.key==['red','red','red','red']:
                        f=False
                        self.hint(root, self.key)
                        l=Label(root,text="CONGRATULATIONS!!!", font=('Arial', 12, 'bold'), fg='green')
                        l.grid(row=1,columnspan=8)
                    else:
                        self.hint(root, self.key)
                        self.code = []
                        self.user_choice = []
            else:
                if f:
                    l=Label(root,text="Game Over! ANSWER:", font=('Arial', 10, 'bold'), fg='red')
                    l.grid(row=1,columnspan=4)
                    c=5
                    for i in self.gen:                        
                        b=Button(root,bg=i,height=1, width=5, relief=SUNKEN)
                        b.grid(row=1,column=c)
                        c+=1
    global hcol, hro
    hcol,hro = 8,20
    def hint(self, root, key):
        global hcol, hro
        a = []
        for i in key:
            a.append(Label(root, bg=i,relief=SUNKEN))
            a[-1].grid(row=hro, column=hcol, sticky=E)
            hcol += 1
        hro -= 1;hcol = 8;

master = Tk()
M = MasterMind(master)
master.mainloop()
