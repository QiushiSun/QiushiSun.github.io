---
title: "[2022] 配置一台用于开发的MacBook"
date: 2022-08-23 17:16:28 +0800
lang: zh
categories:
  - "misc"
tags:
  - "misc"
cover: "/assets/blog/configure-macbook-for-development-2022/cover.jpg"
excerpt: "在 2022 年配置一台用于开发的 MacBook 的完整记录。"
---
在2022年配置一台用于开发的MacBook



# 0 Macbook配置与基本信息

**14-inch MacBook Pro - Space Grey**

- 32GB unified memory
- Backlit Magic Keyboard with Touch ID - US English
- 1TB SSD storage
- 14-inch Liquid Retina XDR display
- Apple M1 Max with 10-core CPU, 24-core GPU, 16-core Neural Engine
- Three Thunderbolt 4 ports, HDMI port, SDXC card slot, MagSafe 3 port



# 1 系统偏好设置

## 1.1 打开电池百分比

现在的macOS默认不显示当前电池百分比，需要在系统偏好设置中手动打开

方法：系统偏好 - 程序坞和菜单 - 电池 - 显示电池百分比

![Show Battery Percentage](/assets/blog/configure-macbook-for-development-2022/show-battery.png "show battery")

## 1.2 显示蓝牙图标

不知道为什么苹果现在默认隐藏了蓝牙图标，需要先点开状态调上的控制中心才能找到蓝牙按钮，直接按住图标将其**拖拽**到上方状态栏即可。

![Show Bluetooth](/assets/blog/configure-macbook-for-development-2022/bluetooth.png "bluetooth")

## 1.3 文件路径

访达并不是那么好用，为了更直接的了解当前文件所在位置，个人建议显示文件的路径

方法：打开终端（Terminal）使用以下命令

```text
# show path bar
defaults write com.apple.finder ShowPathbar -bool true
```

![Show Path](/assets/blog/configure-macbook-for-development-2022/showpath.png)

## 1.4 访达窗口下方状态栏

为了更方便的用鼠标拖动的方式放大/缩小图标，以及查看当前位置的文件个数和状态，可以打开访达窗口下方的状态栏。

方法：打开终端（Terminal）使用以下命令

```text
# show status bar
defaults write com.apple.finder ShowStatusBar -bool true
```

![Show Status Bar](/assets/blog/configure-macbook-for-development-2022/showstatusbar.png)

## 1.5 触控板

触控板可以选择“单指轻触”来代替“按下”，并且自定义触控板速度

位置：系统偏好 - 触控板

![Trackpad](/assets/blog/configure-macbook-for-development-2022/Trackpad.png)

## 1.6 Screenshot

macOS的截屏很方便，使用默认快捷键command+shift+4即可，会得到一张高清png图，如果希望缩小截图所占空间，可以令系统默认使用jpeg格式。

```text
 defaults write com.apple.screencapture type jpg
```

## 1.7 外来软件权限

许多在软件官网下载安装包会因为苹果的安全限制无法打开，可以进入：系统偏好设置 - 安全性与隐私 - 通用，允许任意来源软件的安装。

![Security and Privacy](/assets/blog/configure-macbook-for-development-2022/security-and-privacy.png "security-and-privacy")

顺便可以解锁让Apple Watch解锁Mac的功能（记得先解锁Apple Watch）

Remark：如果找不到“任意来源”，可以使用命令行命令

```text
sudo spctl --master-disable
```

*此处需要输入PIN

# 2 终端与命令行

## 2.1 HOMEBREW

Homebrew是一款经典的开源软件包管理系统，它可被用来简化macOS系统上的软件安装过程。

```text
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

随后执行以下命令（会默认替换username），将Homebrew添加到环境变量

```text
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/username/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

使用Homebrew安装以下软件包

```text
brew install \
  wget \
  exa \
  git \
  nvm \
  pnpm \
  vips
```

## 2.2 iTerm2 & Oh My Zsh

### **2.2.1 iTerm2**

