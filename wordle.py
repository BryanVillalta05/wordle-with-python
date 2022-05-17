import tkinter, random

ventana= tkinter.Tk()#ventana
ventana.title('wordle')
ventana.geometry("450x400")#tamaño de la ventana

def next():
    ventana.geometry("450x150")
    frm_bienvenida.destroy()
    frm_instrucciones.destroy()
    frm_texto.destroy()
    btn.destroy()
    word= random.choice(["sweet", "bingo", "truck", "jumps", "alike", "asset", "began", 
                        "avoid", "award", "blame", "bound", "cycle", "eager", "grace", 
                        "frank", "guest", "gross", "inner", "issue", "joint", "label", 
                        "lucky", "lease", "rough", "scope", "undue", "treat", "yield",
                        "abaft", "bench", "round", "booth", "chain", "chief", "court",
                        "about", "above", "acute", "admit", "adopt", "adult", "actor",
                        "basic", "basis", "blind", "baker", "block", "board", "bread",
                        "civil", "clock", "coast", "clear", "coach", "close", "click",
                        "cross", "curve", "dance", "depth", "dealt", "dozen", "drill",
                        "chest", "chase", "crowd", "crown", "doubt", "drove", "entry",
                        "fiber", "fleet", "found", "faith", "grown", "issue", "input",
                        "layer", "lease", "list", "label", "meant", "might", "loose",
                        "mount", "newly", "night", "ought", "occur", "minus", "phase",
                        "pitch", "plate", "plain", "pound", "pride", "prime", "prize",
                        "prior", "rapid", "ratio", "raise", "reach", "roger", "route",
                        "scale", "scene", "serve", "shift", "shell", "sharp", "shall",
                        "skill", "spent", "waste", "smoke", "sound", "spoke", "south",
                        "stell", "stage", "steam", "stake", "split", "spare", "stick",
                        "strip", "taxes", "stuff", "stood", "taken", "thick", "tight",
                        "theft", "tough", "twice", "truth", "tries", "upset", "usage", 
                        "value", "waste", "wheel", "whose", "worth", "wound", "whole",
                        "valid", "kicks", "bring", "whool", "crazy", "balmy", "joker",
                        "prank", "trick", "aback", "awful", "aware", "brave", "arise",
                        "anger", "blood", "brain", "owner", "piece", "earth", "jazzy",
                        "black", "buzzy", "muzzy", "frame", "ahead", "array", "aside", 
                        "never", "gonna", "chart", "grasp", "champ", "breed", "buyer"])
    print(word)
    

    def check(): #funcion que va a detectar cada letra que se ingrese
        #variables fila 1
        entry_ans=Entry1_1.get()
        entry_ans2=Entry1_2.get()
        entry_ans3=Entry1_3.get()   #variables que van a tomar todo lo que se ingrese
        entry_ans4=Entry1_4.get()
        entry_ans5=Entry1_5.get()
        if entry_ans in word and entry_ans != "":             
            Entry1_1.configure(bg ="blue") 
        if entry_ans == word[0]: 
            Entry1_1.configure(bg ="red")
        if entry_ans2 in word and entry_ans2 != "":             
            Entry1_2.configure(bg ="blue")
        if entry_ans2 == word[1]:
            Entry1_2.configure(bg ="red")   
        if entry_ans3 in word and entry_ans3 != "":             
            Entry1_3.configure(bg ="blue")          #condicionales que van a hacer los operadores par detectar-
        if entry_ans3 == word[2]:                   #si cada letra concuerda la funcion .configure()
            Entry1_3.configure(bg ="red")           #es la que les va a cambiar el color a las casillas
        if entry_ans4 in word and entry_ans4 != "":             
            Entry1_4.configure(bg ="blue")
        if entry_ans4 == word[3]:
            Entry1_4.configure(bg ="red")
        if entry_ans5 in word and entry_ans5 != "":             
            Entry1_5.configure(bg ="blue")
        if entry_ans5 == word[4]:
            Entry1_5.configure(bg ="red")
        
        #Fila 2
        entry_ans_2=Entry2_1.get()
        entry_ans2_2=Entry2_2.get()
        entry_ans3_2=Entry2_3.get()   
        entry_ans4_2=Entry2_4.get()
        entry_ans5_2=Entry2_5.get()
        if entry_ans_2 in word and entry_ans_2 != "":
            Entry2_1.configure(bg ="blue")
        if entry_ans_2 == word[0]: 
            Entry2_1.configure(bg ="red")
        if entry_ans2_2 in word and entry_ans2_2 != "":
            Entry2_2.configure(bg ="blue")  
        if entry_ans2_2 == word[1]:
            Entry2_2.configure(bg ="red")   
        if entry_ans3_2 in word and entry_ans3_2 != "":
            Entry2_3.configure(bg ="blue")
        if entry_ans3_2 == word[2]:               
            Entry2_3.configure(bg ="red")   
        if entry_ans4_2 in word and entry_ans4_2 != "":
            Entry2_4.configure(bg ="blue")
        if entry_ans4_2 == word[3]:
            Entry2_4.configure(bg ="red")
        if entry_ans5_2 in word and entry_ans5_2 != "":
            Entry2_5.configure(bg ="blue")
        if entry_ans5_2 == word[4]:
            Entry2_5.configure(bg ="red")

        #Fila 3
        entry_ans_3=Entry3_1.get()
        entry_ans2_3=Entry3_2.get()
        entry_ans3_3=Entry3_3.get()   
        entry_ans4_3=Entry3_4.get()
        entry_ans5_3=Entry3_5.get()
        if entry_ans_3 in word and entry_ans_3 != "":
            Entry3_1.configure(bg ="blue")
        if entry_ans_3 == word[0]: 
            Entry3_1.configure(bg ="red")
        if entry_ans2_3 in word and entry_ans2_3 != "":
            Entry3_2.configure(bg ="blue")  
        if entry_ans2_3 == word[1]:
            Entry3_2.configure(bg ="red")   
        if entry_ans3_3 in word and entry_ans3_3 != "":
            Entry3_3.configure(bg ="blue")
        if entry_ans3_3 == word[2]:               
            Entry3_3.configure(bg ="red")   
        if entry_ans4_3 in word and entry_ans4_3 != "":
            Entry3_4.configure(bg ="blue")
        if entry_ans4_3 == word[3]:
            Entry3_4.configure(bg ="red")
        if entry_ans5_3 in word and entry_ans5_3 != "":
            Entry3_5.configure(bg ="blue")
        if entry_ans5_3 == word[4]:
            Entry3_5.configure(bg ="red")

        #Fila 4
        entry_ans_4 =Entry4_1.get()
        entry_ans2_4=Entry4_2.get()
        entry_ans3_4=Entry4_3.get()   
        entry_ans4_4=Entry4_4.get()
        entry_ans5_4=Entry4_5.get()
        if entry_ans_4 in word and entry_ans_4 != "":
            Entry4_1.configure(bg ="blue")
        if entry_ans_4 == word[0]: 
            Entry4_1.configure(bg ="red")
        if entry_ans2_4 in word and entry_ans2_4 != "":
            Entry4_2.configure(bg ="blue")  
        if entry_ans2_4 == word[1]:
            Entry4_2.configure(bg ="red")   
        if entry_ans3_4 in word and entry_ans3_4 != "":
            Entry4_3.configure(bg ="blue")
        if entry_ans3_4 == word[2]:               
            Entry4_3.configure(bg ="red")   
        if entry_ans4_4 in word and entry_ans4_4 != "":
            Entry4_4.configure(bg ="blue")
        if entry_ans4_4 == word[3]:
            Entry4_4.configure(bg ="red")
        if entry_ans5_4 in word and entry_ans5_4 != "":
            Entry4_5.configure(bg ="blue")
        if entry_ans5_4 == word[4]:
            Entry4_5.configure(bg ="red")
        
        #Fila 5
        entry_ans_5=Entry5_1.get()
        entry_ans2_5=Entry5_2.get()
        entry_ans3_5=Entry5_3.get()   
        entry_ans4_5=Entry5_4.get()
        entry_ans5_5=Entry5_5.get()
        if entry_ans_5 in word and entry_ans_5 != "":
            Entry5_1.configure(bg ="blue") 
        if entry_ans_5 == word[0]: 
            Entry5_1.configure(bg ="red")
        if entry_ans2_5 in word and entry_ans2_5 != "":
            Entry5_2.configure(bg ="blue")  
        if entry_ans2_5 == word[1]:
            Entry5_2.configure(bg ="red")   
        if entry_ans3_5 in word and entry_ans3_5 != "":
            Entry5_3.configure(bg ="blue")
        if entry_ans3_5 == word[2]:              
            Entry5_3.configure(bg ="red")   
        if entry_ans4_5 in word and entry_ans4_5 != "":
            Entry5_4.configure(bg ="blue")
        if entry_ans4_5 == word[3]:
            Entry5_4.configure(bg ="red")
        if entry_ans5_5 in word and entry_ans5_5 != "":
            Entry5_5.configure(bg ="blue")
        if entry_ans5_5 == word[4]:
            Entry5_5.configure(bg ="red")

        #Fila 6
        entry_ans_6=Entry6_1.get()
        entry_ans2_6=Entry6_2.get()
        entry_ans3_6=Entry6_3.get()   
        entry_ans4_6=Entry6_4.get()
        entry_ans5_6=Entry6_5.get()
        if entry_ans_6 in word and entry_ans_6 != "":
            Entry6_1.configure(bg ="blue")
        if entry_ans_6 == word[0]: 
            Entry6_1.configure(bg ="red")
        if entry_ans2_6 in word and entry_ans2_6 != "":
            Entry6_2.configure(bg ="blue")  
        if entry_ans2_6 == word[1]:
            Entry6_2.configure(bg ="red")  
        if entry_ans3_6 in word and entry_ans3_6 != "":
            Entry6_3.configure(bg ="blue")
        if entry_ans3_6 == word[2]:               
            Entry6_3.configure(bg ="red")   
        if entry_ans4_6 in word and entry_ans4_6 != "":
            Entry6_4.configure(bg ="blue")
        if entry_ans4_6 == word[3]:
            Entry6_4.configure(bg ="red")
        if entry_ans5_6 in word and entry_ans5_6 != "":
            Entry6_5.configure(bg ="blue")
        if entry_ans5_6 == word[4]:
            Entry6_5.configure(bg ="red")
        
        


    #fila 1
    Entry1_1 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus") #Se define el campo
    Entry1_1.place(x=10, y=10)                                       #Se coloca en pantalla
    Entry1_2 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry1_2.place(x=70, y=10)
    Entry1_3 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry1_3.place(x=130, y=10)
    Entry1_4 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry1_4.place(x=190, y=10)
    Entry1_5 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry1_5.place(x=250, y=10)

    #fila 2
    Entry2_1 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry2_1.place(x=10, y=30)
    Entry2_2 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry2_2.place(x=70, y=30)
    Entry2_3 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry2_3.place(x=130, y=30)
    Entry2_4 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry2_4.place(x=190, y=30)
    Entry2_5 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry2_5.place(x=250, y=30)

    #fila 3
    Entry3_1 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry3_1.place(x=10, y=50)
    Entry3_2 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry3_2.place(x=70, y=50)
    Entry3_3 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry3_3.place(x=130, y=50)
    Entry3_4 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry3_4.place(x=190, y=50)
    Entry3_5 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry3_5.place(x=250, y=50)

    #fila 4
    Entry4_1 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry4_1.place(x=10, y=70)
    Entry4_2 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry4_2.place(x=70, y=70)
    Entry4_3 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry4_3.place(x=130, y=70)
    Entry4_4 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry4_4.place(x=190, y=70)
    Entry4_5 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry4_5.place(x=250, y=70)

    #fila 5
    Entry5_1 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry5_1.place(x=10, y=90)
    Entry5_2 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry5_2.place(x=70, y=90)
    Entry5_3 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry5_3.place(x=130, y=90)
    Entry5_4 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry5_4.place(x=190, y=90)
    Entry5_5 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry5_5.place(x=250, y=90)
    #fila 6
    Entry6_1 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry6_1.place(x=10, y=110)
    Entry6_2 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry6_2.place(x=70, y=110)
    Entry6_3 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry6_3.place(x=130, y=110)
    Entry6_4 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry6_4.place(x=190, y=110)
    Entry6_5 = tkinter.Entry(ventana, width=10, bd=5, cursor="plus")
    Entry6_5.place(x=250, y=110)

    #Boton para empezar a checar los input
    submit=tkinter.Button(ventana, text="check", padx=20, pady=20, relief=tkinter.GROOVE, command=check, activebackground='#345', font="Arial 10 bold")
    
    submit.place(x=350, y=50)


