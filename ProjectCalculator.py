#ณัชพล กิตคราม 6410742156
from tkinter import*
#สร้าง Tkinter และกำหนดlogo ขนาดจอ พื้นหลัง และห้ามย่อขยาย
root = Tk()
root.title("Calculator")
#icon
# img = PhotoImage(file='calculator.png')
# root.iconphoto(False,img)
root.geometry("375x667+600+30")
root.resizable(0,0)

#กำหนด stype font & color font เพื่อให้สะดวกต่อการใช้งาน
L_FONT_STYPE = ("Arial", 40, "bold")
S_FONT_STYPE = ("Arial", 16)
HISTORY_FONT_STYPE = ("Arial", 14, "underline")
TITLE_HISTORY_FONT_STYPE = ("Arial", 24, "bold")
DATA_FONT_STYPE = ("Arial", 12)
HISTORY_SMALLHIS_FONT_STYPE = ("Arial", 12)
DIGIT_FONT_STYPE = ("Arial", 24, "bold")
DEFAULE_FONT_STYPE = ("Arial", 22)

FG_TOTAL = "#0ea87f"
FG_SYMBOL = "#19ba94"
FG_DIGIT = "#92a39d"
LABEL_COLOR = "#25265E"
DARK_GRAY = "#696969"
OFF_WHITE = "#F8FAFF"

BG_DISPLAY = "#212b41"
DARK_BLUE = "#2e3951"
DARK_GREEN = "#0db387"
BG_DIGIT = "#333f59"
BG_SYMBOL = "#26324b"


#สร้างตัวแปรเพื่อเก็บคำตอบที่จะแสดง
total_expression =""
current_expression = ""
history = ""

#สร้างdict เพื่อเก็บตัวเลขและก็ '.' เพื่อใช้loop for แสดงเป็นปุ่มตัวเลขออกมา และง่ายในการใช้งาน (key :value)
digits = {
    7: (1, 1), 8: (1, 2), 9: (1, 3),
    4: (2, 1), 5: (2, 2), 6: (2, 3),
    1: (3, 1), 2: (3, 2), 3: (3, 3),
    0: (4, 2), '.': (4, 1)
}

#สร้างdict เพื่อเก็บเครื่องหมาย เพื่อใช้loop for แสดงเป็นปุ่มออกมา และง่ายในการใช้งาน (key :value)
operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

#function
#function เพิ่มตัวเลขและเครื่องหมายเข้าในlabel และ ตัวแปร
def add_to_expresstion(value):
    global current_expression
    global history
    current_expression += str(value)
    update_label()

#update label ข้างบน
def update_label():
    global history
    current_label.config(text=str(current_expression[:11]))  #ความยาวตัวเลขในช่องผลลัพธ์ไม่เกิน11

#update label ผลรวม
def update_total_label():
    global total_expression
    expression = total_expression
    #ใช้loop for เพื่อreplace key ==> value
    for operator, symbol in operations.items():
        expression = expression.replace(operator, f' {symbol} ')
    total_label.config(text=expression)
    

#function เพิ่ม เครื่องหมายตัวดำเนินการ
def append_operator(operator):
    global current_expression
    global total_expression
    current_expression += str(operator)
    total_expression += str(current_expression)
    current_expression = ""
    update_total_label()
    update_label()

#function ไว้ลบทุกอย่างในlabel กดปุ่มแล้วจะเซ็ตค่าผลลัพธ์ และโจทย์ที่จะให้โปรแกรมหาผลลัพธ์
def f_claer():
    global current_expression
    global total_expression
    current_expression = ""
    total_expression = ""
    update_label()
    update_total_label()

