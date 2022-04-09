#создай тут фоторедактор Easy Editor!
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QLineEdit, QPushButton, QListWidget, QLabel, QHBoxLayout, QVBoxLayout, QFileDialog
import os
from PIL import Image, ImageFilter
from PyQt5.QtGui import QPixmap

programfile = QApplication([])
window = QWidget()


window.setWindowTitle('PhotoEditor')
window.resize(700,500)

btn1 = QPushButton('Папка')
spisok = QListWidget()
btn2 = QPushButton('Лево')
btn3 = QPushButton('Право')
btn4 = QPushButton('Зеркало')
btn5 = QPushButton('Резкость')
btn6 = QPushButton('Ч/Б')
pict = QLabel('')

hfull = QHBoxLayout()
v1 = QVBoxLayout()
v2 = QVBoxLayout()
h1 = QHBoxLayout()

v1.addWidget(btn1)
v1.addWidget(spisok)
v2.addWidget(pict)
h1.addWidget(btn2)
h1.addWidget(btn3)
h1.addWidget(btn4)
h1.addWidget(btn5)
h1.addWidget(btn6)

v2.addLayout(h1)
hfull.addLayout(v1)
hfull.addLayout(v2)

#def filemanager():
#    try:
#        global workdir
#        workdir = QFileDialog.getExistingDirectory()
#        files = os.listdir(workdir)
#    except:
#        print('Ошибка "Explorer"')

def a():
    print('лево')
def b():
    print('Право')
def c():
    print('Зеркало')
def d():
    print('Резкость')
def f():
    print('Ч/Б')
def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result
def showFiles():
    try:
        extensions = ['.jpg', '.png', '.jpeg', '.bmp', '.gif']
        global workdir
        workdir = QFileDialog.getExistingDirectory()
        filenames = filter(os.listdir(workdir), extensions)
        spisok.clear()
        spisok.addItems(filenames)
    except:
        pass

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"
    
    def loadImage(self, dir, filename):
        ''' при загрузке запоминаем путь и имя файла '''
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)
    
    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
    
    def saveImage(self):
        ''' сохраняет копию файла в подпапке '''
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
    
    def showImage(self, path):
        pict.hide()
        pixmapimage = QPixmap(path)
        w, h = pict.width(), pict.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        pict.setPixmap(pixmapimage)
        pict.show()

def showPicture():
    if spisok.currentRow() >= 0:
       filename = spisok.currentItem().text()
       workimage.loadImage(workdir, filename)
       image_path = os.path.join(workimage.dir, workimage.filename)
       workimage.showImage(image_path)

workimage = ImageProcessor()
window.setLayout(hfull)

btn1.clicked.connect(showFiles)
btn2.clicked.connect(a)
btn3.clicked.connect(b)
btn4.clicked.connect(c)
btn5.clicked.connect(d)
btn6.clicked.connect(f)
spisok.currentRowChanged.connect(showPicture)





window.show()
programfile.exec_()