import sys
from PySide6.QtCore import QProcess
from PySide6.QtWidgets import QWidget,QApplication,QLabel,QPushButton
from PySide6.QtCore import Qt,QTimer
from PySide6.QtGui import QFont
app=QApplication()
win=QWidget()
win.setGeometry(400,100,800,600)
win.setFixedSize(800,600)
win.setWindowTitle("Quiz")
win.setStyleSheet("""
         background: qlineargradient(
        x1:0, y1:0, x2:1, y2:1,
        stop:0 #0f2027,
        stop:0.5 #134e4a,
        stop:1 #0d7377
    )
""")
font=QFont("poppins",30)
head_label=QLabel("QUIZ",win)
head_label.setGeometry(300,50,200,50)
head_label.setAlignment(Qt.AlignCenter)
head_label.setFont(font)
head_label.setStyleSheet("""QLabel {
        color: white;  
        border-radius: 20px;  
background: qlineargradient(
    x1:0, y1:0, x2:1, y2:1,
    stop:0 #0f2027,
    stop:0.5 #134e4a,
    stop:1 #0d7377
)
    }
""")
score=0
time_value=20
score_label=QLabel(f"Score - {score}",win)
score_label.setGeometry(30,150,200,50)
score_label.setStyleSheet("""QLabel { 
        color:white; 
        font-size:30px;
        border-radius: 20px;
       background: qlineargradient(
    x1:0, y1:0, x2:1, y2:1,
    stop:0 #0f2027,
    stop:0.5 #134e4a,
    stop:1 #0d7377
)
        }"""     
        )
score_label.setAlignment(Qt.AlignCenter)

time_label=QLabel(f"Time - {time_value}",win)
time_label.setGeometry(550,150,200,50)
time_label.setStyleSheet("""QLabel { 
        color:white; 
        font-size:30px;
        border-radius: 20px;
       background: qlineargradient(
    x1:0, y1:0, x2:1, y2:1,
    stop:0 #0f2027,
    stop:0.5 #134e4a,
    stop:1 #0d7377
)
        }"""     
        )
time_label.setAlignment(Qt.AlignCenter)
timer=QTimer()
timer.setInterval(1000)
score_out=QLabel(win)
score_out.setGeometry(250,400,300,50)
score_out.setAlignment(Qt.AlignCenter)
score_out.hide()
score_out.setStyleSheet("""QLabel{color:white;font-size:30px;border-radius:20px;background: qlineargradient(
    x1:0, y1:0, x2:1, y2:1,
    stop:0 #0f2027,
    stop:0.5 #134e4a,
    stop:1 #0d7377
)}
            """)
ques=[
    "1.What is the capital of France?",
    "2.What is the capital of Japan?",
    "3.What is the capital of Brazil?",
    "4.What is the capital of Canada?",
    "5.What is the capital of Australia?",
    "6.What is the capital of Germany?",
    "7.What is the capital of Italy?",
    "8.What is the capital of Egypt?",
    "9.What is the capital of Mexico?",
    "10.What is the capital of India",
    "11.Which country is BMW from?",
    "12.Which country is Mercedes-Benz from?",
    "13.Which country is Honda from?",
    "14.Which country is Lamborghini from?",
    "15.Which country is Maserati from?",
    "16.Which country is Nissan from?",
    "17.Which country is Jaguar from?",
    "18.Which country is Ford from?",
    "19.Which country is Porsche from?",
    "20.Which country is Ferrari from?",
     "21.Who won the ICC Cricket World Cup 2019?",
    "22.Who is known as 'God of Cricket'?",
    "23.Which country hosted the first ever Cricket World Cup in 1975?",
    "24.How many players are there in a cricket team?",
    "25.Who has scored the fastest century in ODI cricket?",
    "26.Which bowler has taken the most wickets in Test cricket?",
    "27.What is the maximum number of overs in a T20 match per side?",
    "28.Which country has won the most ICC Cricket World Cups?",
    "29.Who is the captain of India in the 2023 Cricket World Cup?",
    "30.Which player scored the highest individual score in ODI cricket?",
    "31.Which country is called the 'Land of the Rising Sun'?",
    "32.Who was the first President of the United States?",
    "33.What is the largest desert in the world?",
    "34.Which planet has the most moons in our solar system?",
    "35.Who wrote the book '1984'?",
    "36.What is the chemical symbol for gold?",
    "37Which river is the longest in the world?",
    "38.Who painted the 'Mona Lisa'?",
    "39.In which year did India gain independence?",
    "40.Which gas is most abundant in the Earth's atmosphere?",
    "41.Which actor played Jack Dawson in Titanic?",
    "42.Which actress won an Oscar for her role in La La Land?",
    "43.Who portrayed the character of Harry Potter in the film series?",
    "44.Which actor is known for playing Captain Jack Sparrow in Pirates of the Caribbean?",
    "45.Which actress played Katniss Everdeen in The Hunger Games series?",
    "46.Who played Deadpool in the Deadpool movies?",
    "47.Which actor starred as the Joker in the 2019 film Joker?",
    "48.Which actress played Hermione Granger in the Harry Potter series?",
    "49.Which actor played Forrest Gump in the 1994 movie?",
    "50.Which actress starred as Black Widow in the Marvel Cinematic Universe?"
    
]

