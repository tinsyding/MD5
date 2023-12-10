import os
import random

def isVideo(filename):
    if filename.endswith('.mp4') or filename.endswith('.mkv') \
            or filename.endswith('.avi') or filename.endswith(".wmv") \
            or filename.endswith('.rm') or filename.endswith('.rmvb') \
            or filename.endswith('.flv') or filename.endswith('.mov') \
            or filename.endswith('.vob') or filename.endswith('.mpg') \
            or filename.endswith('.qt') or filename.endswith('.mpeg') \
            or filename.endswith('.wmp') or filename.endswith('.wm') \
            or filename.endswith('.asf') or filename.endswith('.ram') \
            or filename.endswith('.dat') or filename.endswith('.ifo') \
            or filename.endswith('.ogg') or filename.endswith('.3gp'):
        return True
    return False

def isPicture(filename):
    if filename.endswith('.bmp') or filename.endswith('.tif') \
            or filename.endswith('.gif') or filename.endswith(".png") \
            or filename.endswith('.jpg') or filename.endswith('.jpeg') \
            or filename.endswith('.icon') or filename.endswith('.webp') \
            or filename.endswith('.pcx') or filename.endswith('.tga') \
            or filename.endswith('.exif') or filename.endswith('.fpx') \
            or filename.endswith('.psd') or filename.endswith('.avif') \
            or filename.endswith('.raw') or filename.endswith('.ufo') \
            or filename.endswith('.dxf') or filename.endswith('.apng'):
        return True
    return False

def isMusic(filename):
    if filename.endswith('.cda') or filename.endswith('.mp3') \
            or filename.endswith('.flac') or filename.endswith(".wav") \
            or filename.endswith('.aac') or filename.endswith('.aiff') \
            or filename.endswith('.ogg') or filename.endswith('.oga') \
            or filename.endswith('.dts') or filename.endswith('.wv') \
            or filename.endswith('.au') or filename.endswith('.ape') \
            or filename.endswith('.m2a') or filename.endswith('.m4a') \
            or filename.endswith('.mid') or filename.endswith('.wma'):
        return True
    return False

def generate_random_str(randomlength):
  """
  生成一个指定长度的随机字符串
  """
  random_str = ''
  base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
  length = len(base_str) - 1
  for i in range(randomlength):
    random_str += base_str[random.randint(0, length)]
  return random_str

def bfs(rootDir,mode_num):
    global mymd5

    if mode_num == 1 :
        for root, dirs, files in os.walk(rootDir):
            for file in files:
                if isVideo(file):
                    with open(os.path.join(root, file), 'a') as f:
                        f.write(mymd5)
                        f.close()
                        print(file + "  Video Detected, md5 has been changed.")
                        global total_video_num
                        total_video_num = total_video_num + 1
            for dir in dirs:
                print(os.path.join(root,dir))

    if mode_num == 2 :
        for root, dirs, files in os.walk(rootDir):
            for file in files:
                if isMusic(file):
                    with open(os.path.join(root, file), 'a') as f:
                        f.write(mymd5)
                        f.close()
                        print(file + "  Music Detected, md5 has been changed.")
                        global total_music_num
                        total_music_num = total_music_num + 1
            for dir in dirs:
                print(os.path.join(root,dir))

    if mode_num == 3 :
        for root, dirs, files in os.walk(rootDir):
            for file in files:
                if isPicture(file):
                    with open(os.path.join(root, file), 'a') as f:
                        f.write(mymd5)
                        f.close()
                        print(file + "  Picture Detected, md5 has been changed.")
                        global total_pic_num
                        total_pic_num = total_pic_num + 1
            for dir in dirs:
                print(os.path.join(root,dir))

    if mode_num == 4 :
        for root, dirs, files in os.walk(rootDir):
            for file in files:
                if True:
                    with open(os.path.join(root, file), 'a') as f:
                        f.write(mymd5)
                        f.close()
                        print(file + " md5 has been changed.")
                        global total_file_num
                        total_file_num = total_file_num + 1
            for dir in dirs:
                print(os.path.join(root,dir))


total_video_num = 0
total_pic_num = 0
total_music_num = 0
total_file_num = 0
mode_num = 0
mymd5 = ""

print("MD5批量修改助手")

while True:
    total_video_num = 0
    total_pic_num = 0
    total_music_num = 0
    total_file_num = 0
    mode_num = 0
    mymd5 = generate_random_str(3)

    print("请输入要批量修改的文件夹路径：")
    DIRPATH = input()
    
    print("请输入模式，1为修改所有视频文件，2为修改所有音频文件，3是修改所有图片文件，4是修改所有文件")
    mode_num = input()

    print(DIRPATH)
    bfs(DIRPATH,int(mode_num))

    print("Task Done!\n")
    if mode_num == '1':
        print('Successfully modified the md5 value of a total of ' + str(total_video_num) + ' videos')
    elif mode_num == '2':
        print('Successfully modified the md5 value of a total of ' + str(total_music_num) + ' music')
    elif mode_num == '3':
        print('Successfully modified the md5 value of a total of ' + str(total_pic_num) + ' pictures')
    else:
        print('Successfully modified the md5 value of a total of ' + str(total_file_num) + ' files')
