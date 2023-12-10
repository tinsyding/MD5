import hashlib

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

def main():
    """主函数"""
    print("选择MD5计算类型：")
    print("1. 文件")
    print("2. 字符串")
    choice = input("请输入选项（1或2）: ")

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
    else:
        print("无效的选项")

if __name__ == "__main__":
    main()