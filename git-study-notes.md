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

- 查看仓库中的文件状态：`git status`，我们刚刚修改了本文，所以可以看到当前文件有修改。

```bash
 ~/Desktop/huixing/OpenSource/learngit/ [master*] git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   git-study-notes.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   git-study-notes.md
```

- 把文件添加到版本库：`git add filename`，如果需要把当前目录下所有有变更的文件都添加到版本库的话，直接使用`git add .`，这样会将当前目录下所有文件都提交到版本库。

```bash
 ~/Desktop/huixing/OpenSource/learngit/ [master+*] git add git-study-notes.md
 ~/Desktop/huixing/OpenSource/learngit/ [master+] git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   git-study-notes.md
```

- 把文件提交到仓库：`git commit -m "更新日志"`，上面已经把文件添加到版本库了，接下来就可以直接提交了，提交完我们再输入`git status`就可以看到没有变更的文件了。

```bash
 ~/Desktop/huixing/OpenSource/learngit/ [master+] git commit -m "更新文档"
[master 2eb6793] 更新文档
 1 file changed, 47 insertions(+), 4 deletions(-)
 ~/Desktop/huixing/OpenSource/learngit/ [master] git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

- 版本变动查看：`git diff`命令用于显示工作目录中文件的差异，可以查看未提交的更改、已暂存的更改，以及不同提交质检的差异。`git diff`可以显示当前工作目录中所有未暂存的更改，`git diff --cached`查看已经通过`git add`暂存但尚未提交的更改，`git diff HEAD`显示工作目录中所有未暂存和已暂存的更改。

- 版本回退：`git reset --hard HEAD^`，其中`HEAD^`代表是上一个提交（父提交），

  >  `--hard`：回退到上个已提交的版本；`--soft`：回退到上个版本的未提交状态；`--mixed`：回退到上个版本已添加但未提交的状态。

```
 ~/Desktop/huixing/OpenSource/learngit/ [master*] git reset --hard HEAD^
HEAD is now at a7ea889 git学习笔记初次提交
```

- 如果不小心回退错误了，可以再回退回来，首先我们通过`git reflog`查看所有提交。

```
2eb6793 (HEAD -> master) HEAD@{0}: reset: moving to 2eb6793
a7ea889 (origin/master, dev) HEAD@{1}: reset: moving to a7ea889
a7ea889 (origin/master, dev) HEAD@{2}: reset: moving to HEAD^
2eb6793 (HEAD -> master) HEAD@{3}: commit: 更新文档
a7ea889 (origin/master, dev) HEAD@{4}: checkout: moving from dev to master
a7ea889 (origin/master, dev) HEAD@{5}: checkout: moving from master to dev
a7ea889 (origin/master, dev) HEAD@{6}: merge dev: Fast-forward
0f264e0 HEAD@{7}: checkout: moving from dev to master
a7ea889 (origin/master, dev) HEAD@{8}: checkout: moving from master to dev
0f264e0 HEAD@{9}: checkout: moving from dev to master
a7ea889 (origin/master, dev) HEAD@{10}: commit: git学习笔记初次提交
0f264e0 HEAD@{11}: checkout: moving from master to dev
0f264e0 HEAD@{12}: merge dev: Fast-forward
8054cb6 HEAD@{13}: checkout: moving from dev to master
0f264e0 HEAD@{14}: checkout: moving from master to dev
8054cb6 HEAD@{15}: checkout: moving from dev to master
0f264e0 HEAD@{16}: commit: dev 增加
8054cb6 HEAD@{17}: checkout: moving from master to dev
8054cb6 HEAD@{18}: checkout: moving from dev to master
8054cb6 HEAD@{19}: checkout: moving from master to dev
8054cb6 HEAD@{20}: checkout: moving from master to master
8054cb6 HEAD@{21}: commit: test
59c9e41 HEAD@{22}: Branch: renamed refs/heads/main to refs/heads/master
59c9e41 HEAD@{24}: commit: test
```

- 然后比如我现在想回到`a7ea889`这个版本，我就可以通过`git reset --hard a7ea889`来进行恢复。

```
 ~/Desktop/huixing/OpenSource/learngit/ [master] git reset --hard a7ea889
HEAD is now at a7ea889 git学习笔记初次提交
```

- 查看所有引用日志：`git reflog`，如果不小心
- 日志查看：普通查看：`git log`；美化输出：`git log pretty=oneline`
- 家里windows电脑测试