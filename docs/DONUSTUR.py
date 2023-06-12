import os

try:
    os.system("python -m PyQt5.uic.pyuic -x downloadTool.ui -o ui_downloadTool.py")
    #☻os.system("pyrcc5 icons.qrc -o icons_rc.py")
except Exception as e:
    print(e)
    pass