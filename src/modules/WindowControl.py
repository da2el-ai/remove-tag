import os
import glob
from ppretty import ppretty
from PySide6.QtCore import Qt
from PySide6.QtGui import QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QDialog, QMessageBox
from components.mainWindow import Ui_Dialog
from modules.TagManage import TagManage
from modules.RemoveTagControl import RemoveTagControl

class WindowControl(QDialog):

  # removePath = ''
  # captionPath = ''
  # isDeep = False
  # backupExt = ''

  def __init__(self, parent=None):
    super(WindowControl, self).__init__(parent)
    self.ui = Ui_Dialog()
    self.ui.setupUi(self)
    self.setWindowTitle("RemoveTag")
    self.setAcceptDrops(True)

    # UIのアクション定義
    self.ui.btnStart.clicked.connect(self.startRemoveTag)


  # -------------
  # スタートボタンを押した
  def startRemoveTag(self):
    RemoveTagControl.removePath = self.ui.inputRemovePath.text()
    RemoveTagControl.captionPath = self.ui.inputCaptionPath.text()
    RemoveTagControl.isDeep = True if self.ui.checkDeep.checkState() == Qt.Checked else False
    RemoveTagControl.backupExt = self.ui.inputBackupExt.text()

    # 事前準備の結果とエラーメッセージ
    result, message = RemoveTagControl.preparation()

    if(result):
      RemoveTagControl.removeTag()
      QMessageBox.information(None, "通知", "タグの削除が完了しました")
    else:
      QMessageBox.warning(None, "Warning", message)



  # # --------------
  # # 変換前の準備
  # def preparation(self):

  #   # 削除対象タグファイルを読む
  #   if(not TagManage.readRemoveList(self.removePath)):
  #     QMessageBox.warning(None, "Warning", "削除タグ記述ファイルのパスが存在しません")
  #     return False

  #   # キャプションフォルダの存在チェック
  #   if(not os.path.isdir(self.captionPath)):
  #     QMessageBox.warning(None, "Warning", "キャプションフォルダが存在しません")
  #     return False

  #   # glob用にパス区切りを変更
  #   self.captionPath = self.captionPath.replace(os.sep,'/')

  #   # 下層も処理するか
  #   if(self.isDeep):
  #     self.captionPath = self.captionPath + "/**/*.txt"
  #   else:
  #     self.captionPath = self.captionPath + "/*.txt"

  #   return True


  # # ---------------
  # # 変換を実行
  # def removeTag(self):
  #   # タグファイルを開く
  #   for filePath in glob.glob(self.captionPath):
  #       # print("\n" + filePath + "\n")
  #       tags = TagManage.fileToList(filePath)
  #       removedTags = TagManage.removeTag(tags)

  #       # バックアップファイルを作成
  #       if(len(self.backupExt) >= 1):
  #         self.createBackup(filePath)

  #       # 削除後を保存
  #       tagFile = open(filePath, "w")
  #       tagFile.write(",".join(removedTags))
  #       tagFile.close()
  #       # print(",".join(removedTags))


  # # -----------------
  # # バックアップファイルを作成
  # def createBackup(self, filePath):
  #   os.rename(filePath, filePath + '.' + self.backupExt)
