import os
import re
import shutil
import subprocess

file_path = "/media/tombo/Elements/webcam/JPEGImages_10"
split_num = 14
# file_path = "/media/tombo/Elements/webcam/test"
# split_num = 4
file_type = ".jpg"
split_file_name = "TC2018_0502"

files = os.listdir(file_path)# ファイルのリストを取得
n_files = 0# カウンタの初期化
for file in files:# ファイルの数だけループ
    #print(file)
    index = re.search(file_type, file)# 拡張子がjpgのものを検出
    #print(index)
    if index:# jpgの時だけ（今回の場合は）カウンタをカウントアップ
        n_files = n_files + 1

print(f"number of files: {n_files}")# ファイル数の表示
n_split_files = n_files//(split_num+1)
print(f"number of split files: {n_split_files}")
print("-"*10)

if((n_files%split_num)==0):
    for i in range(split_num):
        os.makedirs(f"{file_path}/{split_file_name}_{i:04d}",exist_ok=True)
else:
    for i in range(split_num+1):
        os.makedirs(f"{file_path}/{split_file_name}_{i:04d}",exist_ok=True)

dir_num = 0
split_files_num = 0
i = 0
for file in files:
    index = re.search('.jpg', file)# 拡張子がjpgのものを検出
    if index:# jpgの時だけ（今回の場合は）カウンタをカウントアップ
        #print(i)
        shutil.copy(f"{file_path}/{file}",f"{file_path}/{split_file_name}_{dir_num:04d}")
        split_files_num += 1
        #print(f"{file_path}/{file}:*****>{file_path}/split_{dir_num}")
        if((i+1)%n_split_files==0):
            dir_num+=1
            print(split_files_num)
            split_files_num = 0
        i += 1

print(split_files_num)


if((n_files%split_num)==0):
    for i in range(split_num):
        shutil.make_archive(f"{file_path}/{split_file_name}_{i:04d}","zip",f"{file_path}/{split_file_name}_{i:04d}")
else:
    for i in range(split_num+1):
        shutil.make_archive(f"{file_path}/{split_file_name}_{i:04d}","zip",f"{file_path}/{split_file_name}_{i:04d}")
