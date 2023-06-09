from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import shuffle
from random import randint


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


question_list = []
question_list.append(Question('Что изображено на флаге Вьетнама', 'Звезда', 'Серп и молот', 'Лист', 'Полоска какая-то'))
question_list.append(Question('Какое число будет 7 января', '7 января', '11 марта', '23 февраля', '1 сентября'))
question_list.append(Question('Почему слово слово назвали слово', 'потому что', 'да', 'нет', 'что???'))


app = QApplication([])

btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире?') 

RadioGroupBox = QGroupBox("Варианты ответов")


rbtn_1 = QRadioButton('в1')
rbtn_2 = QRadioButton('в2')
rbtn_3 = QRadioButton('в3')
rbtn_4 = QRadioButton('в4')

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('Правильно/Неправильно') 
lb_Correct = QLabel('Правильный ответ')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) 

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

    
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(otvet):
    lb_Result.setText(otvet)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        window.score += 1
        print('- Всего вопросов:', window.total)
        print('- Правильных ответов:', window.score)
        print('Рейтинг:', window.score / window.total * 100, '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно')
            print('Рейтинг:', window.score / window.total * 100, '%')
    

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 

def test():
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()

def next_question():
    window.total += 1
    print('- Всего вопросов:', window.total)
    print('- Правильных ответов:', window.score)
    print('Рейтинг:', window.score / window.total * 100, '%')
    window.cur_question = window.cur_question + 1
    window.cur_question = randint(0, len(question_list) - 1)
    q = question_list[window.cur_question]
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    q = question_list[window.cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.cur_question = -1

btn_OK.clicked.connect(click_OK) 

window.total = 0
window.score = 0

next_question()
window.show()
app.exec_()