#function คำนวณแสดงผลลัพธ์ ใช้eval function มาช่วยในการหาผลลัพธ์ และtry except เพื่อแสดงerror เมื่อผู้ใช้ป้อนเลขที่คำนวณไม่ได้หรือไม่นิยาม เช่น 1/0
def f_evaluate():
    global total_expression
    global current_expression
    global history

    total_expression += str(current_expression)
    update_total_label()
    #เก็บข้อมูลลงประวัติ เพื่อนำไปแสดงในหน้าประวัติการคำนวณ เก็บโดยใช้การสไลด์ หากข้อมูลยาวเกินหน้าประวัติในบันทึกลงบรรทัดถัดไป หากไม่ยาวให้เก็บในบรรทัดเดียว
    try:
        current_expression = str(eval(total_expression))
        history = total_expression
        fw = open("History.txt","a",encoding="utf-8")
        if len(history) <= 23:
            w_history = str(history)+" = "+current_expression
            fw.writelines(w_history[0:23] +"\n")
            fw.close()
        else:
            w_history = str(history)+" =  "+current_expression
            fw.writelines(w_history[0:23] + "\n" + w_history[24:47] + "\n" + w_history[48:70]+ "\n" + w_history[71:93] + "\n" + w_history[94:] + "\n")
            fw.close()
        history = ""                  #set ตัวแปร์กลับdefult
        total_expression = ""
    except Exception as e:            #ถ้าคิดในเงื่อนไขที่ไม่มีนิยาม จะแสดงคำว่าerror
        current_expression = "Error"
    finally:
        update_label()

    total_expression = ""
    update_label()

#function ยกกำลัง2 ใช้eval ช่วยในการคำนวณ ข้อความโดยจะคำ
def square():
    global current_expression
    current_expression = str(eval(f"{current_expression}**2"))
    update_label()

#function สแควรูท ใช้eval ช่วยในการคำนวณ
def sqrt():
    global current_expression
    current_expression = str(eval(f"{current_expression}**0.5"))
    update_label()

#รับค่าทางแป้นพิมพ์ตัวเลข ถ้ากดปุ่มenter เรียก f_evaluate ถ้ากดตัวเลขก็ addตัวเลขเข้าไป โดยเรียกadd expresstion & append operator
root.bind('<Return>', lambda event: f_evaluate())
for key in digits:
    root.bind(str(key), lambda event, digit=key: add_to_expresstion(digit))
for key in operations:
    root.bind(str(key), lambda event, operator=key: append_operator(operator))

display_frame = Frame(root,height=221,bg=BG_DISPLAY)
display_frame.pack(expand=True, fill="both")

#function checkfile ถ้าเครื่องuser 1ยังไม่มีไฟล์historeyจะทำการสร้างใหม่
def checkfile():
    try:
        #หาไฟล์
        fr = open("History.txt","r",encoding="utf-8")
        fr.read()
        fr.close()
    except FileNotFoundError:
        #สร้างfile
        fw = open("History.txt","w",encoding="utf-8")
        fw.close()
checkfile()
#-------------------------------------------------------------------------------
#หน้าประวัติ
def openWinHis():
    
    winhis = Tk()
    winhis.title("History Calculator")
    winhis.geometry("290x400+300+40")
    winhis.configure(bg=DARK_BLUE)
    winhis.resizable(0,0)

    #สร้างframe ในหน้าที่2
    title_frame = Frame(winhis,width=280,height=50,bg=DARK_BLUE)
    title_frame.pack(pady=5)
    
    data_frame = Frame(winhis,width=280,height=270,bg=DARK_BLUE)
    data_frame.pack(pady=0)

    btn_frame = Frame(winhis,width=200,height=30,bg=DARK_BLUE)
    btn_frame.pack(anchor=E,pady=20,padx=5)

    #Label ประวัติ ตรงหัว
    heading = Label(title_frame,text='History',bg=DARK_BLUE,fg="white",font=TITLE_HISTORY_FONT_STYPE)
    heading.pack(anchor=N)

    #function ให้อ่านไฟล์history แล้วโชว์ประวัติ
    def showhis():
        global labelHis
        fr = open("History.txt","r",encoding="utf-8")
        labelHis = StringVar()
        labelHis = Label(data_frame,text=fr.read(),fg=OFF_WHITE,bg=DARK_BLUE,font=DATA_FONT_STYPE,pady=5,justify=LEFT).place(x=20)
    #run function showhis
    showhis()

    #function Clear History กดเคลียร์ข้อมูลให้history
    def clearHis():
        fw = open("History.txt","w",encoding="utf-8")
        fw.close()
        data_frame = Frame(winhis,width=280,height=275,bg=DARK_BLUE)
        data_frame.place(y=45,x=5)

    Button(btn_frame,text='ล้างประวัติ',bg='#C0C0C0',fg='black',border=0,cursor='hand2',
    font=HISTORY_SMALLHIS_FONT_STYPE,command=clearHis).grid(row=0,column=0,padx=10)


    #run mainloop winhis
    winhis.mainloop()