macOS自带的终端（Terminal）在灵活度和颜值上都稍有欠缺，在此推荐使用 [iTerm2](https://link.zhihu.com/?target=https%3A//iterm2.com/)，可以提供全屏编辑/窗口拆分/窗口透明等功能。

ZSH_THEME="powerlevel10k/powerlevel10k”

https://github.com/romkatv/powerlevel10k

### **2.2.2 Oh My Zsh**

Oh My Zsh是一款社区驱动的命令行（终端）工具，可以方便地配置主题，并提供了插件机制（如命令的自动补全、提示等），使用以下命令安装即可

```text
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/too
```

![Install Oh My Zsh](/assets/blog/configure-macbook-for-development-2022/omz-install.png)

随后，每当Oh My Zsh的配置改变时，都需要执行：

```text
source ~/.zshrc
```

我选择的主题是：*ZSH_THEME="powerlevel10k/powerlevel10k”*，在~/.zshrc文件中修改对应参数即可。也建议尝试omz的插件，比如 [zsh-autosuggestions](https://link.zhihu.com/?target=https%3A//github.com/zsh-users/zsh-autosuggestions) 等。

地址：[https://github.com/romkatv/powe](https://link.zhihu.com/?target=https%3A//github.com/romkatv/powerlevel10k)

# 3 软件推荐

接下来就是软件推荐清单了，仅仅是推荐一些个人常用的软件。除了日常应用外，我还选择了一些可能对CS/SE/DS等相关专业学生大裨益的软件。我将他们分成三个类别，并且附上了官网链接。

Remark：如果你和我一样使用的是M1系列芯片（包括M1 Pro 和 M1 Max），在官网下载时请选择apple silicon mac版本的软件

比较Intel与Apple Silicon：https://support.apple.com/en-us/HT211814

## 3.1 日常使用

1. [腾讯柠檬清理](https://link.zhihu.com/?target=https%3A//lemon.qq.com/)：据说是企鹅为数不多的良心产品，用来清理垃圾文件。
2. [CleanMyMac X](https://link.zhihu.com/?target=https%3A//cleanmymac.macpaw.com/)：功能更全面的系统垃圾清理软件，缺点是需要购买License。
3. [Snipaste](https://link.zhihu.com/?target=https%3A//www.snipaste.com/)：占用低但功能丰富的截图软件，目前macOS已经有了测试版，免费版即可覆盖大部分人的日常需求。
4. [欧路词典](https://link.zhihu.com/?target=https%3A//www.eudic.net/v4/en/app/download)：用了若干年的词典软件，个人是否好用取决于是否构建好适合自己的词典库。
5. Outlook：用于管理邮件，在App Store下载
6. The Unarchiver：非常好用的的macOS端解压软件，在App Store下载
7. [MonitorControl](https://link.zhihu.com/?target=https%3A//github.com/MonitorControl/MonitorControl)：外接显示器亮度调整（GitHub开源）
8. Zoom/Cisco Webex/腾讯会议，各取所需

## 3.2 笔记与文献管理

1. [Notion](https://link.zhihu.com/?target=https%3A//www.notion.so/)：全能型笔记软件，本人为重度用户，利用Notion构建了如电子图书馆，知识库等，有教育优惠。可以使用微信小程序Notion助手方便地通过分享链接保存知乎/微信公众号文章。此外，虽然我还有一年半的印象笔记订阅，但因其愈发过分的广告，我已在迁移出所有内容后将其弃用。
2. [Typora](https://link.zhihu.com/?target=https%3A//typora.io/)：轻量级Markdown编辑器
3. Zotero/Mendeley Desktop：用于文献管理，安装插件后可以和Notion搭配使用
4. [Mathpix](https://link.zhihu.com/?target=https%3A//mathpix.com/)：用于OCR数学公式，将其转为markdown语法
5. Goodnotes/Notability：老牌的笔记软件，在App Store下载
6. [Calibre](https://link.zhihu.com/?target=https%3A//calibre-ebook.com/)：用于电子书管理
7. [语雀](https://link.zhihu.com/?target=https%3A//www.yuque.com/)：用于构建/查看知识库、协作编辑，支持多种编辑器（其实网页版的飞书文档也不错）

## 3.3 开发用途

1. [Filezilla2](https://link.zhihu.com/?target=https%3A//filezilla-project.org/)：FTP传输客户端,用于向服务器（及跳板）传文件
2. [VS Code](https://link.zhihu.com/?target=https%3A//code.visualstudio.com/)：无需多言
3. Jetbrains全家桶（如果是学生身份可以无限白嫖）
4. [Sublime Text](https://link.zhihu.com/?target=https%3A//www.sublimetext.com/)：跨平台文本编辑器
5. [Navicat](https://link.zhihu.com/?target=https%3A//www.navicat.com/en/)：图形化数据库管理工具，用于连接本地和远程数据库
6. [GitHub Desktop](https://link.zhihu.com/?target=https%3A//desktop.github.com/)：通过图形界面更方便的管理GitHub仓库
7. [Docker](https://link.zhihu.com/?target=https%3A//www.docker.com/)：用于容器管理



一些关于 MacBook 的基本配置和软件推荐暂且就先介绍到这里，希望对读到这里的你有所帮助。



**Reference**

1. https://www.robinwieruch.de/mac-setup-web-development/
2. https://zhuanlan.zhihu.com/p/48207191
