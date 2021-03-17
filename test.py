def number():
	global ans
	app.set(ans.get())
	print(ans.get())
	sa.append(ans.get())
	print(sa)

sa = []

import tkinter as tk

window = tk.Tk()
window.title("測試")

top_label = tk.Label(window, text = '標題').grid(row = 0, column = 0)

ans = tk.StringVar()
enter = tk.Entry(window, textvariable = ans).grid(row =1, column = 0)


push = tk.Button(window, text= '輸入', command = number)
push.grid(row = 2, column = 0)

app = tk.StringVar()
appear_label = tk.Label(window, textvariable = app).grid(row = 3, column = 0)


window.mainloop()