options=options = [
    ["Paris", "Lyon", "Marseille", "Nice"],                 # France
    ["Osaka", "Tokyo", "Kyoto", "Hiroshima"],              # Japan
    ["Rio de Janeiro", "Brasília", "São Paulo", "Salvador"],# Brazil
    ["Toronto", "Vancouver", "Montreal", "Ottawa"],        # Canada
    ["Sydney", "Canberra", "Melbourne", "Brisbane"],       # Australia
    ["Berlin", "Munich", "Frankfurt", "Hamburg"],          # Germany
    ["Milan", "Rome", "Venice", "Florence"],               # Italy
    ["Alexandria", "Giza", "Cairo", "Luxor"],              # Egypt
    ["Mexico City", "Guadalajara", "Monterrey", "Cancun"], # Mexico
    ["New Delhi", "Mumbai", "Bangalore", "Kolkata"],
    ["USA", "Germany", "Italy", "Sweden"],         # BMW
    ["Germany", "UK", "Italy", "USA"],             # Mercedes-Benz
    ["Germany", "Japan", "South Korea", "USA"],    # Honda
    [ "UK", "France","Italy", "Germany"],          # Lamborghini
    [ "France", "Germany","Italy", "UK"],          # Maserati
    ["Japan", "Germany", "USA", "Italy"],          # Nissan
    ["UK", "Italy", "Germany", "USA"],             # Jaguar
    [ "Germany", "Italy","USA", "Japan"],          # Ford
    ["Germany", "Italy", "France", "UK"],          # Porsche
    ["Germany","Italy",  "UK", "USA"],             # Ferrari (alternate)
    ["India", "Australia", "England", "New Zealand"],             # Q1 → answer=2
    ["Sachin Tendulkar", "MS Dhoni", "Virat Kohli", "Brian Lara"], # Q2 → answer=0
    ["Australia", "England", "India", "West Indies"],             # Q3 → answer=1
    ["9", "10", "11", "12"],                                      # Q4 → answer=3
    ["Chris Gayle", "Shahid Afridi", "AB de Villiers", "Brian Lara"], # Q5 → answer=3
    ["Shane Warne", "M Muralitharan", "Anil Kumble", "James Anderson"], # Q6 → answer=1
    ["50", "10", "20", "15"],                                     # Q7 → answer=2
    ["England", "India", "Australia", "Pakistan"],                # Q8 → answer=2
    ["Virat Kohli", "Rohit Sharma", "MS Dhoni", "KL Rahul"],     # Q9 → answer=1
    ["Rohit Sharma", "Sachin Tendulkar", "Martin Guptill", "Chris Gayle"],
     ["Japan", "China", "Thailand", "South Korea"],            # correct at index 0
    ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams"],  # correct at index 2
    ["Sahara", "Gobi", "Kalahari", "Arabian"],               # correct at index 3
    ["Jupiter", "Mars", "Saturn", "Neptune"],                # correct at index 1
    ["George Orwell", "Aldous Huxley", "J.K. Rowling", "Ernest Hemingway"], # correct at index 1
    ["Ag", "Au", "Gd", "Go"],                                 # correct at index 2
    ["Amazon", "Nile", "Yangtze", "Mississippi"],            # correct at index 0
    ["Vincent Van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"], # correct at index 0
    ["1945", "1947", "1950", "1939"],                         # correct at index 2
    ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
      ["Leonardo DiCaprio", "Brad Pitt", "Tom Cruise", "Matt Damon"],
    [ "Jennifer Lawrence", "Meryl Streep", "Natalie Portman","Emma Stone",],
    [ "Rupert Grint", "Tom Holland", "Daniel Radcliffe","Asa Butterfield"],
    [ "Chris Hemsworth","Johnny Depp", "Orlando Bloom", "Robert Downey Jr."],
    [ "Emma Watson", "Scarlett Johansson","Jennifer Lawrence", "Shailene Woodley"],
    [ "Chris Evans", "Hugh Jackman", "Chris Pratt","Ryan Reynolds"],
    [ "Heath Ledger", "Joaquin Phoenix","Jared Leto", "Jack Nicholson"],
    [ "Bonnie Wright", "Evanna Lynch","Emma Watson", "Danielle Radcliffe"],
    ["Tom Hanks", "Matt Damon", "Will Smith", "Russell Crowe"],
    [ "Elizabeth Olsen", "Brie Larson", "Gal Gadot","Scarlett Johansson"]      # correct at index 1
]


  

