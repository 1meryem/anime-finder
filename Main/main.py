from PyQt5.QtCore import center
import requests
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtCore import *

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):

        self.text = QtWidgets.QLabel("Aramak istediğin animenin ismini gir.")
        self.text.setFont(QtGui.QFont("Arial",13))
        self.text.setStyleSheet("color : white;")
        self.line = QtWidgets.QLineEdit("Sword Art Online")
        self.buton = QtWidgets.QPushButton("Ara")
        self.wallpaper = QtWidgets.QLabel(self)
        self.wallpaper.setPixmap(QtGui.QPixmap("wall.jpg"))
        self.wallpaper.setGeometry(0,0,2500,1060)
        self.setWindowTitle("Anime Arayıcı | Türkanime")
        self.setWindowIcon(QtGui.QIcon("nekopara.jpg"))
        self.setGeometry(700,300,500,500)

        self.v_box = QtWidgets.QVBoxLayout()
        self.h_box = QtWidgets.QHBoxLayout()

        self.v_box.addStretch()
        self.v_box.addWidget(self.text)
        self.v_box.addWidget(self.line)
        self.v_box.addWidget(self.buton)
        self.v_box.addStretch()
        
        self.h_box.addStretch()
        self.h_box.addLayout(self.v_box)
        self.h_box.addStretch()

        self.setLayout(self.h_box)
        self.buton.clicked.connect(self.clicked)
        self.show()

    def clicked(self):
        signal = self.sender()
        if signal.text() == "Ara":
            if len(self.line.text()) < 3:
                self.text.setText("3 kelimeden büyük harf girin.")
                return
            data = self.line.text().replace(" ","-")

            anime_info = []
            i = 0
            url = f"https://www.turkanime.net/anime/{data}"
            response = requests.get(url)
            content = response.content
            soup = BeautifulSoup(content,"html.parser")

            anime_name = soup.find_all("td",{"style":"vertical-align: middle;","width":"70%"})

            for name in anime_name:
                i += 1
                if i == 13:
                    self.text.setText("\n\n".join(anime_info))
                    return
                else:
                    if i == 1:
                        anime_info.append(f"Kategori : {name.text}")
                    elif i == 2:
                        anime_info.append(f"Anime ismi : {name.text}")
                    elif i == 3:
                        anime_info.append(f"Japonca : {name.text}")
                    elif i == 4:
                        anime_info.append(f"Diğer Adları : {name.text}")
                    elif i == 5:
                        anime_info.append(f"Anime Türü : {name.text}")
                    elif i == 6:
                        anime_info.append(f"Bölüm Sayısı : {name.text}")
                    elif i == 7:
                        anime_info.append(f"Başlama Tarihi : {name.text}")
                    elif i == 8:
                        anime_info.append(f"Bitiş Tarihi : {name.text}")
                    elif i == 9:
                        anime_info.append(f"Yaş Sınırı : {name.text}")
                    elif i == 10:
                        anime_info.append(f"Yapımcı : {name.text}")
                    elif i == 11:
                        anime_info.append(f"Stüdyo : {name.text}")
                    elif i == 12:
                        anime_info.append(f"Bölüm Süresi : {name.text}")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    pencere = Window()
    app.exec_()
        