frm_bienvenida = tkinter.Label(ventana, text="Welcome to Wordle", font="Arial 30 bold") 
frm_bienvenida.place(x=10, y=30)

frm_instrucciones = tkinter.Label(ventana, text="Instructions:", font="Arial 20 bold") 
frm_instrucciones.place(x=10, y=90)

frm_texto = tkinter.Label(ventana, font="Arial", justify= tkinter.LEFT, 
text="-Wordle is a word guessing game. \n-The word has 5 letters \n-In each cell you must add a word. \n-If the CELL turns red the letter is correct. \n-When all the CELLS are red in the same line, you have won.\n-You have 6 chances to find the word. \n-To check the word you press the CHECK button.") 
frm_texto.place(x=10, y=130)

btn=tkinter.Button(ventana, text="Next", padx=5, pady=5, relief=tkinter.GROOVE, font="Arial 20 bold", command=next, activebackground='#345')
btn.place(x=30, y=300)



ventana.mainloop() #bucle principal


"""
Use tkinter porque ya estoy familiarizado con las funciones y metodos que maneja.

la variable ventana es la que crea el programa aparte y geometry es solo para el tamaño

el "ventana.mainloop()" es porque se necesita de un bucle para mantener corriendo el programa

el tkinter.Entry es para crear el campo de texto, los parametros que maneja es donde va a ir ubicada
y un extra que es el width qu, bd=5, cursor="plus"e es para que no sea tan largo el campo

solo hay una fila que no esta comentada ya que como usaremos el metodo place se necesita de cordenadas
en x y en y, así que hay que configurar eso pero luego ya que si hay que calcular.
"""