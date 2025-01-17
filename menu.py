from PyQt5.QtWidgets import *

import database


def menu():
    window = QDialog()
    main_line = QVBoxLayout()
    add_btn = QPushButton("Добавити")
    quest_lbl = QLabel("Запитання")
    quest_ledt = QLineEdit()

    h1 = QHBoxLayout()
    h1.addWidget(quest_lbl)
    h1.addWidget(quest_ledt)
    main_line.addLayout(h1)


    right_lbl = QLabel("Правильна відповідь")
    right_ledt = QLineEdit()

    h2 = QHBoxLayout()
    h2.addWidget(right_lbl)
    h2.addWidget(right_ledt)
    main_line.addLayout(h2)


    wrong_lbl = QLabel("Неправильна відповідь 1")
    wrong_ledt = QLineEdit()

    h3 = QHBoxLayout()
    h3.addWidget(wrong_lbl)
    h3.addWidget(wrong_ledt)
    main_line.addLayout(h3)

    wrong1_lbl = QLabel("Неправильна відповідь 2")
    wrong1_ledt = QLineEdit()

    h4 = QHBoxLayout()
    h4.addWidget(wrong1_lbl)
    h4.addWidget(wrong1_ledt)
    main_line.addLayout(h4)

    wrong2_lbl = QLabel("Неправильна відповідь 3")
    wrong2_ledt = QLineEdit()

    h5 = QHBoxLayout()
    h5.addWidget(wrong2_lbl)
    h5.addWidget(wrong2_ledt)
    main_line.addLayout(h5)

    def add_func():
        new_quest = {
            "запитання": quest_ledt.text(),
            "Правильна відповідь": right_ledt.text(),
            "Не правильна відповідь1": wrong1_ledt.text(),
            "Не правильна відповідь2": "5",
            "Не правильна відповідь3": "7",

        }
        database.question.append(new_quest)

    add_btn.clicked.connect(add_func)
    main_line.addWidget(add_btn)














    window.setLayout(main_line)
    window.exec()

