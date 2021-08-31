import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
TEMPO_MIN = 5
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    global ciclos

    if timer is not None:
        label_timer.config(text="Timer")
        window.after_cancel(timer)
        label_vistos.config(text="")
        canvas.itemconfig(texto, text="00:00")
        timer = None
        ciclos = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
ciclos = 0

def start_timer():
    if ciclos % 2 == 0:
        label_timer.config(text="WORK", fg=GREEN)
        count_down(WORK_MIN * TEMPO_MIN)
    elif ciclos % 7 == 0:
        label_timer.config(text="BREAK", fg=RED)
        count_down(LONG_BREAK_MIN * TEMPO_MIN)
    else:
        label_timer.config(text="BREAK", fg=PINK)
        count_down(SHORT_BREAK_MIN * TEMPO_MIN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutos = count // TEMPO_MIN
    segundos = count % TEMPO_MIN
    if segundos > 10:
        tempo = f"{minutos}:{segundos}"
    else:
        tempo = f"{minutos}:0{segundos}"

    canvas.itemconfig(texto, text=tempo)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        global ciclos
        ciclos += 1

        vistos = "✔" * int((ciclos + 1) / 2)
        label_vistos.config(text=vistos)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=203, height=224, bg=YELLOW, highlightthickness=0)

imagem = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=imagem)
texto = canvas.create_text(103, 130, fill="white", text="00:00", font= (FONT_NAME, 35, "bold"))

canvas.grid(column=1, row = 1)

label_timer = tkinter.Label(text="Timer", font = (FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=0)

botao_start = tkinter.Button(text="Start", font = (FONT_NAME, 14, "bold"), command=start_timer)
botao_start.grid(column=0, row=2)
botao_reset = tkinter.Button(text="Reset", font = (FONT_NAME, 14, "bold"), command=reset_timer)
botao_reset.grid(column=2, row=2)

label_vistos = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
label_vistos.grid(column=1, row=3)

window.mainloop()