import socket
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from socket_practice.student_information_management_system.mwin import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.delete_buttion.clicked.connect(self.on_clicked_deleted_button)
        self.socket = socket.socket()
        self.socket.connect(('10.3.19.118', 8888))

    def on_clicked_deleted_button(self):
        deleted_id = self.deleted_id.text()
        message = '4 ' + deleted_id
        if deleted_id:
            self.socket.sendall(message.encode('utf-8'))
            data = self.socket.recv(1024).decode("utf-8")
            if data == 1:
                self.result.setPlainText("删除成功")
            else:
                self.result.setPlainText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
