from logging import root
from tkinter import *

if __name__ == '__main__':
    def finish():
        root.destroy()  # ручное закрытие окна и всего приложения
        print("Закрытие приложения")


    book = 0
    def click_txt1():
        global book
        book = '1'
        # изменяем текст на кнопке
        # btn["text"] = f"Clicks {book}"


    def click_txt2():
        global book
        book = '2'


    def click_txt3():
        global book
        book = '3'

    root = Tk()
    frame = Frame(root)
    frame.pack(anchor=S)

    labelframe = LabelFrame(root, text="This is a LabelFrame")
    labelframe.pack(fill="both", expand=TRUE)

    left = Label(labelframe, text="Inside the LabelFrame")
    left.pack()

    # lbl = Label(root, text="Привет", font=("Arial Bold", 50), bg="black", fg="red")
    # lbl.pack()

    redbutton = Button(frame, text="Сгущенное молоко - Варлам Шаламов", command=click_txt1)
    redbutton.pack(anchor=SW, fill=X, ipadx=10, ipady=5)

    greenbutton = Button(frame, text="Мастер и Маргарита - Михаил Булгаков", command=click_txt2)
    greenbutton.pack(anchor=S, fill=X, ipadx=10, ipady=5)

    bluebutton = Button(frame, text="Мы - Евгений Замятин", command=click_txt3)
    bluebutton.pack(anchor=SE, fill=X, ipadx=10, ipady=5)

    root.title('Частотный анализ текста')
    root.geometry('600x450')
    root.protocol("WM_DELETE_WINDOW", finish)
    root.mainloop()