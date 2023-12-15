import hashlib
import os

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

def print_md5_for_directory(directory, prefix=''):
    """以目录树样式打印文件夹内所有文件的MD5值"""
    files = os.listdir(directory)
    files.sort()  # 确保顺序一致
    for i, file in enumerate(files):
        path = os.path.join(directory, file)
        if os.path.isdir(path):
            new_prefix = prefix + ("├── " if i < len(files) - 1 else "└── ")
            print(f"{prefix}{('├──' if i < len(files) - 1 else '└──')} {file}/")
            print_md5_for_directory(path, prefix + ("│   " if i < len(files) - 1 else "    "))
        else:
            md5_value = get_md5_for_file(path)
            print(f"{prefix}{('├──' if i < len(files) - 1 else '└──')} {file}: {md5_value}")

def main():
    """主函数"""
    input_value = input("请输入文件路径、文件夹路径或字符串: ").strip("\"")

    if os.path.isfile(input_value):
        md5_value = get_md5_for_file(input_value)
        print(f"'{input_value}'的MD5值是：{md5_value}")
    elif os.path.isdir(input_value):
        print(f"'{input_value}'文件夹内的文件MD5值是：")
        print_md5_for_directory(input_value)
    else:
        md5_value = get_md5_for_string(input_value)
        print(f"'{input_value}'的MD5值是：{md5_value}")

if __name__ == "__main__":
    main()