#-------------------------------------------------------------------------------

history_frame = Frame(root,height=100,width=150,bg=BG_DISPLAY)
history_frame.place(x=0,y=0)
#ปุ่มไปหน้าประวัติ
button_history = Button(history_frame,width=6,text='history',border=0,bg=BG_DISPLAY,fg=DARK_GRAY,cursor='hand2',font=HISTORY_FONT_STYPE,command=openWinHis,activebackground=BG_DISPLAY,foreground='white')
button_history.pack(padx=15,pady=15)

button_frame = Frame(root)
button_frame.pack(expand=True,fill="both")

button_frame.rowconfigure(0, weight=1)

#ลูปให้ขนาดปุ่มเต็มจอ
for x in range(1,5):
    button_frame.rowconfigure(x, weight=1)
    button_frame.columnconfigure(x, weight=1)

#ช่องdisplay แสดงผล
total_label = Label(display_frame,text=total_expression,anchor=E,bg=BG_DISPLAY,fg=FG_TOTAL,padx=24,font=S_FONT_STYPE)
total_label.pack(expand=True,fill='both')
current_label = Label(display_frame,text=current_expression,anchor=E,bg=BG_DISPLAY,fg=DARK_GREEN,padx=24,font=L_FONT_STYPE)
current_label.pack(expand=True,fill='both')

#create number button
for digit,grid_value in digits.items():
    button =Button(button_frame, text=str(digit),bg=BG_DIGIT,fg=FG_DIGIT,font=DIGIT_FONT_STYPE,
            borderwidth=0,command=lambda d=digit: add_to_expresstion(d))
    button.grid(row=grid_value[0],column=grid_value[1],sticky=NSEW)

#create operator button
i = 0
for operator,symbol in operations.items():
    oper_button = Button(button_frame,text=symbol,bg=BG_SYMBOL,fg=FG_SYMBOL,font=DEFAULE_FONT_STYPE, 
            borderwidth=0,command=lambda o=operator: append_operator(o))
    oper_button.grid(row=i ,column=4 ,sticky=NSEW)
    i += 1

#create clear button
clear_button = Button(button_frame,text="C",bg=BG_SYMBOL,fg=FG_SYMBOL,font=DEFAULE_FONT_STYPE,
        borderwidth=0,command=f_claer)
clear_button.grid(row=0 ,column=1 , columnspan=1,sticky=NSEW)

#create square button
square_button = Button(button_frame,text="X\u00b2",bg=BG_SYMBOL,fg=FG_SYMBOL,font=DEFAULE_FONT_STYPE,
        borderwidth=0,command=square)
square_button.grid(row=0 ,column=2 , columnspan=1,sticky=NSEW)

#create square button
sqrt_button = Button(button_frame,text="\u221ax",bg=BG_SYMBOL,fg=FG_SYMBOL,font=DEFAULE_FONT_STYPE,
        borderwidth=0,command=sqrt)
sqrt_button.grid(row=0 ,column=3 , columnspan=1,sticky=NSEW)

#create equals button
equals_button = Button(button_frame,text="=",bg=FG_SYMBOL,fg="#2e3951",font=DEFAULE_FONT_STYPE,
        borderwidth=0,command=f_evaluate)
equals_button.grid(row=4 ,column=3 , columnspan=2,sticky=NSEW)

root.mainloop()