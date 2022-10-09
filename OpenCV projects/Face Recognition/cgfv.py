import tkinter as tk

parent = tk.Tk()
parent.geometry("300x300")
frame = tk.Frame(parent)
frame.pack()

name = tk.StringVar()


def write_text():
    print(name.get())


inp = tk.Entry(frame, textvariable=name)
inp.pack()

text_disp = tk.Button(frame,
                      text="Ok",
                      command=write_text
                      )

text_disp.pack(side=tk.LEFT)

exit_button = tk.Button(frame,
                        text="Exit",
                        fg="green",
                        command=quit)
exit_button.pack(side=tk.RIGHT)

parent.mainloop()
