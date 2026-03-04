# 파일 복사 또는 이동
import os
import shutil

pwd = "/Users/admin/Desktop/초격자캠프/운영체제/EX01"
filenames = os.listdir(pwd)

for filename in filenames:
    if "tokyo" in filename:
        origin = os.path.join(pwd, filename)
        print(origin)
        # shutil.copy(origin, os.path.join(pwd, "copy.txt"))
        shutil.move(origin, os.path.join(pwd, "anony"))