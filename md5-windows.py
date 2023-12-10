import hashlib
import tkinter as tk
from tkinter import filedialog

def get_file_md5(filename):
    """计算并返回文件的MD5哈希值"""
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def select_file():
    """打开文件选择对话框并返回选择的文件路径"""
    root = tk.Tk()
    root.withdraw() # 不显示主窗口
    file_path = filedialog.askopenfilename()
    return file_path

def main():
    """主函数"""
    file_path = select_file()
    if file_path:
        md5_value = get_file_md5(file_path)
        print(f"'{file_path}'的MD5值是：{md5_value}")
    else:
        print("未选择文件")

if __name__ == "__main__":
    main()
