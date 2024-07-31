---
title: Git&Github学习笔记
toc: true
tags:
	- git
	- github
categories:
	- 随笔
---

很多年前我就使用过Github，但是这么多年我基本只会用`clone`来下载东西，从来没有通过本地进行推送过，原因也很简单，因为我本职工作还是产品设计，并不会系统的写一个大项目，但是最近我在学习swift的过程中，我很想实现在公司写的代码，在我家电脑也能同步出现，我知道这个问题通过NAS是可以实现的，但是感觉不够优雅，于是我就又找了一些Git的使用教程开始了稍微深入下的学习。

学习教程我找的是廖雪峰的Git学习教程：[Git教程](https://liaoxuefeng.com/books/git/introduction/)

要学习Git，首先是如何创建Git，我的设备是Mac+Win10。Mac本身自带有Git，Win10在官网下载安装下即可，这里不赘述了。

## 创建Git仓库

- 创建Git仓库：在本地随便创建一个文件夹，路径不要带中文，然后进入这个文件夹，输入`git init`。

```bash
 ~/Desktop/huixing/OpenSource/learnGit1/ git init
Initialized empty Git repository in /Users/daniellau/Desktop/huixing/OpenSource/learnGit1/.git/
 ~/Desktop/huixing/OpenSource/learnGit1/ [main]
```

输入完`git init`之后就出现了一个`[main]`，这个代表已经创建好git仓库，同时在`main`分支下。此时我们要做的就是可以在当前文件夹内创建文件，我们输入`echo "hello world" > test.md`创建一个`test.md`文件，并在这个文件中写入了一句“hello world”。

```bash
 ~/Desktop/huixing/OpenSource/learnGit1/ [main] echo "hello world" > test.md
 ~/Desktop/huixing/OpenSource/learnGit1/ [main] ls
test.md
```

此时我们查看下这个文件下所有文件，使用`ls -ah`查看所有文件，包括隐藏的文件。

```
 ~/Desktop/huixing/OpenSource/learnGit1/ [main] ls -ah
.       ..      .git    test.md
```

可以看到此时文件夹内包含一个`.git`目录跟`test.md`文件，说明这个Git仓库创建完成了。

## 本地使用Git

Git的使用之前我只用过`clone`，但是clone其实是最简单的，而且不是核心说白了就是下载，下面是我总结的Git的一些核心使用功能（可能不全，大神勿喷）：

- 查看仓库中的文件状态：`git status`

- 把文件添加到版本库：`git add filename`
- 把文件提交到仓库：`git commit -m "更新日志"`
- 日志查看
  - 普通查看：`git log`
  - 美化输出：`git log pretty=oneline`
- 版本管理