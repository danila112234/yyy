import pygame
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Shrek(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, -40, 1411, 871))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("шрек.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 70, 291, 61))
        self.label_2.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: white;\n"
"background-color: #000000;\n"
"border-radius:30")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 490, 211, 81))
        self.pushButton.setStyleSheet("font: 87 14pt \"Arial Black\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "СРАВНИ СО СВОИМ РИСУНКОМ"))
        self.pushButton.setText(_translate("MainWindow", "Выйти"))


class Fighter(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-350, -100, 1181, 761))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("имперский штурмовик.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 20, 291, 61))
        self.label_2.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: white;\n"
"background-color: #000000;\n"
"border-radius:30")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 490, 211, 81))
        self.pushButton.setStyleSheet("font: 87 14pt \"Arial Black\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "СРАВНИ СО СВОИМ РИСУНКОМ"))
        self.pushButton.setText(_translate("MainWindow", "Выйти"))


class Anonimus(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 692)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, -10, 1411, 691))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("anonimus.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 20, 291, 61))
        self.label_2.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: white;\n"
"background-color: #000000;\n"
"border-radius:30")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 590, 211, 81))
        self.pushButton.setStyleSheet("font: 87 14pt \"Arial Black\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "СРАВНИ СО СВОИМ РИСУНКОМ"))
        self.pushButton.setText(_translate("MainWindow", "Выйти"))


class Start(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 617)
        MainWindow.setStyleSheet("background-color: #22222e ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 500, 211, 51))
        self.pushButton.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"font: 87 10pt \"Arial Black\";\n"
"color: white")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-20, 0, 841, 111))
        self.label.setStyleSheet("font: 87 20pt \"Arial Black\";\n"
"color: white;\n"
"background-color: black")
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(170, 260, 481, 61))
        self.radioButton.setStyleSheet("font: 87 20pt \"Arial Black\";\n"
"color: white;\n"
"background-color: black;\n"
"border-radius:30")
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(170, 150, 481, 61))
        self.radioButton_2.setStyleSheet("font: 87 20pt \"Arial Black\";\n"
"color: white;\n"
"background-color: black;\n"
"border-radius:30\n"
"")
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup_2.addButton(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(170, 370, 481, 61))
        self.radioButton_3.setStyleSheet("font: 87 20pt \"Arial Black\";\n"
"color: white;\n"
"background-color: black;\n"
"border-radius:30")
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup_2.addButton(self.radioButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Рисовать"))
        self.label.setText(_translate("MainWindow", "    Можете попытаться нарисовать одну из картинок:"))
        self.radioButton.setText(_translate("MainWindow", "Шрек(lvl.2)"))
        self.radioButton_2.setText(_translate("MainWindow", "Имперский штурмовик(lvl.1)"))
        self.radioButton_3.setText(_translate("MainWindow", "Анонимус(lvl.3)"))


class Palitra(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(399, 240)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #22222e")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 75, 23))
        self.pushButton.setStyleSheet("background-color: #ff0000;\n"
"font: 87 8pt \"Arial Black\";\n""")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 20, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: #00ff00;\n"
"font: 87 8pt \"Arial Black\";\n")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 20, 75, 23))
        self.pushButton_3.setStyleSheet("background-color: #0000ff ;\n"
"font: 87 8pt \"Arial Black\";\n")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 100, 75, 23))
        self.pushButton_4.setStyleSheet("background-color: #ffffff;\n"
"font: 87 8pt \"Arial Black\";\n")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 100, 91, 23))
        self.pushButton_5.setStyleSheet("background-color: #A52A2A;\n"
"font: 87 8pt \"Arial Black\";\n")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 100, 91, 23))
        self.pushButton_6.setStyleSheet("background-color: #9400D3;\n"
"font: 87 8pt \"Arial Black\";\n")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(24, 170, 81, 23))
        self.pushButton_7.setStyleSheet("background-color: #808080;\n"
"font: 87 8pt \"Arial Black\";\n")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(170, 170, 75, 23))
        self.pushButton_8.setStyleSheet("background-color: #FFFF00;\n"
"font: 87 8pt \"Arial Black\";\n")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(300, 170, 75, 23))
        self.pushButton_9.setStyleSheet("background-color: #ffffff;\n"
"font: 87 8pt \"Arial Black\";\n")
        self.pushButton_9.setObjectName("pushButton_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "красный"))
        self.pushButton_2.setText(_translate("MainWindow", "зеленый"))
        self.pushButton_3.setText(_translate("MainWindow", "синий"))
        self.pushButton_4.setText(_translate("MainWindow", "белый"))
        self.pushButton_5.setText(_translate("MainWindow", "коричневый"))
        self.pushButton_6.setText(_translate("MainWindow", "фиолетовый"))
        self.pushButton_7.setText(_translate("MainWindow", "серый"))
        self.pushButton_8.setText(_translate("MainWindow", "желтый"))
        self.pushButton_9.setText(_translate("MainWindow", "ЛАСТИК"))


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        def load_image(name, colorkey=None):
            if not os.path.isfile(name):
                print(f"Файл с изображением '{name}' не найден")
                sys.exit()
            image = pygame.image.load(name)
            if colorkey is not None:
                image = image.convert()
                if colorkey == -1:
                    colorkey = image.get_at((0, 0))
                image.set_colorkey(colorkey)
            else:
                image = image.convert_alpha()
            return image

        self.image = pygame.Surface((50, 50))
        img = load_image('кисточка.webp', -1)
        self.image = img
        self.image = pygame.transform.scale(img, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)

    def update(self, x, y):
        self.rect.x = x
        self. rect.y = y


class The_first_window(QMainWindow, Start):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.go)

    def go(self):
        self.close()
        a = self.buttonGroup_2.checkedButton().text()
        h = open('клетки.txt', 'w', encoding='utf-8')
        h.write(a)
        h.close()
        board = Board(35, 35)
        size = 1011, 1011
        screen = pygame.display.set_mode(size)

        all_sprites = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)

        drawing = False
        running = True

        k = 0
        d = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    board.get_click(event.pos)
                    drawing = True
                if event.type == pygame.MOUSEBUTTONUP:
                    drawing = False
                if event.type == pygame.MOUSEMOTION:
                    x = int(event.pos[0])
                    y = int(event.pos[1])
                    all_sprites.update(x, y)
                    if drawing:
                        board.get_click(event.pos)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_2:
                        k += 1
                    if event.key == pygame.K_1:
                        board = Board(35, 35)
                    if event.key == pygame.K_3:
                        if d:
                            ex2 = The_second_window()
                            ex2.show()
                            d = False
                        else:
                            ex2.hide()
                            d = True
                    if event.key == pygame.K_TAB:
                        h = open('клетки.txt', 'r', encoding='utf-8')
                        a = h.read()
                        h.close()
                        if a == 'Имперский штурмовик(lvl.1)':
                            ex3 = lvl_1()
                        elif a == "Шрек(lvl.2)":
                            ex3 = lvl_2()
                        else:
                            ex3 = lvl_3()
                        ex3.show()

            board.render(screen, k)
            all_sprites.draw(screen)
            pygame.display.flip()
        pygame.quit()


