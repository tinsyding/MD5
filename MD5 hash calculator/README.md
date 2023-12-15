# MD5哈希值计算器

这个Python脚本提供了一个快速且简便的方式来计算文件、文件夹或字符串的MD5哈希值。适用于需要验证文件完整性、检测文件更改或简单地获取字符串的MD5哈希值的场景。

## 功能

- **文件MD5计算**：计算单个文件的MD5哈希值。
- **文件夹MD5计算**：递归计算一个文件夹内所有文件的MD5哈希值，并以树状结构显示。
- **字符串MD5计算**：计算任意字符串的MD5哈希值。

## 安装

本脚本需要Python环境。如果你的系统尚未安装Python，请先[下载并安装Python](https://www.python.org/downloads/)。

克隆仓库至本地：

```bash
git clone https://github.com/your-username/md5-calculator.git
cd md5-calculator
```

## 使用说明

1. 启动脚本：

    ```bash
    python md5_calculator.py
    ```

2. 根据提示输入文件路径、文件夹路径或字符串。

3. 查看终端输出的MD5哈希值或查看生成的`out.txt`文件获取更详细的信息。

## 示例

```shell
请输入文件路径、文件夹路径或字符串: example.txt
'example.txt'的MD5值是：[md5_hash_value]
```

```shell
请输入文件路径、文件夹路径或字符串: /path/to/directory
'/path/to/directory'文件夹内的文件MD5值是：
...
```