from PySide import QtCore, QtGui
import sys
from ui import Ui_MainWindow


# Create application
app = QtGui.QApplication(sys.argv)

# Create form and init UI
MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

# Hook logic

# -------Переменные----------

# Переменная хранящая ответ
answer = ""

# Операнд 1
oper_1 = ""

# Операнд 2
oper_2 = ""

# Операция
operation = ""

# -------Функции кнопок-------

# Кнопка 0
def b_0_clicked():
	global answer

	if answer == "":
		answer = "0"
	else:
		answer += "0"

	ui.lineEdit_2.setText(answer)

# Кнопка 1
def b_1_clicked():
	global answer

	if answer == "":
		answer = "1"
	else:
		answer += "1"

	ui.lineEdit_2.setText(answer)

# Кнопка 2
def b_2_clicked():
	global answer

	if answer == "":
		answer = "2"
	else:
		answer += "2"

	ui.lineEdit_2.setText(answer)

# Кнопка 3
def b_3_clicked():
	global answer

	if answer == "":
		answer = "3"
	else:
		answer += "3"

	ui.lineEdit_2.setText(answer)

# Кнопка 4
def b_4_clicked():
	global answer

	if answer == "":
		answer = "4"
	else:
		answer += "4"

	ui.lineEdit_2.setText(answer)

# Кнопка 5
def b_5_clicked():
	global answer

	if answer == "":
		answer = "5"
	else:
		answer += "5"

	ui.lineEdit_2.setText(answer)

# Кнопка 6
def b_6_clicked():
	global answer

	if answer == "":
		answer = "6"
	else:
		answer += "6"

	ui.lineEdit_2.setText(answer)

# Кнопка 7
def b_7_clicked():
	global answer

	if answer == "":
		answer = "7"
	else:
		answer += "7"

	ui.lineEdit_2.setText(answer)

# Кнопка 8
def b_8_clicked():
	global answer

	if answer == "":
		answer = "8"
	else:
		answer += "8"

	ui.lineEdit_2.setText(answer)

# Кнопка 9
def b_9_clicked():
	global answer

	if answer == "":
		answer = "9"
	else:
		answer += "9"

	ui.lineEdit_2.setText(answer)

# Плюс
def P():
	global answer
	global operation
	global oper_1

	operation = "P"
	oper_1 = answer
	answer = ""

	ui.lineEdit_2.setText(answer)

# Стереть
def C():
	global answer
	global oper_1

	oper_1 = ""
	answer = ""
	ui.lineEdit_2.setText(answer)

# Равно
def R():
	global answer
	global operation
	global oper_1
	global oper_2

	if operation == "P":
		oper_2 = answer
		answer = str(int(oper_1) + int(oper_2))

	ui.lineEdit_2.setText(answer)

# Процент
def PRO():
	pass

# Плюс/Минус
def PM():
	pass

# Минус
def M():
	pass

# Разделить
def D():
	pass

# Умножить
def X():
	pass

# Запятая
def Z():
	pass

# ---------Обработка нажатия кнопок действий--------

# Плюс	
ui.Button_P_2.clicked.connect(P)
# Равно
ui.Button_R_2.clicked.connect(R)
# Стереть
ui.Button_C_2.clicked.connect(C)
# Минус
ui.Button_M_2.clicked.connect(M)
# Умножить
ui.Button_X_2.clicked.connect(X)
# Плюс/Минус
ui.Button_PM_2.clicked.connect(PM)
# Процент
ui.Button_PRO_2.clicked.connect(PRO)
# Разделить
ui.Button_D_2.clicked.connect(D)
# Запятая
ui.Button_Z_2.clicked.connect(Z)

# ---------Обработка нажатия кнопок от 0 до 9-------

ui.Button_13.clicked.connect(b_0_clicked)#0
ui.Button_14.clicked.connect(b_1_clicked)#1
ui.Button_10.clicked.connect(b_2_clicked)#2
ui.Button_12.clicked.connect(b_3_clicked)#3
ui.Button_18.clicked.connect(b_6_clicked)#4
ui.Button_11.clicked.connect(b_5_clicked)#5
ui.Button_15.clicked.connect(b_4_clicked)#6
ui.Button_19.clicked.connect(b_7_clicked)#7
ui.Button_17.clicked.connect(b_8_clicked)#8
ui.Button_16.clicked.connect(b_9_clicked)#9


# Run main loop
sys.exit(app.exec_())

    
    
    
    

