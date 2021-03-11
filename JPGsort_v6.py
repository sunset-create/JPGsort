# フォルダを指定すると、フォルダ内の写真、動画ファイルを更新日毎のフォルダを作成して整理するプログラム
# 関数を使用

import glob, os, time, shutil, os.path
from tkinter import filedialog

# ダイアログを開き作業ディレクトリを選択
dir = "C:/Users/harry/PycharmProjects"
fld = filedialog.askdirectory(initialdir = dir)
os.chdir(fld)


def file_sort(files):
    for i, photo_name in enumerate(files):
        j = 0
    # ファイルの更新日時を得る --- (*3)
        t = os.path.getmtime(photo_name)
        ts = time.strftime("%Y%m%d", time.localtime(t))
        For_fn = time.strftime("%Y%m%d"'_'"%H%M%S", time.localtime(t))
        r, e = os.path.splitext(photo_name)
    # 更新日時のディレクトリを作成 --- (*4)
        os.makedirs(ts, exist_ok=True)
    # 作成したディレクトリへ写真ファイルを移動 --- (*5)
        new_name = For_fn + e
        os.rename(photo_name, new_name)
        curdir = fld + '/' + ts + '/' + new_name
        if os.path.exists(curdir):
            new_name2 =  '{}({}){}'.format(new_name, j, e)
            os.rename(new_name, new_name2)
            shutil.move(new_name2, ts)
            j = j + 1
            print(ts)

        else:
            shutil.move(new_name, ts)
            print(ts)

# jpgを処理
files = glob.glob("*.jpg")
file_sort(files)

# HEICを処理
files = glob.glob("*.HEIC")
file_sort(files)

# mp4を処理
files = glob.glob("*.mp4")
file_sort(files)

# aviを処理
files = glob.glob("*.avi")
file_sort(files)