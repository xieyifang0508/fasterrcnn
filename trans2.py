# 打开 val.txt 文件以读取模式打开
with open('2007_val_relative.txt', 'r') as file:
    # 读取文件内容
    content = file.read()

# 将所有的 '\' 替换为 '/'
content = content.replace('\\', '/')

# 打开 val.txt 文件以写入模式打开
with open('2007_val_relative2.txt', 'w') as file:
    # 将替换后的内容写回文件
    file.write(content)

print("文件中所有的 '\\' 已被替换为 '/'")
