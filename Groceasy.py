from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit,QTextEdit
from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QFileDialog


app = QApplication()
win = QWidget()
win.setGeometry(500, 50, 360, 640)
win.setFixedSize(360,640)
win.setWindowTitle("Groceasy")
win.setStyleSheet("""
QWidget {
    background: qlineargradient(
        x1:0, y1:0, x2:1, y2:1,
        stop:0 #2196F3, 
        stop:1 #21CBF3
    );
}
""")

# Total grocery
grocery_label = QLabel("Total Amount", win)
grocery_label.setGeometry(30, 50, 200, 50)
grocery_label.setStyleSheet("""
QLabel {
    color: white;
    font-size: 24px;
    font-weight: bold;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #2196F3, stop:1 #21CBF3);
    border-radius: 15px;
    padding: 5px;
    border: 2px solid #1976D2;
}
""")

grocery_entry = QLineEdit(win)
grocery_entry.setGeometry(250, 50, 100, 50)
grocery_entry.setPlaceholderText("Amount")
grocery_entry.setAlignment(Qt.AlignCenter)
grocery_entry.setStyleSheet("""
    QLineEdit {
        color: white;               /* user-entered text color */
        font-size: 20px;            /* user-entered text size */
        font-weight: bold;
        border-radius: 20px;
        background-color: #1E88E5;  /* soft blue background */
        padding: 10px;
        border: 2px solid #1565C0;
    }
     QLineEdit:focus {
    border: 2px solid #E1BEE7;
    background-color: #F3E5F5;
    color: #333333;
}
    QLineEdit::placeholder {
        color: #BBDEFB;            /* lighter color for placeholder */
        font-size: 10px;            /* smaller placeholder text */
        font-style: italic;
    }
    """)
grocery_entry.setValidator(QIntValidator(0, 100000))

# Name and amount entries
name_entries = []
amount_entries = []

y = 120
for i in range(5):
    name_entry = QLineEdit(win)
    name_entry.setGeometry(30, y, 200, 50)
    name_entry.setPlaceholderText(f"Enter name {i+1}")
    name_entry.setAlignment(Qt.AlignCenter)
    name_entry.setMaxLength(14)
    name_entry.setStyleSheet("""
    QLineEdit {
        color: white;               /* user-entered text color */
        font-size: 20px;            /* user-entered text size */
        font-weight: bold;
        border-radius: 20px;
        background-color: #1E88E5;  /* soft blue background */
        padding: 10px;
        border: 2px solid #1565C0;
    }
      QLineEdit:focus {
    border: 2px solid #E1BEE7;
    background-color: #F3E5F5;
    color: #333333;
}
    QLineEdit::placeholder {
        color: #BBDEFB;            /* lighter color for placeholder */
        font-size: 10px;            /* smaller placeholder text */
        font-style: italic;
    }
    """)

    name_entries.append(name_entry)
    y += 60

y1 = 120
for i in range(5):
    amount_entry = QLineEdit(win)
    amount_entry.setGeometry(250, y1, 100, 50)
    amount_entry.setPlaceholderText("Amount")
    amount_entry.setAlignment(Qt.AlignCenter)
    amount_entry.setStyleSheet("""
    QLineEdit {
        color: white;               /* user-entered text color */
        font-size: 20px;            /* user-entered text size */
        font-weight: bold;
        border-radius: 20px;
        background-color: #1E88E5;  /* soft blue background */
        padding: 10px;
        border: 2px solid #1565C0;
    }
     QLineEdit:focus {
    border: 2px solid #E1BEE7;
    background-color: #F3E5F5;
    color: #333333;
}
    QLineEdit::placeholder {
        color: #BBDEFB;            /* lighter color for placeholder */
        font-size: 10px;            /* smaller placeholder text */
        font-style: italic;
    }
    """)

    amount_entry.setValidator(QIntValidator(0, 100000))
    amount_entries.append(amount_entry)
    y1 += 60