opt=["A","B","C","D"]
answers=[
    0,  # France → "Paris"
    1,  # Japan → "Tokyo"
    1,  # Brazil → "Brasília"
    3,  # Canada → "Ottawa"
    1,  # Australia → "Canberra"
    0,  # Germany → "Berlin"
    1,  # Italy → "Rome"
    2,  # Egypt → "Cairo"
    0,  # Mexico → "Mexico City"
    0,
    1,  # BMW → Germany
    0,  # Mercedes-Benz → Germany
    1,  # Honda → Japan
    2,  # Lamborghini → Italy
    2,  # Maserati → Italy
    0,  # Nissan → Japan
    0,  # Jaguar → UK
    2,  # Ford → USA
    0,  # Porsche → Germany
    1,  # Ferrari → Italy
    2,
    0,
    3,
    2,
    2,
    1,
    2,
    2,
    1,
    0,
    0,2,0,2,0,1,1,1,1,1,
    0,3,2,1,2,3,1,2,0,3
]



x=100
y=400
z=0
w=0
a=40
ques_index=0
buttons=[]
labels=[]
def start_timer():
     global time_value
     time_value-=1
     time_label.setText(f"Time - {time_value}")
     if time_value<=0:
          timer.stop()
          next_question()

def load_ques():
        global time_value
        time_value=20
        time_label.setText(f"Time - {time_value}")
        timer.start()
        ques_label.setText(ques[ques_index])
        for h in range(len(options[ques_index])):
             buttons[h].setText(options[ques_index][h])
def restart_app():
    QProcess.startDetached(sys.executable, sys.argv)
    QApplication.quit()
       
restart_button=QPushButton("Restart",win)
restart_button.setGeometry(250,500,150,50)
restart_button.setStyleSheet("""QPushButton{color:white;font-size:30px;border-radius:20px;background: qlineargradient(
    x1:0, y1:0, x2:1, y2:1,
    stop:0 #0f2027,
    stop:0.5 #134e4a,
    stop:1 #0d7377
)}
            QPushButton:hover{background-color:lightskyblue}
            QPushButton:pressed{background-color:lightskyblue}""")
restart_button.clicked.connect(restart_app)   
restart_button.hide()   
exit_button=QPushButton("Exit",win)
exit_button.setGeometry(410,500,150,50)
exit_button.setStyleSheet("""QPushButton{color:white;font-size:30px;border-radius:20px;background: qlineargradient(
    x1:0, y1:0, x2:1, y2:1,
    stop:0 #0f2027,
    stop:0.5 #134e4a,
    stop:1 #0d7377
)}
            QPushButton:hover{background-color:lightskyblue}
            QPushButton:pressed{background-color:lightskyblue}""")
exit_button.clicked.connect(QApplication.quit)
exit_button.hide()
def next_question():
    global ques_index
    ques_index += 1
    if ques_index < len(ques):
        load_ques()
    else:
        # Quiz finished
        ques_label.setText("Quiz Finished!")
        score_out.show()
        restart_button.show()
        exit_button.show()
        score_label.hide()
        time_label.hide()
        head_label.hide()
        for d in buttons:
            d.hide()
        for e in labels:
            e.hide()

    
    
def click_button(clicked_answer):
    global ques_index,w,score
    timer.stop()
    if clicked_answer==answers[ques_index]:
         score+=10
         score_out.setText(f"Your Score is {score}")
         score_label.setText(f"Score - {score}")
    next_question()
timer.timeout.connect(start_timer)
ques_label=QLabel(ques[ques_index],win)
ques_label.setGeometry(50,300,700,80)
ques_label.setStyleSheet("""QLabel { 
        color:white; 
        font-size:30px;
        border-radius:32px;
        background:transparent;border:none}"""     
        )
ques_label.setWordWrap(True)
ques_label.setAlignment(Qt.AlignCenter)
for j in range(4):
     ques_label.setText(ques[ques_index])
for i in range(4):
    button=QPushButton(options[w][z],win)
    button.setGeometry(x,y,250,50)
    button.setStyleSheet("""QPushButton{color:white;font-size:20px;border-radius:20px;background: qlineargradient(
    x1:0, y1:0, x2:1, y2:1,
    stop:0 #0f2027,
    stop:0.5 #134e4a,
    stop:1 #0d7377
)}
                         QPushButton:hover{background-color:lightskyblue}
                          QPushButton:pressed{background-color:lightskyblue}""")
    buttons.append(button)
    button.clicked.connect(lambda checked=False,idx=i:click_button(idx))

    opt_label=QLabel(opt[z],win)
    opt_label.setGeometry(a,y,55,50)
    opt_label.setStyleSheet("""QLabel { 
        color:white; 
        font-size:30px;
        border-radius: 20px;
        background: qlineargradient(
    x1:0, y1:0, x2:1, y2:1,
    stop:0 #0f2027,
    stop:0.5 #134e4a,
    stop:1 #0d7377
)
        }"""     
        )
    opt_label.setAlignment(Qt.AlignCenter)
    labels.append(opt_label)

    a+=380
    x+=380
    z+=1
    if z==2:
        x=100
        a=40
        y+=100
































load_ques()
win.show()
app.exec()
