import hashlib
import os
from datetime import datetime

def get_md5_for_file(filename):
    """计算并返回文件的MD5哈希值"""
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def get_md5_for_string(s):
    """计算并返回字符串的MD5哈希值"""
    return hashlib.md5(s.encode()).hexdigest()

def print_and_save_md5_for_directory(directory, prefix='', file_handle=None):
    """以目录树样式打印并保存文件夹内所有文件的MD5值"""
    files = os.listdir(directory)
    files.sort()  # 确保顺序一致
    for i, file in enumerate(files):
        path = os.path.join(directory, file)
        if os.path.isdir(path):
            new_prefix = prefix + ("├── " if i < len(files) - 1 else "└── ")
            line = f"{prefix}{('├──' if i < len(files) - 1 else '└──')} {file}/"
            print(line)
            if file_handle:
                file_handle.write(line + '\n')
            print_and_save_md5_for_directory(path, prefix + ("│   " if i < len(files) - 1 else "    "), file_handle)
        else:
            md5_value = get_md5_for_file(path)
            line = f"{prefix}{('├──' if i < len(files) - 1 else '└──')} {file}: {md5_value}"
            print(line)
            if file_handle:
                file_handle.write(line + '\n')

def main():
    """主函数"""
    input_value = input("请输入文件路径、文件夹路径或字符串: ").strip("\"")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open('out.txt', 'a', encoding='utf-8') as out_file:
        out_file.write(f"\n查询时间: {current_time}\n")
        if os.path.isfile(input_value):
            md5_value = get_md5_for_file(input_value)
            line = f"'{input_value}'的MD5值是：{md5_value}"
            print(line)
            out_file.write(line + '\n')
        elif os.path.isdir(input_value):
            line = f"'{input_value}'文件夹内的文件MD5值是："
            print(line)
            out_file.write(line + '\n')
            print_and_save_md5_for_directory(input_value, file_handle=out_file)
        else:
            md5_value = get_md5_for_string(input_value)
            line = f"'{input_value}'的MD5值是：{md5_value}"
            print(line)
            out_file.write(line + '\n')

if __name__ == "__main__":
    main()
