## python开发环境配置
#### 1. 下载python安装包
##### 1.1 首先去Pycharm官网，https://www.python.org/，下载python安装包，根据自己电脑的操作系统进行选择，对于windows系统步骤如下：
##### 1.2 选择Downloads，进入Windows版下载最新版本的python

![](https://imgkr2.cn-bj.ufileos.com/16d43f55-364f-4094-bb15-fa29b5f0953f.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=ZYVhQ1Zz77tMk5NlqVpVI4xDe4s%253D&Expires=1603546591)

##### 1.3 选择相对应的安装包，点击下载。

![](https://imgkr2.cn-bj.ufileos.com/108f7b5f-d504-40a2-977d-c597afc2c93c.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=Hy57b2Tg%252B6awkWLIAzD%252FtYDyGXc%253D&Expires=1603546558)
#### 2. 安装Python
##### 2.1 在Windows 64位系统上安装Python 3.9.0的步骤如下：

（1）双击下载后得到的安装文件python-3.9.0-amd64.exe，将显示安装向导对话框，选中“Add Python3.9.0 to PATH”复选框，表示将自动配置环境变量。

（2）单击“Customize installation”按钮，进行自定义安装（自定义安装可以修改安装路径），在弹出的安装选项对话框中采用默认设置。

（3）单击Next按钮，将打开高级选项对话框，在该对话框中，设置安装路径为“D:\Python\Python”（读者可自行设置路径），其他采用默认。

（4）单击Install按钮，开始安装Python。
#### 3. 测试Python是否安装成功
Python安装完成后，需要检测Python是否成功安装。打开cmd命令，启动命令行窗口，在当前的命令提示符后面输入“python”，按下<Enter>键，如果出现如图所示的信息，则说明Python安装成功，同时系统进入交互式Python解释器中。

![](https://imgkr2.cn-bj.ufileos.com/71b845b2-45f7-4b93-86af-b8c7769f89ee.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=9OENxv9BG%252FZfszNAhhEDwHLmD1E%253D&Expires=1603547014)

#### 4. 配置环境变量
先右键python.exe，选择属性，把路径Ctrl+C复制出来。
进入系统属性，找到高级系统设置，点击环境变量，在系统变量中找到PATH，双击打开，点击新建，然后把刚才复制的python.exe的路径复制过去。
  
![](https://imgkr2.cn-bj.ufileos.com/1fd9576c-cc65-48f2-9674-1ea3468aec98.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=ReS62IvjFGCVAZHERLR2fi00Zmo%253D&Expires=1603546816)
  
![](https://imgkr2.cn-bj.ufileos.com/984a875b-d61c-4a3a-83e5-e0dd372587c3.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=IKlku%252FbM34v5tIAumr984e8S2ko%253D&Expires=1603546927)

然后一直点确定。最后打开cmd，直接输入python。

![](https://imgkr2.cn-bj.ufileos.com/8ace9d01-dcba-42fc-b0d0-5b45e2e76945.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=C9edYbRtjfd%252FZv4b%252FtB2P0vpK3M%253D&Expires=1603546413)








