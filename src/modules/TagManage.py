# タグの操作

import re
import os

class TagManage:
  # 削除対象タグ
  removeTags = []

  # ---------------
  # 除外タグに一致しないものを書き出す
  @classmethod
  def removeTag(cls, list):
    newList = []

    for tag in list:
        if not tag in cls.removeTags:
            newList.append(tag)

    return newList


  # ---------------
  # 削除対象キーワードデータを読み込む　
  # ファイルが存在しなければ False を返す
  # 存在するなら読み込んだ後に True を返す
  @classmethod
  def readRemoveList(cls, filePath):
    if(not os.path.isfile(filePath)):
      return False

    cls.removeTags = cls.fileToList(filePath)
    return True


  # ---------------
  # カンマと改行で分割してリスト化
  @classmethod
  def fileToList(cls, filePath):
    with open(filePath, "r") as f:
      list = re.split(" *[,\n]+ *", f.read())

    return list
