from pycrawlers import huggingface
# 实例化类
hg = huggingface()



# 2.单个下载
url = 'https://huggingface.co/SurplusDeficit/GeLM'

# 默认保存位置在当前脚本所在文件夹 ./
hg.get_data(url)

