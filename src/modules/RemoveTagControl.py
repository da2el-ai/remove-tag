import os
import glob
from ppretty import ppretty
from modules.TagManage import TagManage


class RemoveTagControl:
  removePath = ''
  captionPath = ''
  isDeep = False
  backupExt = ''


  # --------------
  # 変換前の準備
  @classmethod
  def preparation(cls):

    # 削除対象タグファイルを読む
    if(not TagManage.readRemoveList(cls.removePath) or len(cls.removePath) < 1):
      return False, "削除タグ記述ファイルのパスが存在しません"

    # キャプションフォルダの存在チェック
    if(not os.path.isdir(cls.captionPath) or len(cls.captionPath) < 1):
      return False, "キャプションフォルダが存在しません"

    # glob用にパス区切りを変更
    cls.captionPath = cls.captionPath.replace(os.sep,'/')

    # 下層も処理するか
    if(cls.isDeep):
      cls.captionPath = cls.captionPath + "/**/*.txt"
    else:
      cls.captionPath = cls.captionPath + "/*.txt"

    return True, ""


  # ---------------
  # 変換を実行
  @classmethod
  def removeTag(cls):
    # タグファイルを開く
    for filePath in glob.glob(cls.captionPath):
        # print("\n" + filePath + "\n")
        tags = TagManage.fileToList(filePath)
        removedTags = TagManage.removeTag(tags)

        # バックアップファイルを作成
        if(len(cls.backupExt) >= 1):
          cls.createBackup(filePath)

        # 削除後を保存
        tagFile = open(filePath, "w")
        tagFile.write(",".join(removedTags))
        tagFile.close()
        # print(",".join(removedTags))


  # -----------------
  # バックアップファイルを作成
  @classmethod
  def createBackup(cls, filePath):
    backupFilePath = filePath + '.' + cls.backupExt

    if(os.path.isfile(backupFilePath)):
      os.remove(backupFilePath)

    os.rename(filePath, backupFilePath)
