#import csv and set inputs and output
import pandas as pd
df=pd.read_csv(r"D:\Prakash\Heart Disease Prediction\heart.csv")
x=df.drop("target",axis=1)
y=df["target"]

#datas train test split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

#model create and train
from sklearn.linear_model import LogisticRegression
model=LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)


#Check accuracy,precision,recall,f1,confusion matrix
from sklearn.metrics import accuracy_score,confusion_matrix,f1_score,precision_score,recall_score 
accuracy=accuracy_score(y_test,y_pred)
f1=f1_score(y_test,y_pred)
precision=precision_score(y_test,y_pred)
recall=recall_score(y_test,y_pred)
cm=confusion_matrix(y_test,y_pred)











#app
from PySide6.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QLineEdit,QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QDoubleValidator
app=QApplication()
win=QWidget()
win.setWindowTitle("Heart Disease Prediction")
win.setGeometry(200,100,800,600)
win.setFixedSize(800,600)
win.setStyleSheet("""QWidget{background:qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:1,stop:0 #0f2027,stop:0.5 #203a43,stop:1 #2c5364);}""")
des_label=QLabel("",win)
des_label.setGeometry(40,210,580,380)
title_label=QLabel("HEART DISEASE PREDICTION ❤️",win)
title_label.setGeometry(0,50,900,50)
title_label.setAlignment(Qt.AlignCenter)
title_label.setStyleSheet("color:white;font-size:40px;font:segoi UI")

name_label=QLabel("Name ",win)
name_label.setGeometry(130,160,65,30)
name_label.setAlignment(Qt.AlignCenter)
name_label.setStyleSheet("""QLabel{background-color:rgba(255,255,255,255,0.25);color:white;font-size:20px;border-radius:15px}""")
name_entry=QLineEdit(win)
name_entry.setGeometry(200,150,300,50)
name_entry.setPlaceholderText("Name")
name_entry.setStyleSheet("color:black;background-color:mediumaquamarine;font-size:20px;border-radius:20px")
name_entry.setAlignment(Qt.AlignCenter)


def clear_all():
    for i in inputs:
        i.clear()
name_button=QPushButton("Start",win)
name_button.setGeometry(520,150,160,50)
name_button.setStyleSheet("""QPushButton{color:black;font-size:20px;background-color:teal;border-radius:20px}
                          QPushButton:hover{background-color:beige}QPushButton:pressed{background-color:teal}""")
name_button.clicked.connect(clear_all)


xa=50
y=200
z=0
u=x.columns
w=0
for i in range(1,14):
    input_label=QLabel(u[w],win)
    input_label.setGeometry(xa,y,70,50)
    input_label.setStyleSheet("background-color:rgba(255,255,255,255,0.25);color:white;font-size:20px")
    input_label.setAlignment(Qt.AlignCenter)
    xa+=160
    w+=1
    z+=1
    if z==4:
        y+=90
        xa=50
        z=0

a=50
b=250
c=0
inputs=[]
for j in range(1,14):
    input_entry=QLineEdit(win)
    input_entry.setGeometry(a,b,100,50)
    input_entry.setStyleSheet("background-color:mediumaquamarine;color:black;font-size:20px;border-radius:25px")
    input_entry.setAlignment(Qt.AlignCenter)
    input_entry.setPlaceholderText("0")
    validator=QDoubleValidator(0.0,100.0,3)
    input_entry.setValidator(validator)
    inputs.append(input_entry)
    a+=150
    c+=1
    if c==4:
        b+=90
        a=50
        c=0





em_entry=QLineEdit(win)
em_entry.setGeometry(500,520,100,50)
em_entry.setStyleSheet("background-color:mediumaquamarine;color:black;font-size:20px;border-radius:25px")
em_entry.setAlignment(Qt.AlignCenter)
em_entry.setPlaceholderText("Acc")














import numpy as np
def predict():
    em_entry.setText(f"{accuracy:.2f}")
    user_data=[]
    for field in inputs:
            if field.text().strip() == "":
                QMessageBox.warning(win,"Error","Please fill all 13 values")
                return
            user_data.append(float(field.text()))
    array = np.array(user_data).reshape(1, -1) 
    prediction = model.predict(array)[0]
    probability = model.predict_proba(array)
    if prediction==1:
        msg=QMessageBox()
        msg.setWindowTitle("Result")
        msg.setText("Heart Disease Detected")
        msg.setIcon(QMessageBox.Warning)
        msg.setGeometry(400,300,200,100)
        msg.setStyleSheet("color:black;font-size:20px;background-color:aqua")
        msg.exec()
        # QMessageBox.Warning(win,"Result","Heart Disease Detected")
    else:
        msg1=QMessageBox()
        msg1.setWindowTitle("Result")
        msg1.setText("No Heart Disease Detected")
        msg1.setIcon(QMessageBox.Information)
        msg1.setGeometry(400,300,200,100)
        msg1.setStyleSheet("color:black;font-size:20px;background-color:aqua")
        msg1.exec()
        msg2=QMessageBox()
        msg2.setWindowTitle("Probability")
        msg2.setText(f"No Disease:{probability[0][0]:.2f}\nDisease:{probability[0][1]:.2f}")
        msg2.setIcon(QMessageBox.Warning)
        msg2.setGeometry(400,300,200,100)
        msg2.setStyleSheet("color:white;font-size:20px;background-color:aqua")
        msg2.exec()



pred_button=QPushButton("Predict",win)
pred_button.setGeometry(210,520,270,50)
pred_button.setStyleSheet("""QPushButton{color:black;font-size:30px;background-color:teal;border-radius:20px}
                          QPushButton:hover{background-color:beige}QPushButton:pressed{background-color:teal}""")
pred_button.clicked.connect(predict)


#chart
def click_cm():
    import seaborn as sns
    import matplotlib.pyplot as plt
    sns.heatmap(cm,annot=True,fmt="d")
    plt.xlabel("Predicted Value")
    plt.ylabel("Actual Value")
    plt.title("Confusion Matrix")
    plt.show()
def click_arp():
    import matplotlib.pyplot as plt
    x=["Accuracy","Precision","F1","Recall"]
    y=[accuracy,precision,f1,recall]
    plt.bar(x,y)
    plt.title("Evolution Matrix")
    plt.xlabel("Metrics")
    plt.ylabel("value")
    plt.show()



x1=630
y1=250
d=["Accuracy","Precision","F1","Confusion Matrix"]
for k in range(4):
    score_button=QPushButton(d[k],win)
    score_button.setGeometry(x1,y1,160,50)
    score_button.setStyleSheet("""QPushButton{color:black;font-size:20px;background-color:teal;border-radius:20px}
                          QPushButton:hover{background-color:beige}QPushButton:pressed{background-color:teal}""")
    y1+=90
    if d[k]=="Confusion Matrix":
        score_button.clicked.connect(click_cm)

    else:
        score_button.clicked.connect(click_arp)



































win.show()
app.exec()