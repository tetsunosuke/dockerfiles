# -*- coding: utf-8 -*-

import os
import glob
import subprocess
import shutil


"""
reports フォルダには　YYYY-MM-DD 形式のフォルダがあり、
その中には {従業員番号}_{氏名}_{YYYY-MM-DD}_{コース名}.xlsx
でレポートファイルが格納されている

これを、excelフォルダに、{従業員コード}_氏名_{YYYYMM} でフォルダを作成し、
その中にコピーする
"""

folders = glob.glob("report/*")
for folder in folders:
    files = glob.glob(folder + "/*.xlsx")
    for file in files:
        (f1, f2, f) = file.split("/")
        #print(file)
        tmp = f.split("_")
        (code, name, ymd) = tmp[:3]
        ymd = ymd.replace("-", "")
        path = "{}_{}_{}".format(code, name, ymd[0:6])

        # フォルダ作成
        new_path = "excel/" + path
        if not os.path.exists(new_path):
            os.mkdir(new_path)

        # そのフォルダにファイルをコピー
        shutil.copyfile(file, new_path + "/" + f)


"""
excel フォルダ以下にある 従業員コード_氏名_YYYYMM のフォルダの
配下にあるexlxファイルをすべて一度pdfファイルに変換し、
それらのPDFファイルをその人ごとに統合する
"""

# 下記を名前ぶん繰り返す

folders = glob.glob("excel/*")
for folder in folders:
    target = folder.split("/")[1]
    cmd = "/usr/bin/soffice --headless --nologo --nofirststartwizard  --convert-to pdf --outdir pdf/{} excel/{}/*".format(target, target)
    subprocess.call(cmd, shell=True)




    cmd ="pdftk pdf/{}/*.pdf cat output result/{}.pdf".format(target, target)
    subprocess.call(cmd, shell=True)
    #subprocess.run(cmd.split(" "))

# 全ファイル結合版も作成
cmd ="pdftk result/*.pdf cat output all.pdf"
subprocess.call(cmd, shell=True)

