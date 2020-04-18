#!/bin/python
#-*- encoding=utf-8 -*-
#date 2020-04-17
# author  dingjianmin
#递归拷贝指定类型的文件
#参数  源文件夹   目标文件夹   文件类型列表
# <source_directory>  <dest_directory> <type_list>

import sys
import os
import shutil

def  make_directory(directory_s):
    try:
        os.mkdir(directory_s)
    except:
        pass

class CopyEx:
    #True  is move   other  is copy
    ismove=True
    #the list of  file type
    dict_types = {}
    def copy_file_ex(self,srcFile,dstFile):
        stat_1 =None
        st_mtime_2 = 0
        try:
            stat_1 = os.stat(srcFile)
        except:
            #获取原始文件失败
            return
        try:
            stat_2 = os.stat(dstFile)
            st_mtime_2 = stat_2.st_mtime
        except:
            pass
        if st_mtime_2 >= stat_1.st_mtime:
            if True == self.ismove :
                shutil.rmtree(srcFile)
            return
        if True == self.ismove:
            shutil.move(srcFile, dstFile)
            print("move file=%s" % (srcFile))
        else:
            shutil.copy(srcFile, dstFile)
            print("copy file=%s" % (srcFile))
            os.utime(dstFile, (stat_1.st_atime, stat_1.st_mtime))

    def deal(self,src,dst):
        for file in os.listdir(src):
            srcFile = os.path.join(src, file)
            dstFile=os.path.join(dst, file)
            if os.path.isdir(srcFile):
                print("dir=%s"%srcFile)
                stat_dir=os.stat(srcFile)
                make_directory(dstFile)
                self.deal(srcFile,dstFile)
                os.utime(dstFile,(stat_dir.st_atime,stat_dir.st_mtime))
                continue
            if len(self.dict_types)==0:
                self.copy_file_ex(srcFile,dstFile)
            pos=file.rfind(".")
            sf=""
            if -1!=pos:
                sf=file[pos+1:]
            if self.dict_types.get(sf) :
                self.copy_file_ex(srcFile, dstFile)
            else :
                print("skip suffix=%s, name=%s, file=%s" % (sf,file, srcFile))

if __name__ == "__main__" :
    args=sys.argv
    if len(args)<3 :
        print("invalid parameter  \n grammer <program> <source_directory> dest_directory \n "
              "eg   ./source_directory   ./dest_directory   txt,zip")
        sys.exit(0)
    s_types=args[3].split(",")
    cpx = CopyEx()
    cpx.ismove = True
    cpx.dict_types = {}
    for ty in  s_types :
        cpx.dict_types[ty]=1
    dst=args[2]
    if True!=os.path.exists(dst) :
        str_in=input("destination is not exist create[y/n]:")
        if "y"!=str_in.lower():
            sys.exit(0)
        os.mkdir(dst)
    cpx.deal(args[1],args[2])
    #s1 = "txt"
    #print("txt_find=",cpx.dict_types[s1])

