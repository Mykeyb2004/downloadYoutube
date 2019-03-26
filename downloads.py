#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '1.0.0'
__author__ = '张奇进'

from pytube import YouTube
from pytube import Playlist


def load_file(filename):
    with open(filename, encoding='utf-8') as file:
        list = file.readlines()
    # 取消回车符
    for i, item in enumerate(list):
        list[i] = item.strip('\n')
    return list


if __name__ == '__main__':
    path = r'.\\video\\'  # 设置下载路径
    filename = 'list.txt'
    failed = [] # 记录下载失败的url
    
    # 载入url列表文件
    url_list = load_file(filename)
    print('载入文件', filename)
    print('载入url共计%d项。' % len(url_list))

    i = 0
    for url in url_list:
        i += 1
        try:
            print('Download: %s - [%s]. [%d/%d]' %
                  (url, YouTube(url).title, i, len(url_list)))
            yt = YouTube(url)
            yt.streams.first().download(path)  # 默认下载清晰度最高的视频
        except:
            failed.append(url)
    print("It's DONE!")
    
    if len(failed) > 0:
        print('Failed to save:')
        for item in failed:
            print(item)
            print(YouTube.title(item))
