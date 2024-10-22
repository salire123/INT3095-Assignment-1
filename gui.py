from customtkinter import *
from Assignment1 import question1, question2

def resize_frame(event):
    frame.configure(width=int(app.winfo_width() * 0.9), 
                    height=int(app.winfo_height() * 0.9))

def show_question1():
    hide_all_frames()
    frame_q1.place(relx=0.5, rely=0.5, anchor="center")

def show_question2():
    hide_all_frames()
    frame_q2.place(relx=0.5, rely=0.5, anchor="center")

def hide_all_frames():
    frame_q1.place_forget()
    frame_q2.place_forget()

def run_question1():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        q1 = question1(a, b, c)
        equation,result = q1.run()
        result_label_q1.configure(text=f"Result: {result}/nEquation: {equation}")
    except:
        result_label_q1.configure(text="Error, input not valid")

def run_question2():
    try:
        numbers = [float(x) for x in entry_numbers.get().split(',')]
        q2 = question2(numbers)
        sum_result = q2.my_sum()
        mean_result = q2.my_mean()
        median_result = q2.my_median()
        stdev_result = q2.my_stdev()
        max_result = q2.my_max()
        result_label_q2.configure(text=f"Sum: {sum_result}\nMean: {mean_result}\nMedian: {median_result}\nStdev: {stdev_result}\nMax: {max_result}")
    except:
        result_label_q2.configure(text="Error, input not valid")

app = CTk()
app.geometry("600x500")
app.title("Assignment 1")

frame = CTkFrame(master=app,
                 width=int(app.winfo_width() * 0.9),
                 height=int(app.winfo_height() * 0.9),
                 corner_radius=10)

frame.place(relx=0.5, rely=0.5, anchor="center")

# selection buttons
label_select = CTkLabel(master=frame, text="Select a question:")
label_select.place(relx=0.5, rely=0.1, anchor="center")

button_select_q1 = CTkButton(master=frame, text="Question 1", command=show_question1)
button_select_q1.place(relx=0.3, rely=0.2, anchor="center")

button_select_q2 = CTkButton(master=frame, text="Question 2", command=show_question2)
button_select_q2.place(relx=0.7, rely=0.2, anchor="center")

# Question 1 frame
frame_q1 = CTkFrame(master=frame, corner_radius=20)

label_q1 = CTkLabel(master=frame_q1, text="Question 1: Quadratic Equation")
label_q1.pack(pady=10)

entry_a = CTkEntry(master=frame_q1, placeholder_text="Enter a")
entry_a.pack(pady=5)

entry_b = CTkEntry(master=frame_q1, placeholder_text="Enter b")
entry_b.pack(pady=5)

entry_c = CTkEntry(master=frame_q1, placeholder_text="Enter c")
entry_c.pack(pady=5)

button_q1 = CTkButton(master=frame_q1, text="Solve", command=run_question1)
button_q1.pack(pady=10)

result_label_q1 = CTkLabel(master=frame_q1, text="Result will be displayed here", wraplength=400)
result_label_q1.pack(pady=10)

# Question 2 frame
frame_q2 = CTkFrame(master=frame, corner_radius=20)

label_q2 = CTkLabel(master=frame_q2, text="Question 2: Statistical Calculations")
label_q2.pack(pady=10)

entry_numbers = CTkEntry(master=frame_q2, placeholder_text="Enter numbers separated by commas, like 1,2,2,4,5", width=300)
entry_numbers.pack(pady=10)

button_q2 = CTkButton(master=frame_q2, text="Calculate", command=run_question2)
button_q2.pack(pady=10)

result_label_q2 = CTkLabel(master=frame_q2, text="Result will be displayed here", wraplength=400)
result_label_q2.pack(pady=10)


app.bind("<Configure>", resize_frame)
app.mainloop()
