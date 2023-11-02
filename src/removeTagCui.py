import argparse
import sys
from modules.RemoveTagControl import RemoveTagControl

class RemoveTagCui:
  args = ''

  # -------------------
  # 初期化
  @classmethod
  def init(cls):
    # オプションの処理
    argps = argparse.ArgumentParser(description="キャプションからタグを除去")

    argps.add_argument('-rm', '--remove', type=str, help='削除タグ記述ファイルのパス', default='')
    argps.add_argument('-cp','--caption', type=str, help='キャプションファイルのパス', default='')
    argps.add_argument('-d', '--deep', action='store_true', help='下層フォルダも対象にする')
    argps.add_argument('-bk', '--backup', type=str, help='バックアップの拡張子', default='')

    cls.args = argps.parse_args()

    if(len(sys.argv) == 1):
      argps.print_help(sys.stderr)
      return False
    else:
      return True

  # -------------------
  # タグ削除実行
  @classmethod
  def startRemoveTag(cls):
    RemoveTagControl.removePath = cls.args.remove
    RemoveTagControl.captionPath = cls.args.caption
    RemoveTagControl.isDeep = cls.args.deep
    RemoveTagControl.backupExt = cls.args.backup

    # 事前準備の結果とエラーメッセージ
    result, message = RemoveTagControl.preparation()

    if(result):
      RemoveTagControl.removeTag()
      print("タグの削除が完了しました")
    else:
      print(message)


# モジュールではなくメインとして呼び出されたときに実行
if __name__ == "__main__":
  if(not RemoveTagCui.init()):
    sys.exit(1)
  else:
    RemoveTagCui.startRemoveTag()
