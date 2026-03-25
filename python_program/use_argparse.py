import argparse
# 创建 ArgumentParser 对象
parser = argparse.ArgumentParser(description="这是一个示例程序")
# 添加可选参数 --foo
parser.add_argument('--foo', type=int, help='一个整数参数')
# 添加位置参数 bar
parser.add_argument('bar', type=str, help='一个位置参数')
# 解析命令行参数
args = parser.parse_args()
# 使用解析后的参数
print(f'foo: {args.foo}')
print(f'bar: {args.bar}')

# 示例：见 use_argparse.py
# 使用步骤；
# 打开命令行或终端。
# 导航到脚本所在的目录：
# 如果你的脚本在桌面上，你需要先使用 cd 命令改变当前目录到桌面。例如，在 Windows 上可能是 cd Desktop，在 macOS 或 Linux 上可能是 cd ~/Desktop。
# 如果你的脚本在其他位置，使用相应的 cd 命令导航到那个位置。
# 运行脚本：
# 输入 python use_argparse.py hello --foo 42 并按下回车键。
# 注意：如果你的系统同时安装了 Python 2 和 Python 3，并且 python 命令默认指向 Python 2，你可能需要使用 python3 命令来运行脚本，即 python3 use_argparse.py hello --foo 42。
# 查看输出：
# 脚本运行后，你应该会在命令行或终端中看到输出，类似于 foo: 42 和 bar: hello

# 或者直接输入 python "D:\VSCodepythonprogram\python_program\use_argparse.py" hello --foo 42




