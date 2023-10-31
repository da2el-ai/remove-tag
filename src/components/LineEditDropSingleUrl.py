"""
ファイル1個しか許可しない1行入力
"""

from PySide6.QtGui import QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QLineEdit, QMessageBox

class LineEditDropSingleUrl(QLineEdit):
  def __init__(self, *args):
    super(LineEditDropSingleUrl, self).__init__(*args)
    self.setAcceptDrops(True)

  # -------------
  # ドラッグドロップの処理
  def dragEnterEvent(self, event:QDragEnterEvent):
    if(event.mimeData().hasUrls()):
      event.accept()


  def dropEvent(self, event:QDropEvent):
    if(not event.mimeData().hasUrls()):
      QMessageBox.warning(None, "Warning", "ファイル・フォルダーをドロップしてください")
      return

    urls = event.mimeData().urls()
    if(len(urls) >= 2):
      QMessageBox.warning(None, "Warning", "ドロップできるファイル・フォルダーは1個だけです")
      return

    self.setText(urls[0].toLocalFile())
