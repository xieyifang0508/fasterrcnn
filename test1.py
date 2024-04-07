# 打开文件
with open('VOCdevkit/VOC2007/ImageSets/Main/test.txt', 'w') as file:
    # 依次输出从 "000001" 到 "001200"
    for i in range(1, 1201):
        # 将数字格式化为6位的字符串，左侧补零
        padded_number = str(i).zfill(6)
        # 写入文件，并添加换行符
        file.write(padded_number + '\n')