class The_second_window(QMainWindow, Palitra):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedWidth(400)
        self.setFixedHeight(230)
        self.pushButton.clicked.connect(self.chuse)
        self.pushButton_2.clicked.connect(self.chuse)
        self.pushButton_3.clicked.connect(self.chuse)
        self.pushButton_4.clicked.connect(self.chuse)
        self.pushButton_5.clicked.connect(self.chuse)
        self.pushButton_6.clicked.connect(self.chuse)
        self.pushButton_7.clicked.connect(self.chuse)
        self.pushButton_8.clicked.connect(self.chuse)
        self.pushButton_9.clicked.connect(self.chuse)

    def chuse(self):
        k = {'красный': 'red', 'зеленый': 'green', 'синий': 'blue', 'белый': 'white', 'коричневый': 'brown',
             'фиолетовый': 'purple', 'серый': 'gray', 'желтый': 'yellow', 'ЛАСТИК': 'black'}
        a = k[self.sender().text()]
        h = open('цвет.txt', 'w', encoding='utf-8')
        h.write(a)
        h.close()


class lvl_1(QMainWindow, Fighter):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.go)

    def go(self):
        self.close()


class lvl_2(QMainWindow, Shrek):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.go)

    def go(self):
        self.close()


class lvl_3(QMainWindow, Anonimus):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.go)

    def go(self):
        self.close()


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen, k=0):

        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] != 0:
                    color = self.board[row][col]
                else:
                    color = pygame.Color((0, 0, 0))
                if k % 2:
                    pygame.draw.rect(screen, color, (
                        col * self.cell_size + self.left, row * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 0)
                    pygame.draw.rect(screen, (255, 255, 255), (
                        col * self.cell_size + self.left, row * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 1)
                else:
                    pygame.draw.rect(screen, color, (
                        col * self.cell_size + self.left, row * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 0)

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if 0 <= cell_x < self.width and 0 <= cell_y < self.height:
            return cell_x, cell_y
        return None

    def on_click(self, cell):
        h = open('цвет.txt', 'r', encoding='utf-8')
        a = h.read()
        h.close()
        self.board[cell[1]][cell[0]] = a

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = The_first_window()
    ex.show()
    sys.exit(app.exec_())
