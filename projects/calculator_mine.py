from tkinter import*

def btn_click(numbers):
	global operator
	operator=operator+ str(numbers)
	text_input.set(operator)

def btnClearDisplay():
	global operator
	operator=""
	text_input.set("")

def btnEqualsInput():
	global operator
	sumup=str(eval(operator))
	text_input.set(sumup)
	operator=""

cal = Tk()
cal.title("My Calculator")
operator=""
text_input = StringVar()

txtDisplay = Entry(cal,font=('arial', 20,'bold'), textvariable=text_input, bd=30, insertwidth=4, bg="sky blue", justify='right').grid(columnspan=4)
#=================================================== 
btn7=Button(cal,padx=16,pady=16,bd=8,font=('arial', 20,'bold'),text="7",bg="powder blue",command=lambda:btn_click(7)).grid(row=1,column=0)
btn8=Button(cal,padx=16,pady=16,bd=8,font=('arial', 20,'bold'),text="8",bg="powder blue",command=lambda:btn_click(8)).grid(row=1,column=1)
btn9=Button(cal,padx=16,pady=16,bd=8,font=('arial', 20,'bold'),text="9",bg="powder blue",command=lambda:btn_click(9)).grid(row=1,column=2)
Add=Button(cal,padx=16,pady=16,bd=8,font=('arial', 20,'bold'),text="+",bg="powder blue",command=lambda:btn_click("+")).grid(row=1,column=3)
#====================================================
btn4=Button(cal,padx=16,pady=16,bd=8,font=('arial', 20,'bold'),text="4",bg="powder blue",command=lambda:btn_click(4)).grid(row=2,column=0)
btn5=Button(cal,padx=16,pady=16,bd=8,font=('arial', 20,'bold'),text="5",bg="powder blue",command=lambda:btn_click(5)).grid(row=2,column=1)
btn6=Button(cal,padx=16,pady=16,bd=8,font=('arial', 20,'bold'),text="6",bg="powder blue",command=lambda:btn_click(6)).grid(row=2,column=2)
Sub=Button(cal,padx=16,pady=16,bd=8,font=('arial', 20,'bold'),text="-",bg="powder blue",command=lambda:btn_click("-")).grid(row=2,column=3)
#====================================================
btn1=Button(cal,padx=16,pady=16,bd=8,font=('arial', 20,'bold'),text="1",bg="powder blue",command=lambda:btn_click(1)).grid(row=3,column=0)
btn2=Button(cal,padx=16,pady=16,bd=8,font=('arial', 20,'bold'),text="2",bg="powder blue",command=lambda:btn_click(2)).grid(row=3,column=1)
btn3=Button(cal,padx=16,pady=16,bd=8,font=('arial', 20,'bold'),text="3",bg="powder blue",command=lambda:btn_click(3)).grid(row=3,column=2)
Mult=Button(cal,padx=16,pady=16,bd=8,font=('arial', 20,'bold'),text="*",bg="powder blue",command=lambda:btn_click("*")).grid(row=3,column=3)
#====================================================
btn0=Button(cal,padx=16,pady=16,bd=8,font=('arial', 20,'bold'),text="0",bg="powder blue" ,command=lambda:btn_click(0)).grid(row=4,column=0)
btnPoint=Button(cal,padx=16,pady=16,bd=8,font=('arial', 20,'bold'),text=".",bg="powder blue" ,command=lambda:btn_click(".")).grid(row=4,column=1)
btnClear=Button(cal,padx=16,pady=16,bd=8,font=('arial', 20,'bold'),text="C",bg="powder blue",command=btnClearDisplay).grid(row=4,column=2)
Div=Button(cal,padx=16,pady=16,bd=8,font=('arial', 20,'bold'),text="/",bg="powder blue",command=lambda:btn_click("/")).grid(row=4,column=3)
btnEquals=Button(cal,padx=130,pady=16,bd=8,font=('arial', 20,'bold'),text="=",bg="powder blue",command= btnEqualsInput).grid(row=5,column=0,columnspan=4)

cal.mainloop()