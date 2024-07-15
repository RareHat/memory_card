from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
menu_btn = QPushButton("Меню")

relax_btn = QPushButton("Відпочити")
timer_sbx = QSpinBox()
min_lbl = QLabel("Хвилин")
quest_lbl = QLabel("2+2")
varl1_btn = QRadioButton("1")
varl2_btn = QRadioButton("2")
varl3_btn = QRadioButton("3")
varl4_btn = QRadioButton("4")
answer_btn = QPushButton("Відповісти")

group = QGroupBox("Варіанти відповідей")

main_line = QVBoxLayout()
horizontal_line1 = QHBoxLayout()
horizontal_line1.addWidget(menu_btn)
horizontal_line1.addStretch(1)
horizontal_line1.addWidget(relax_btn)
horizontal_line1.addWidget(timer_sbx)
horizontal_line1.addWidget(min_lbl)
main_line.addLayout(horizontal_line1)
main_line.addWidget(quest_lbl)

group_main_line = QVBoxLayout()
group_main_line.addWidget(varl1_btn)
group_main_line.addWidget(varl2_btn)
group_main_line.addWidget(varl3_btn)
group_main_line.addWidget(varl4_btn)
group.setLayout(group_main_line)
main_line.addWidget(group)
main_line.addWidget(answer_btn)



































window.setLayout(main_line)
window.show()
app.exec()












