import os
import random
import logging

# 设置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_file_type(filename, extensions):
    """
    检查文件是否是指定类型。
    """
    return any(filename.endswith(ext) for ext in extensions)

def generate_random_str(length=32):
    """
    生成指定长度的随机字符串。
    """
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(base_str) for _ in range(length))

def modify_file_md5(file_path, random_str):
    """
    修改文件的MD5。
    """
    try:
        with open(file_path, 'a') as f:
            f.write(random_str)
        logging.info(f"MD5 modified: {file_path}")
    except Exception as e:
        logging.error(f"Error modifying {file_path}: {e}")

def batch_modify_md5(root_dir, mode_num):
    """
    批量修改文件MD5。
    """
    extensions = {
        1: ['.mp4', '.mkv', '.avi', '.wmv', '.rm', '.rmvb', '.flv', '.mov', '.vob', '.mpg', '.qt', '.mpeg', '.wmp', '.wm', '.asf', '.ram', '.dat', '.ifo', '.ogg', '.3gp'],  # 视频文件
        2: ['.cda', '.mp3', '.flac', '.wav', '.aac', '.aiff', '.ogg', '.oga', '.dts', '.wv', '.au', '.ape', '.m2a', '.m4a', '.mid', '.wma'],  # 音乐文件
        3: ['.bmp', '.tif', '.gif', '.png', '.jpg', '.jpeg', '.icon', '.webp', '.pcx', '.tga', '.exif', '.fpx', '.psd', '.avif', '.raw', '.ufo', '.dxf', '.apng']  # 图片文件
    }

    file_count = 0
    random_str = generate_random_str()

    for root, _, files in os.walk(root_dir):
        for file in files:
            if mode_num == 4 or is_file_type(file, extensions.get(mode_num, [])):
                modify_file_md5(os.path.join(root, file), random_str)
                file_count += 1

    logging.info(f"Total files modified: {file_count}")

def main():
    """
    主函数。
    """
    print("MD5批量修改助手")
    dir_path = input("请输入要批量修改的文件夹路径：")
    mode_num = int(input("请输入模式，1为修改所有视频文件，2为修改所有音频文件，3为修改所有图片文件，4为修改所有文件："))
    batch_modify_md5(dir_path, mode_num)
    print("任务完成！")

if __name__ == "__main__":
    main()
