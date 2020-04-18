

说明

  system:  windows/linux

  language:  python 3.8.6



function功能

The file of local disk  move/copy. When you use download software(such as xunlei,baidu),and there is no extra space on the disk, batch move files of the specified type to other hard disks,reserve file properties (such as modified time). It can also be used for file synchronization between two folders.

本地磁盘文件转移.当迅雷或者百度硬盘下载文件时候,磁盘没有多余空间时,批量移动指定类型的文件到其它硬盘。保存文件的属性(修改时间)。也可以用于两个文件夹之间的文件同步。

usage用法

  参数  源文件夹   目标文件夹   文件类型列表

 <source_directory>  <destination_directory> <type_list>

 example:      ./111   ./222 "txt,zip"

clone

git clone git@github.com:cnliving/tools_files_syn_py.git

