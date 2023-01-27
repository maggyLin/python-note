import tkinter as tk
root = tk.Tk()
root.title('hello world')
root.geometry('500x500')

mylabel = tk.Label(root, text=' ', font=('Arial', 18), bg='yellow')
mylabel.pack()
# width , height 的屬性可以設定幾倍字元的高度
tk.Label(root, text='hello world', font=('Arial', 18), width=20, height=3).pack()
tk.Label(root, text='HI', font=('Arial', 18), height=2).pack()


# click 觸發 event ,觸發的事件要在呼叫前面 or event not defined
def button_event():
    mybutton['bg'] = 'blue'
    mybutton.config(text='hello world')  #不同修改寫法

mybutton = tk.Button(root, text='My button', height=3, command=button_event)
mybutton.pack()
#使用lambda寫法
tk.Button(root, text='lambda btn',  command=lambda : mybutton.config(text='HIHI')).pack()

def button_event(button, w, h):
    button.config(width=w, height=h)
    
mybutton2 = tk.Button(root, text='button 2')
mybutton2.configure(command=lambda: button_event(mybutton2,20,3))
mybutton2.pack()

# 關閉程式 : root.destroy  
mybutton3 = tk.Button(root, text='exit', command=root.destroy, width=20, height=3)
mybutton3.pack()

root.mainloop()