# Output
output_label = QTextEdit(win)
output_label.setGeometry(30, 470, 300, 160)
output_label.setReadOnly(True)
output_label.setStyleSheet("""
QTextEdit {
    color: white;
    font-size: 16px;
    font-weight: bold;
    background: qlineargradient(
        x1:0, y1:0, x2:1, y2:1,
        stop:0 #4CAF50, stop:1 #81C784
    );
    border-radius: 20px;
    padding: 10px;
    border: 2px solid #388E3C;
}
""")


# Calculation
def calculation():
    try:
        total = float(grocery_entry.text())
        if total <= 0:
            output_label.setText("⚠ Enter total amount > 0")
            return
    except:
        output_label.setText("⚠ Enter valid total amount")
        return

    balances = []
    sum_paid = 0  # sum of entered amounts
    for i in range(5):
        name = name_entries[i].text().strip()
        amount_text = amount_entries[i].text().strip()
        if name and amount_text:
            paid = float(amount_text)
            balances.append([name, paid])
            sum_paid += paid

    if not balances:
        output_label.setText("⚠ No valid entries found!")
        return

    # ✅ Check if sum of individual amounts matches total
    if round(sum_paid, 2) != round(total, 2):
        output_label.setText(f"⚠ Sum of entered amounts (₹{sum_paid}) does not match Total Amount (₹{total})")
        return

    people_count = len(balances)
    share = total / people_count

    net_balances = []
    for name, paid in balances:
        net_balances.append([name, round(paid - share, 2)])

    creditors = [[n, b] for n, b in net_balances if b > 0]
    debtors = [[n, -b] for n, b in net_balances if b < 0]

    result = f"Total Amount : ₹{total}\n"
    result += f"Each Share : ₹{round(share,2)}\n\n"

    for debtor in debtors:
        debtor_name, debt_amt = debtor
        debt = debt_amt

        for creditor in creditors:
            cred_name, cred_amt = creditor
            if cred_amt <= 0:
                continue

            pay = round(min(debt, cred_amt), 2)
            result += f"{debtor_name} should pay {cred_name} : ₹{pay}\n"

            creditor[1] -= pay
            debt -= pay

            if debt <= 0:
                break

    output_label.setText(result)


    output_label.setText(result)




# Button
cal_button = QPushButton("Calculate", win)
cal_button.setGeometry(30, 430, 200, 30)
cal_button.setStyleSheet("""
QPushButton {
    color: white;
    font-size: 18px;
    border-radius: 10px;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #4CAF50, stop:1 #2E7D32);
    border: 2px solid #1B5E20;
}
QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #66BB6A, stop:1 #388E3C);
}
QPushButton:pressed {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #2E7D32, stop:1 #1B5E20);
}
""")
cal_button.clicked.connect(calculation)


def reset_fields():
    grocery_entry.clear()
    output_label.clear()
    for field in name_entries:
        field.clear()
    for field in amount_entries:
        field.clear()


reset_btn = QPushButton("Reset", win)
reset_btn.setGeometry(300, 430, 50, 30)
reset_btn.setStyleSheet("""
QPushButton {
    color: white;
    font-size: 18px;
    border-radius: 10px;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #FF5252, stop:1 #D32F2F);
    border: 2px solid #B71C1C;
}
QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #FF867F, stop:1 #E53935);
}
QPushButton:pressed {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #D32F2F, stop:1 #B71C1C);
}
""")
reset_btn.clicked.connect(reset_fields)


def save_output():
    text = output_label.toPlainText()
    # If using QTextEdit use:
    # text = output_label.toPlainText()

    if not text.strip():
        output_label.setText("Nothing to save!")
        return

    file_path, _ = QFileDialog.getSaveFileName(
        win,
        "Save File",
        "",
        "Text Files (*.txt)"
    )

    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)

        output_label.setText("Saved Successfully ✅")


save_button = QPushButton("Save", win)
save_button.setGeometry(240, 430, 50, 30)
save_button.clicked.connect(save_output)
save_button.setStyleSheet("""
QPushButton {
    color: white;
    font-size: 18px;
    border-radius: 10px;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #FF5252, stop:1 #D32F2F);
    border: 2px solid #B71C1C;
}
QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #FF867F, stop:1 #E53935);
}
QPushButton:pressed {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #D32F2F, stop:1 #B71C1C);
}
""")

win.show()

app.exec()
