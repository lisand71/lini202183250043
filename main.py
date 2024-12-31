from frame.mainframe import MainFrame
from PyQt5.Qt import *
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainFrame = MainFrame()
    mainFrame.show()
    sys.exit(app.exec())