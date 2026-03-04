# 경로와 확장자 이용해 파일 찾고, 내용 읽기

import os

def serrchFile(dirname, extension):
    filenames = os.listdir(dirname)
    for filename in filenames:
        filepath = os.path.join(dirname, filename)
        if os.path.isdir(filepath):
            serrchFile(filepath, extension)
        elif os.path.isfile(filepath):
            name, ext = os.path.splitext(filepath)
            if ext == extension:
                with open(filepath, "r", encoding="utf-8") as f:
                    print(f.read())

serrchFile("/Users/admin/Desktop/초격자캠프/운영체제/EX01", ".js")