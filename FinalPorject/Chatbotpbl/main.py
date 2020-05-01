
from chatterbot import  ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp



engine = pp.init()

voices= engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot = ChatBot("My Bot")

convo_greet= [
    "Hello","Hi there","How are you",
    "Whats up?","How can I help you?","Good Morning",
    "Welcome to Sharda University website",
    "help","what can i help you with?"
]

convo_greet_bye = ["Bye", "See you later", "Goodbye",
                   "thanks for visiting","Have a good day",
                   "Bye! Come back again soon."
                   ,"Thanks", "Happy to help!",
                   "Thank you", "Any time!",
                   "That's helpful", "My pleasure"
                   ]

convo_main01= ["What hours are you open?","We're open every day 9am-9pm",
               "What are your hours?","Our hours are 9am-9pm every day"
               "at what time are you opne?","We're open every day 9am-9pm"]

convo_main02 = ["What courses are  available?",
                "'Engineering and Technology,"
                "\nBusiness Studies,Architecture & PlanningMedia,"
                "\nFilm and Entertainment,"
                "\nLaw,"
                "\nHumanities "
                "\n Social Sciences,"
                "\nDental Sciences,"
                "\nMedical Sciences & Research,"
                "\nBasic Sciences & Research"
                "\n,Nursing Sciences & Research\
                n,Pharmacy,"
                "\nEducation,"
                "\nAgricultural Sciences,"
                "\nAllied Health Sciences'",
                "Is there any kind of Scholarship?","Yes,we do have scholarship scheme","Am i eligible for a scholarship?",
                "We offer scholarship","Can i get any kind of discount on fee?","for detailed info visit scholarship column in the website.",
                    "Is there hostel facility available?","We have separate boys and girls hostel available inside the premises of university.",
                "Is there any hostel facility for non-locals?",
                "Yes, we have hostel facility for the ones who one to avail it."

                ,"Is there any refund policy?",
                "Refunds are not applicable",
                "How can i get my money back?",
                "There is no refund policy",
                "How can i get my advance payment back?",
                "Sorry! No refund",
                "How do i get admission?",
                "You have to appear for the entrance exam.",
                "How can i apply for a course?",
                "Visit or contact administration of Sharda University.",
                "How can i enroll myslef?",
                "Fill the online Entrance application form",
                "Where do i get application form?",
                "For detailed info visit ADMISSION column.",
                "Is there any anti-ragging policy?",
                "We have anti-ragging form that is mandatory to be filled.",

                "Whom can i contact for detailed information?",
                "You can either e-mail or call for your queries.The contact information are available in the website",
                "I need contact information",
                "National Whatsapp- 8800533663,International  Whatsapp- +91-8800998881",
                    "Are placement programmes avalaible?","we do offer placement options","Which companies come for placement?",
                    "All the details are available in the website"


                ]

trainer = ListTrainer(bot)

trainer.train(convo_greet)
trainer.train(convo_greet_bye)
trainer.train(convo_main01)
trainer.train(convo_main02)


#ans = bot.get_response("how are you doing?")
#print(ans)
# print("Talk to your Bot")
# while True:
#     query = input()
#     if query== 'exit':
#         break
#     answer =bot.get_response(query)
#     print("bot : ",answer)

main = Tk()


main.config(bg="#2874A6")


main.geometry("500x650")

main.title("Sharda ChatBot")
img = PhotoImage(file="shardalogo.png")
photoL=Label(main,image=img)
photoL.pack(pady=5)

def ask_from_bot():
    query = textF.get()
    ans_from_bot= bot.get_response(query)
    msgs.insert(END,"You :"+ query)
    print(type(ans_from_bot))
    msgs.insert(END,"Bot :"+ str(ans_from_bot))
    speak(ans_from_bot)
    textF.delete(0,END)
    msgs.yview(END)



frame = Frame(main)
sc = Scrollbar(frame,bg="#2874A6")
msgs = Listbox(frame,width=80,height=20,yscrollcommand=sc.set,font=30,bg="#1FCBCB")

sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)

frame.pack()

#creating text field

textF = Entry(main,font=("Verdana",20),bg="#C6D523")
textF.pack(fill=X,pady=10)

btn =Button(main,text="Ask your Query",font=("Verdana",20),command=ask_from_bot)
btn.pack()

#creating a function
def enter_function(event):
    btn.invoke()

#going to bind main window with enter key

main.bind('<Return>',enter_function)


main.mainloop()