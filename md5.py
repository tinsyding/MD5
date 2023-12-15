import hashlib
import os

def get_md5_for_file(filename):
    """计算并返回文件的MD5哈希值"""
    hash_md5 = hashlib.md5()
    try:
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except FileNotFoundError:
        return None

def get_md5_for_string(s):
    """计算并返回字符串的MD5哈希值"""
    return hashlib.md5(s.encode()).hexdigest()

def print_md5_for_directory(directory, prefix=''):
    """以目录树样式打印文件夹内所有文件的MD5值"""
    if not os.path.isdir(directory):
        print("文件夹未找到或为空")
        return

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
    print("选择MD5计算类型：")
    print("1. 文件")
    print("2. 字符串")
    print("3. 文件夹")
    choice = input("请输入选项（1, 2或3）: ")

    if choice == '1':
        file_path = input("请输入文件路径: ").strip("\"")
        md5_value = get_md5_for_file(file_path)
        if md5_value:
            print(f"'{file_path}'的MD5值是：{md5_value}")
        else:
            print("文件未找到")
    elif choice == '2':
        text = input("请输入字符串: ")
        md5_value = get_md5_for_string(text)
        print(f"'{text}'的MD5值是：{md5_value}")
    elif choice == '3':
        directory_path = input("请输入文件夹路径: ").strip("\"")
        print(f"'{directory_path}'文件夹内的文件MD5值是：")
        print_md5_for_directory(directory_path)
    else:
        print("无效的选项")

if __name__ == "__main__":
    main()
