BACKGROUND_COLOR = "#B1DDC6"
WHITE="#FFFFFF"
BLACK="#000000"

from tkinter import *
import pandas
import random


# ---------------------------- Implementation of LEARNING ------------------------------- #

data = pandas.read_csv("data/french_words.csv")

to_learn=data.to_dict(orient="records")

learned = pandas.read_csv("data/learned.csv")

learned=learned.to_dict(orient="records")

print(learned)

# sample = data.sample()

def take_a_sample():
    # # One of the way to get a sample
    # sample=data.sample()
    # sample=sample.squeeze(axis=0).to_list()

    global sample
    k=random.choice(to_learn)
    if k not in learned:
        sample=random.choice(to_learn)
    else:
        take_a_sample()



# _____________________

def wrong():
    take_a_sample()
    canvas.itemconfig(word, text=sample["French"])
    canvas.itemconfig(image, image=cardfront)
    canvas.itemconfig(lang, text="French")
    canvas.itemconfig(lang, fill=BLACK)
    canvas.itemconfig(word, fill=BLACK)
    wait_3sec(0)

def correct():
    learned.append(sample)

    pandas.DataFrame([sample]).to_csv("data/learned.csv", index=False, mode="a", header=False)

    # try:
    #     with open("data/learned.csv", "r") as file:
    #         pandas.DataFrame([sample]).to_csv("data/learned.csv", index=False, mode="a", header=False)
    # except FileNotFoundError:
    #     pandas.DataFrame([sample]).to_csv("data/learned.csv", index=False)

    take_a_sample()
    canvas.itemconfig(word, text=sample["French"])
    canvas.itemconfig(image, image=cardfront)
    canvas.itemconfig(lang, text="French")
    canvas.itemconfig(lang, fill=BLACK)
    canvas.itemconfig(word, fill=BLACK)

    wait_3sec(0)



def wait_3sec(count):
    if count == 1:
        canvas.itemconfig(word, text=sample["English"])
        canvas.itemconfig(image, image=cardback)
        canvas.itemconfig(lang, text="English")
        canvas.itemconfig(lang, fill=WHITE)
        canvas.itemconfig(word, fill=WHITE)
        window.after_cancel(wait_3sec)
        return
    window.after(3000, wait_3sec, count+1)

# ---------------------------- - - ---------- ------------------------------- #

# ---------------------------- UI SETUP of LEARNING ------------------------------- #


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
take_a_sample()

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
cardfront = PhotoImage(file="images/card_front.png")
cardback = PhotoImage(file="images/card_back.png")

image = canvas.create_image(400, 263, image=cardfront)
canvas.grid(column=0, row=0, columnspan=2)

cor = PhotoImage(file="images/right.png")
wro = PhotoImage(file="images/wrong.png")

button1 = Button(image=wro, highlightthickness=0, command=wrong)
button1.grid(column=0, row=1)
button2 = Button(image=cor, highlightthickness=0, command=correct)
button2.grid(column=1, row=1)

lang = canvas.create_text(400, 150, text="French", font=(("Ariel", 40, "italic")))
word = canvas.create_text(400, 263, text=sample["French"], font=("Ariel", 60, "bold"))

wait_3sec(0)

# ---------------------------- ----------------------------------------------- #





window.mainloop()