# -*- coding: utf-8 -*-

import os
import glob
import subprocess
import shutil
import re


"""
report フォルダには　YYYY-MM-DD 形式のフォルダがあり、
その中には {従業員番号}_{氏名}_{YYYY-MM-DD}_{コース名}.xlsx
でレポートファイルが格納されている

これを、resourceフォルダに、{従業員コード}_氏名_{YYYYMM} でフォルダを作成し、
その中にコピーする
"""

folders = glob.glob("report/*")
for folder in folders:
    files = glob.glob(folder + "/*")
    for file in files:
        if not re.search('\.(xlsx|docx)$', file):
            continue
        (f1, f2, f) = file.split("/")
        #print(file)
        tmp = f.split("_")
        (code, name, ymd) = tmp[:3]
        ymd = ymd.replace("-", "")
        path = "{}_{}_{}".format(code, name, ymd[0:6])

        # フォルダ作成
        new_path = "resource/" + path
        if not os.path.exists(new_path):
            os.mkdir(new_path)

        # そのフォルダにファイルをコピー（上書き）
        shutil.copyfile(file, new_path + "/" + f)

"""
resource フォルダ以下にある 従業員コード_氏名_YYYYMM のフォルダの
配下にあるファイルをすべて一度pdfファイルに変換し、
それらのPDFファイルをその人ごとに統合する
"""

# 下記を名前ぶん繰り返す

folders = glob.glob("resource/*")
for folder in folders:
    target = folder.split("/")[1]
    cmd = "/usr/bin/soffice --headless --nologo --nofirststartwizard  --convert-to pdf --outdir pdf/{} resource/{}/*".format(target, target)
    subprocess.call(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    cmd ="pdftk pdf/{}/*.pdf cat output result/{}.pdf".format(target, target)
    subprocess.call(cmd, shell=True)


# 20000 台のものをpll、残りをpcとして分割
files = glob.glob("result/*.pdf")
pc = []
pll = []
for f in files:
    if re.match(r'result/2[0-9]{4}', f):
        pll.append(f)
    else:
        pc.append(f)
cmd ="pdftk {} cat output pll.pdf".format(" ".join(pll))
subprocess.call(cmd, shell=True)
cmd ="pdftk {} cat output pc.pdf".format(" ".join(pc))
subprocess.call(cmd, shell=True)
 

# 全ファイル結合版も作成
cmd ="pdftk  pll.pdf pc.pdf cat output all.pdf"
subprocess.call(cmd, shell=True)

