# -*- coding:utf-8 -*-
import os,_winreg
from PIL import Image

#用户目录
user_home =  os.path.expandvars('$HOME')
#windows聚焦图片原存储路径
original_path = user_home + r'\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'
#获取用户图片目录
keys = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders')
user_pic = _winreg.QueryValueEx(keys,'My Pictures')[0]
#将windows聚焦图片保存到此路径
target_path = os.path.join(user_pic,u'windows聚焦')

def isBg(pic):
    '判断是否合适做背景'
    width,hight = pic.size
    return True if width>hight and width > 1000 else False

def copyPic(pic,name):
    '拷贝聚焦图片'
    file_name = os.path.join(target_path,name+'.jpg')
    pic.save(file_name)


#获取图片名字
pic_names = os.listdir(original_path)
#创建目录
if not os.path.exists(target_path):
	os.makedirs(target_path)
#开始拷贝图片
for pic_name in pic_names:
	pic_dir = os.path.join(original_path,pic_name)
	try:
		pic_file = Image.open(pic_dir)
		if isBg(pic_file):
			copyPic(pic_file,pic_name)
	except Exception as e:
		print e
