import os

# 读取原始文件
with open('2007_val.txt', 'r') as f:
    lines = f.readlines()

# 转换路径并写入新文件
with open('2007_val_relative.txt', 'w') as f:
    for line in lines:
        parts = line.strip().split(' ')
        # 获取文件名（包括路径）
        filepath = parts[0]
        # 获取相对路径
        relative_path = os.path.relpath(filepath, os.getcwd())
        # 将绝对路径改为相对路径
        parts[0] = relative_path
        # 写入新文件
        f.write(' '.join(parts) + '\n')
