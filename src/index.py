import sys
from ppretty import ppretty
from PySide6.QtWidgets import QApplication
from modules.WindowControl import WindowControl


# モジュールではなくメインとして呼び出されたときに実行
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowControl()
    myWindow.show()
    sys.exit(app.exec())


